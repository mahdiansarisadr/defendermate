"""C4 deterministic validator. Recomputes every check from cache/; never trusts `verified` flags."""

from __future__ import annotations

import json
from dataclasses import dataclass
from functools import lru_cache
from typing import Any, Protocol

import jsonschema
from pydantic import ValidationError

from . import config
from .adapters import doc_text, json_meta, parse
from .fetch import EXT
from .models import APP_SIDE_CATEGORIES, RiskModel
from .normalize import normalize
from .registry import load_registry


@dataclass
class Issue:
    level: str        # error | warning
    code: str
    where: str
    message: str

    def to_dict(self) -> dict:
        return self.__dict__.copy()


class Context(Protocol):
    def corpus(self, source_id: str) -> str | None: ...
    def json_doc(self, source_id: str) -> Any | None: ...
    def model_exists(self, ref: str) -> bool: ...


class CacheContext:
    """Resolves inventory source ids to cached files through the registry."""

    def __init__(self, project: str, inventory: list[dict]) -> None:
        self.project = project
        self.reg = load_registry(project)
        self.inv = {s["source_id"]: s for s in inventory}

    def _path(self, source_id: str):
        rec = self.inv.get(source_id)
        if not rec:
            return None, None
        spec = next((s for s in self.reg.sources if s.id == rec["registry_source"]), None)
        if not spec:
            return None, None
        label = source_id.split("@", 1)[1] if "@" in source_id else "doc"
        import re
        name = re.sub(r"[^A-Za-z0-9._-]", "_", label)
        return config.CACHE_DIR / config.slugify(self.project) / spec.id / f"{name}.{EXT[spec.format]}", spec.format

    def corpus(self, source_id: str) -> str | None:
        return _corpus(*self._path(source_id))

    def json_doc(self, source_id: str) -> Any | None:
        p, fmt = self._path(source_id)
        if p is None or fmt != "json" or not p.exists():
            return None
        return json_meta.load(p.read_text())

    def model_exists(self, ref: str) -> bool:
        return (config.OUTPUTS_DIR / ref / "risk_model.json").exists()


@lru_cache(maxsize=256)
def _corpus(path, fmt) -> str | None:
    if path is None or not path.exists():
        return None
    if fmt == "json":
        return normalize(path.read_text())
    return doc_text(parse(path.read_text(encoding="utf-8"), fmt))


@lru_cache(maxsize=1)
def _schema() -> dict:
    return json.loads((config.SCHEMAS_DIR / "risk_model.schema.json").read_text())


def verify_quote(quote: str, corpus: str | None) -> bool:
    return bool(corpus) and normalize(quote) in corpus  # exact after normalization; no fuzzy matching (L16)


