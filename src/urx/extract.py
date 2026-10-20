"""B2 extraction: strong model, structured output, quotes verified against the source corpus (TDD B2, G9, G10)."""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from typing import Literal

from pydantic import BaseModel

from .llm import ExtractionFailed, LLMClient
from .models import (
    APP_SIDE_CATEGORIES, AppliesTo, Category, ChangeItem, Condition, ContextFact, DerivedBy, Evidence, FiresAt,
    Operator, RiskLevel, RiskPath, RiskType, Role, SearchQuery, SourceRecord, Surface, VersionFact,
)
from .normalize import normalize, opening_quote


class DraftQuery(BaseModel):
    tool: Literal["ripgrep", "kubectl", "sql"]
    query: str


class DraftCondition(BaseModel):
    statement: str
    category: Category
    role: Role
    operator: Operator
    expected_value: str
    quotes: list[str]
    relevance: str
    ambiguities: list[str]
    derived_by: DerivedBy
    search_queries: list[DraftQuery]


class DraftAppliesTo(BaseModel):
    upgrade_method: str | None
    cluster_type: str | None
    from_versions: str | None


class DraftPath(BaseModel):
    path_name: str
    risk_type: RiskType
    risk_level: RiskLevel
    affected_surface: Surface
    description: str
    primary_symbol: str
    symbols: list[str]
    fires_at: FiresAt
    applies_to: DraftAppliesTo
    conditions: list[DraftCondition]
    suggested_actions: list[str]


class ExtractionResult(BaseModel):
    disposition: Literal["risk", "context"]
    context_reason: str
    paths: list[DraftPath]


def slug(text: str, n: int = 40) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")[:n].strip("_")


def short_hash(*parts: str, n: int = 8) -> str:
    return hashlib.sha1("|".join(parts).encode()).hexdigest()[:n]


def norm_symbol(s: str) -> str:
    s = s.strip().strip("`").replace("()", "").strip().lower()
    s = re.sub(r"\s+(setting|function|method|class|api|argument|parameter)$", "", s)
    if s.endswith(".js"):
        s = s[:-3]
    if "/" not in s and re.fullmatch(r"[\w]+(\.[\w]+)+", s):
        s = s.split(".")[-1]
    return s


def risk_key(project: str, release: str, primary: str, risk_type: str) -> str:
    return short_hash(project, release, norm_symbol(primary), risk_type, n=10)


def condition_id(statement: str) -> str:
    return f"{slug(statement, 40)}_{short_hash(normalize(statement), n=6)}"


def canonical_version_value(release: str) -> dict:
    if release == "*":
        return {"applies_to": "every release hop on the upgrade path"}
    return {"current_version": f"< {release}", "target_version": f">= {release}"}


@dataclass
class ItemResult:
    item: ChangeItem
    paths: list[RiskPath] = field(default_factory=list)
    context: ContextFact | None = None
    rejected: list[dict] = field(default_factory=list)
    failed: str | None = None


def _bad_quotes(res: ExtractionResult, corpus: str) -> list[str]:
    return [q for p in res.paths for c in p.conditions for q in c.quotes if normalize(q) not in corpus]