def validate_model(data: dict, ctx: Context, extra_models: set[str] | None = None) -> list[Issue]:
    issues: list[Issue] = []

    def err(code: str, where: str, msg: str) -> None:
        issues.append(Issue("error", code, where, msg))

    def warn(code: str, where: str, msg: str) -> None:
        issues.append(Issue("warning", code, where, msg))

    # E1 schema + enums
    try:
        jsonschema.validate(data, _schema())
    except jsonschema.ValidationError as e:
        err("E1_schema", "/".join(map(str, e.absolute_path)), e.message[:300])
        return issues
    try:
        model = RiskModel.model_validate(data)
    except ValidationError as e:
        err("E1_schema", "model", str(e)[:300])
        return issues
    if model.disclaimer != config.DISCLAIMER:
        err("E1_schema", "disclaimer", "missing or altered disclaimer")

    inv = {s.source_id: s for s in model.source_inventory}
    tiers = {s.source_id: s.authority_tier for s in model.source_inventory}

    def check_evidence(ev, where: str) -> bool:
        ok = True
        src = inv.get(ev.source_id)
        if src is None or src.status != "used":
            err("E2_unknown_source", where, f"evidence source {ev.source_id!r} not in inventory with status 'used'")
            return False
        if src.source_type != ev.source_type:
            err("E2_unknown_source", where, f"source_type {ev.source_type} != inventory {src.source_type}")
            ok = False
        if ev.json_path:
            doc = ctx.json_doc(ev.source_id)
            actual = json_meta.lookup_str(doc, ev.json_path) if doc is not None else None
            if actual is None or actual != ev.expected:
                err("E4_json_path", where, f"{ev.source_id}:{ev.json_path} is {actual!r}, evidence expects {ev.expected!r}")
                ok = False
        elif ev.quote is not None:
            if not verify_quote(ev.quote, ctx.corpus(ev.source_id)):
                err("E3_quote_not_found", where, f"quote not found verbatim in {ev.source_id}: {ev.quote[:120]!r}")
                ok = False
            if normalize(ev.quote_or_summary) != normalize(ev.quote):
                err("E3_quote_not_found", where, "quote_or_summary must mirror quote")
                ok = False
            if len(ev.quote.split()) > 40:
                warn("W2_long_quote", where, f"quote has {len(ev.quote.split())} words (>40)")
        else:
            err("E3_quote_not_found", where, "evidence has neither a verbatim quote nor a json_path")
            ok = False
        return ok

    path_ids: set[str] = set()
    for p in model.risk_paths:
        w = f"risk_paths/{p.path_id}"
        if p.path_id in path_ids:
            err("E9_duplicate_id", w, "duplicate path_id")
        path_ids.add(p.path_id)
        cats = [c.category for c in p.conditions]
        if "version" not in cats:
            err("E5_structure", w, "path has no version condition")
        if not any(c in APP_SIDE_CATEGORIES for c in cats):
            err("E5_structure", w, "path has no application/deployment condition")
        if not p.suggested_actions:
            warn("W1_no_actions", w, "no suggested actions")
        cond_ids: set[str] = set()
        for c in p.conditions:
            cw = f"{w}/{c.condition_id}"
            if c.condition_id in cond_ids:
                err("E9_duplicate_id", cw, "duplicate condition_id within path")
            cond_ids.add(c.condition_id)
            if c.required != (c.role == "required"):
                err("E11_role_mismatch", cw, f"required={c.required} inconsistent with role={c.role}")
            if not c.evidence and not (c.role == "uncertain" and c.ambiguities):
                err("E6_no_evidence", cw, "condition has no evidence and is not an uncertain condition with ambiguities")
            for ev in c.evidence:
                check_evidence(ev, cw)
            if c.confidence == "high" and not any(tiers.get(e.source_id) == 1 for e in c.evidence):
                err("E7_high_without_tier1", cw, "confidence high without tier-1 evidence")
            if c.derived_by == "inference" and c.confidence == "high":
                warn("W3_inferred_high", cw, "inferred condition marked high")
            if c.category in APP_SIDE_CATEGORIES and c.operator in ("present", "contains") and not c.search_queries:
                warn("W4_no_search_queries", cw, "symbol-bearing app condition has no search queries")

    known = extra_models or set()
    for r in model.requires_upgrades:
        if r.model_ref not in known and not ctx.model_exists(r.model_ref):
            err("E8_dangling_requires", f"requires_upgrades/{r.model_ref}", "referenced risk model does not exist")
        for ev in r.evidence:
            check_evidence(ev, f"requires_upgrades/{r.model_ref}")
    for f in model.context_facts:
        for ev in f.evidence:
            check_evidence(ev, f"context_facts/{f.fact_id}")
        if not f.evidence:
            err("E10_unverifiable_context", f"context_facts/{f.fact_id}", "context fact without evidence")
    for d in model.disqualified_candidates:
        for ev in d.evidence:
            check_evidence(ev, f"disqualified_candidates/{d.candidate_id}")
        if not d.evidence:
            err("E10_unverifiable_context", f"disqualified_candidates/{d.candidate_id}", "disqualified without evidence")
    return issues


def summarize(issues: list[Issue]) -> dict:
    from collections import Counter

    return {"errors": sum(i.level == "error" for i in issues), "warnings": sum(i.level == "warning" for i in issues),
            "by_code": dict(Counter(i.code for i in issues))}