def extract_item(client: LLMClient, item: ChangeItem, parent_text: str, facts: list[VersionFact],
                 src: SourceRecord, corpus: str, ctx: dict, project_slug: str) -> ItemResult:
    out = ItemResult(item=item)
    variables = {
        **ctx, "release": item.release, "source_title": src.title, "source_type": src.source_type,
        "heading_path": " / ".join(item.heading_path), "item_text": item.text,
        "parent_text": parent_text or "(none)",
        "facts": [f.model_dump() for f in facts] or "none",
    }
    try:
        res = client.complete("extract.v1", variables, ExtractionResult, model_tier="strong", max_tokens=12000,
                              stage="extract")
        bad = _bad_quotes(res, corpus)
        if bad:
            note = ("These quotes are NOT exact substrings of the ITEM/PARENT text: "
                    + " | ".join(repr(b) for b in bad[:10])
                    + ". Re-emit the complete answer; copy every quote exactly, character for character.")
            res = client.complete("extract.v1", variables, ExtractionResult, model_tier="strong", max_tokens=12000,
                                  stage="extract_repair", repair_note=note)
    except ExtractionFailed as e:
        out.failed = str(e)
        return out

    if res.disposition == "context" or not res.paths:
        out.context = ContextFact(
            fact_id=f"ctx_{item.item_id}", statement=opening_quote(item.text, 40), introduced_in=item.release,
            evidence=[Evidence(source_id=item.source_id, source_type=src.source_type,
                               quote_or_summary=opening_quote(item.text, 40), quote=opening_quote(item.text, 40),
                               verified=True, relevance="Item text in the release documentation.")],
            why_not_risk=res.context_reason or "Extractor found no actionable risk.",
            fires_at="future_removal" if item.section_type == "deprecated" else None,
        )
        return out

    used_ids: set[str] = set()
    for dp in res.paths:
        conditions: list[Condition] = []
        for dc in dp.conditions:
            ev: list[Evidence] = []
            for q in dc.quotes:
                if normalize(q) in corpus:
                    ev.append(Evidence(source_id=item.source_id, source_type=src.source_type,
                                       quote_or_summary=normalize(q), quote=normalize(q), verified=True,
                                       relevance=dc.relevance))
                else:
                    out.rejected.append({"item_id": item.item_id, "kind": "quote_not_found", "quote": q,
                                         "statement": dc.statement})
            if not ev and not (dc.role == "uncertain" and dc.ambiguities):
                out.rejected.append({"item_id": item.item_id, "kind": "condition_without_evidence",
                                     "statement": dc.statement})
                continue
            conditions.append(Condition(
                condition_id=condition_id(dc.statement), statement=dc.statement, category=dc.category,
                required=dc.role == "required", operator=dc.operator, expected_value=dc.expected_value,
                evidence=ev, confidence="low", ambiguities=dc.ambiguities, role=dc.role, derived_by=dc.derived_by,
                search_queries=[SearchQuery(tool=q.tool, query=q.query) for q in dc.search_queries],
            ))

        version_conds = [c for c in conditions if c.category == "version"]
        if version_conds:
            v = version_conds[0]
            v.operator = "in_range"
            v.expected_value = canonical_version_value(item.release)
        else:
            q = opening_quote(item.text, 30)
            conditions.insert(0, Condition(
                condition_id=condition_id(f"upgrade crosses {item.release}"),
                statement=f"The upgrade crosses {src.title.split(':')[0]} release {item.release}, where this change is documented.",
                category="version", required=True, operator="in_range",
                expected_value=canonical_version_value(item.release),
                evidence=[Evidence(source_id=item.source_id, source_type=src.source_type, quote_or_summary=q,
                                   quote=q, verified=True,
                                   relevance=f"The change is listed in the {item.release} documentation section '{' / '.join(item.heading_path[-2:])}'.")],
                confidence="low", role="required", derived_by="rule",
            ))
        if not any(c.category in APP_SIDE_CATEGORIES for c in conditions):
            out.rejected.append({"item_id": item.item_id, "kind": "path_without_app_condition", "path_name": dp.path_name})
            continue

        key = risk_key(item.project, item.release, dp.primary_symbol or dp.path_name, dp.risk_type)
        pid = f"{project_slug}_{key}"
        n = 2
        while pid in used_ids:
            pid = f"{project_slug}_{key}_{n}"
            n += 1
        used_ids.add(pid)
        at = dp.applies_to
        out.paths.append(RiskPath(
            path_id=pid, path_name=dp.path_name, risk_type=dp.risk_type, risk_level=dp.risk_level,
            affected_surface=dp.affected_surface, description=dp.description, conditions=conditions,
            suggested_actions=dp.suggested_actions, fires_at=dp.fires_at, introduced_in=item.release,
            applies_to=AppliesTo(**at.model_dump()) if any(at.model_dump().values()) else None,
            primary_symbol=dp.primary_symbol, symbols=dp.symbols or item.symbols, source_item_ids=[item.item_id],
        ))
    return out
