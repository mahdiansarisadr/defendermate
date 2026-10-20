"""C2 net-effect composition rules R1-R7 plus rule-derived version-fact paths (G13)."""

from __future__ import annotations

import re
from collections import defaultdict

from packaging.specifiers import InvalidSpecifier, SpecifierSet
from packaging.version import Version
from pydantic import BaseModel

from .config import upgrade_slug
from .extract import canonical_version_value, condition_id, norm_symbol, short_hash
from .link import BM25, path_text, symbols_equal
from .llm import ExtractionFailed, LLMClient
from .models import (
    ChangeItem, Condition, ContextFact, Disagreement, DisqualifiedCandidate, Evidence, RequiresUpgrade, RiskPath,
    SearchQuery, SourceRecord, VersionFact,
)
from .normalize import normalize, opening_quote
from .planner import Plan, vkey
from .registry import Registry

_APIVER = re.compile(r"\b((?:[a-z0-9-]+\.)*[a-z0-9-]+/v\d+(?:(?:alpha|beta)\d+)?)\b")


# ---------- R4 / R5 ----------

def r4_on_path(items: list[ChangeItem], plan: Plan) -> tuple[list[ChangeItem], list[ChangeItem], list[ChangeItem]]:
    """Split items into (on path, future releases, dropped)."""
    on, future, dropped = [], [], []
    for it in items:
        if it.release == "*" or it.release in plan.releases:
            on.append(it)
        elif it.release in plan.future_releases:
            future.append(it)
        else:
            dropped.append(it)
    return on, future, dropped


def r5_start_applicability(paths: list[RiskPath], current: str) -> tuple[list[RiskPath], list[dict]]:
    keep, dropped = [], []
    for p in paths:
        spec = p.applies_to.from_versions if p.applies_to else None
        if spec:
            try:
                if Version(current) not in SpecifierSet(spec.replace(" ", "")):
                    dropped.append({"path_id": p.path_id, "rule": "R5", "applies_if_from": spec})
                    continue
            except (InvalidSpecifier, ValueError):
                p.conditions[0].ambiguities.append(f"Unparsed applicability specifier: {spec!r}")
        keep.append(p)
    return keep, dropped


# ---------- R1 reverts ----------

class _RevertLink(BaseModel):
    path_id: str | None
    quote: str
    explanation: str


def r1_reverts(client: LLMClient, paths: list[RiskPath], revert_items: list[ChangeItem], target: str,
               corpora: dict[str, str], inventory: dict[str, SourceRecord], ctx: dict
               ) -> tuple[list[RiskPath], list[DisqualifiedCandidate], list[str], list[dict]]:
    disq, unresolved, log = [], [], []
    by_release = defaultdict(list)
    for p in paths:
        by_release[p.introduced_in].append(p)
    removed: set[str] = set()
    for it in revert_items:
        cands = by_release.get(it.release, [])
        if not cands:
            continue
        idx = BM25([path_text(p) for p in cands])
        top = [cands[i] for i, _ in idx.search(it.text, k=5)]
        if not top:
            continue
        patch = it.source_id.split("@")[-1]
        try:
            res = client.complete("reconcile.v1", {
                **ctx, "patch_release": patch, "release": it.release, "revert_text": it.text,
                "candidates_json": [{"path_id": p.path_id, "path_name": p.path_name, "description": p.description}
                                    for p in top]}, _RevertLink, model_tier="strong", stage="reconcile")
        except ExtractionFailed:
            unresolved.append(f"Could not reconcile revert note in {patch}: {opening_quote(it.text, 20)}")
            continue
        log.append({"revert_item": it.item_id, "patch": patch, **res.model_dump()})
        hit = next((p for p in top if p.path_id == res.path_id), None)
        quote_ok = normalize(res.quote) in corpora.get(it.source_id, "")
        reverted_by_target = vkey(patch) <= vkey(target) or patch.startswith(target + ".")
        if hit is None or not quote_ok:
            unresolved.append(f"Revert note in {patch} not linked to a risk path ({res.explanation[:160]})")
            if quote_ok and reverted_by_target:
                q = normalize(res.quote)
                disq.append(DisqualifiedCandidate(
                    candidate_id=f"revert_{it.item_id}", statement=q,
                    reason=f"R1: a {it.release} change was reverted in {patch}, at or before the target; "
                           "no extracted risk path matched it, so the revert is recorded on its own.",
                    evidence=[Evidence(source_id=it.source_id, source_type=inventory[it.source_id].source_type,
                                       quote_or_summary=q, quote=q, verified=True,
                                       relevance="Patch release note stating the revert.")]))
            continue
        if reverted_by_target:
            hit.reverted_in = patch
            removed.add(hit.path_id)
            disq.append(DisqualifiedCandidate(
                candidate_id=hit.path_id, statement=hit.path_name,
                reason=f"R1: change introduced in {hit.introduced_in} was reverted in {patch}, at or before the target. {res.explanation}",
                evidence=[Evidence(source_id=it.source_id, source_type=inventory[it.source_id].source_type,
                                   quote_or_summary=normalize(res.quote), quote=normalize(res.quote), verified=True,
                                   relevance="Patch release note stating the revert.")]
                + [e for c in hit.conditions if c.category != "version" for e in c.evidence][:1],
            ))
    return [p for p in paths if p.path_id not in removed], disq, unresolved, log


# ---------- R2 supersession ----------

def r2_supersession(paths: list[RiskPath]) -> tuple[list[RiskPath], list[dict]]:
    cands = [p for p in paths if p.primary_symbol and p.introduced_in != "*"]
    groups: list[list[RiskPath]] = []
    for p in cands:
        for g in groups:
            if g[0].risk_type == p.risk_type and symbols_equal(g[0].primary_symbol, p.primary_symbol):
                g.append(p)
                break
        else:
            groups.append([p])
    superseded: set[str] = set()
    log = []
    for g in groups:
        sym = norm_symbol(g[0].primary_symbol)
        if len({p.introduced_in for p in g}) < 2:
            continue
        g.sort(key=lambda p: vkey(p.introduced_in))
        latest = g[-1]
        for older in g[:-1]:
            older.superseded_by = latest.path_id
            superseded.add(older.path_id)
            vc = next(c for c in latest.conditions if c.category == "version")
            vc.ambiguities.append(f"History: in {older.introduced_in}, '{older.path_name}' applied to the same symbol "
                                  f"({sym}); superseded by the {latest.introduced_in} change (R2).")
            for c in older.conditions:
                if c.category == "version":
                    continue
                for e in c.evidence:
                    if all(e.quote != x.quote for x in vc.evidence):
                        vc.evidence.append(e.model_copy(update={"relevance": f"Earlier ({older.introduced_in}) step for the same symbol: {e.relevance}"}))
                break
            latest.merged_from.append(older.path_id)
            log.append({"superseded": older.path_id, "by": latest.path_id, "symbol": sym})
    return [p for p in paths if p.path_id not in superseded], log


# ---------- R3 remediation chain (Kubernetes API versions) ----------

def removal_map(items: list[ChangeItem]) -> dict[str, dict]:
    """apiVersion -> {removed_in, replacements, item} from deprecation-guide style text."""
    out: dict[str, dict] = {}
    by_section: dict[tuple[str, ...], list[ChangeItem]] = defaultdict(list)
    for it in items:
        by_section[tuple(it.heading_path)].append(it)
    for sec, its in by_section.items():
        removed, repl, src = [], [], None
        for it in its:
            m = re.search(r"no longer served as of v(\d+\.\d+)", it.text)
            if m:
                for a in _APIVER.findall(it.text.split("API version")[0] if "API version" in it.text else it.text):
                    removed.append((a, m.group(1), it))
                src = src or it
            m2 = re.search(r"Migrate .*? to use the (.+?) API version", it.text)
            if m2:
                repl += _APIVER.findall(m2.group(1))
        for a, rel, it in removed:
            entry = out.setdefault(a, {"removed_in": rel, "replacements": [], "item": it})
            entry["replacements"] += [r for r in repl if r != a and r not in entry["replacements"]]
    return out


def r3_remediation(paths: list[RiskPath], rmap: dict[str, dict], target: str, inventory: dict[str, SourceRecord]
                   ) -> list[dict]:
    log = []
    for p in paths:
        own = {s.lower() for s in [p.primary_symbol, *p.symbols]}
        text = " ".join(p.suggested_actions)
        for api in sorted(set(_APIVER.findall(text))):
            info = rmap.get(api)
            if not info or api.lower() in own and api.lower() == p.primary_symbol.lower():
                continue
            removed_in = info["removed_in"]
            good = [r for r in info["replacements"] if r not in rmap or vkey(rmap[r]["removed_in"]) > vkey(target)]
            it: ChangeItem = info["item"]
            ev = Evidence(source_id=it.source_id, source_type=inventory[it.source_id].source_type,
                          quote_or_summary=opening_quote(it.text, 40), quote=opening_quote(it.text, 40), verified=True,
                          relevance=f"Shows that {api} is itself removed in v{removed_in}.")
            app = next((c for c in p.conditions if c.category != "version"), p.conditions[-1])
            if vkey(removed_in) <= vkey(target):
                note = (f"R3: the remediation names {api}, which is itself removed in v{removed_in} (at or before the "
                        f"target {target}); migrate to {', '.join(good) or 'a served version'} instead.")
                p.suggested_actions = [a + (f" [Superseded: {api} is removed in v{removed_in}; use {', '.join(good) or 'a served version'}.]" if api in a else "") for a in p.suggested_actions]
                if good:
                    p.suggested_actions.append(f"Migrate directly to {' or '.join(good)} (served at {target}).")
                p.review_flags.append("remediation_rewritten")
            else:
                note = (f"R3: the replacement {api} is removed later, in v{removed_in} (after target {target}); "
                        f"prefer {', '.join(good) or 'a GA version'} to avoid a second migration.")
            if note not in app.ambiguities:
                app.ambiguities.append(note)
                if all(e.quote != ev.quote for e in app.evidence):
                    app.evidence.append(ev)
                log.append({"path_id": p.path_id, "api": api, "removed_in": removed_in, "note": note})
    return log


# ---------- R6 future removals ----------

def r6_future_context(future_items: list[ChangeItem], inventory: dict[str, SourceRecord], target: str) -> list[ContextFact]:
    out = []
    for it in future_items:
        if it.section_type not in ("removed", "deprecated", "other", "incompatible") or len(it.text) < 30:
            continue
        q = opening_quote(it.text, 40)
        out.append(ContextFact(
            fact_id=f"future_{it.item_id}", statement=f"Scheduled for removal in {it.release} (after target {target}): {q}",
            introduced_in=it.release,
            evidence=[Evidence(source_id=it.source_id, source_type=inventory[it.source_id].source_type,
                               quote_or_summary=q, quote=q, verified=True,
                               relevance=f"Listed under release {it.release} in the deprecation/removal timeline.")],
            why_not_risk=f"Still works at {target}; it is removed only in {it.release}, after the target (R6).",
            fires_at="future_removal",
        ))
    return out


# ---------- G13 version-fact paths and R7 ----------

def _floor(spec: str) -> str | None:
    m = re.search(r">=\s*([\d.]+)", spec) or re.search(r"\^([\d.]+)", spec)
    return m.group(1) if m else None


def fact_paths(reg: Registry, facts: list[VersionFact], plan: Plan, project_slug: str,
               inventory: dict[str, SourceRecord]) -> tuple[list[RiskPath], list[RequiresUpgrade]]:
    paths, reqs = [], []
    for spec in reg.version_facts:
        for field, json_path in spec.fields.items():
            fs = [f for f in facts if f.field == field]
            cur = [f for f in fs if f.release == plan.current_version]
            tgt = [f for f in fs if f.release == plan.target_version]
            if not cur or not tgt:
                continue
            c, t = cur[-1], max(tgt, key=lambda f: f.source_id)
            if c.value == t.value:
                continue
            label = spec.labels.get(field, field)
            def ev(f: VersionFact, why: str) -> Evidence:
                return Evidence(source_id=f.source_id, source_type="package_registry_metadata",
                                quote_or_summary=f"{f.json_path} = {f.value!r}", relevance=why, json_path=f.json_path,
                                expected=f.value, verified=True)
            floor = _floor(t.value)
            vcond = Condition(
                condition_id=condition_id(f"{field} requirement changes {c.value} {t.value}"),
                statement=f"{reg.project} {plan.target_version} declares {label} requirement {t.value!r} "
                          f"(was {c.value!r} in {plan.current_version}).",
                category="version", required=True, operator="in_range",
                expected_value=canonical_version_value(plan.target_version),
                evidence=[ev(c, f"{label} requirement at the current version."), ev(t, f"{label} requirement at the target version.")],
                confidence="low", derived_by="rule",
            )
            is_runtime = field in ("node", "python")
            app = Condition(
                condition_id=condition_id(f"deployment {field} below {floor}"),
                statement=f"The application's {label} version does not satisfy {t.value!r}"
                          + (f" (is below {floor})." if floor else "."),
                category="runtime" if is_runtime else "dependency", required=True,
                operator="less_than" if floor else "not_equals", expected_value=floor or t.value,
                evidence=[ev(t, f"Package metadata of the target version requires {t.value!r}.")],
                confidence="low", derived_by="rule",
                search_queries=_fact_queries(field),
            )
            key = short_hash(reg.project, "facts", field, n=10)
            paths.append(RiskPath(
                path_id=f"{project_slug}_{key}", path_name=f"{label} requirement raised to {t.value}",
                risk_type="runtime_requirement" if is_runtime else "dependency_requirement",
                risk_level="critical" if is_runtime else "high",
                affected_surface="runtime" if is_runtime else "dependencies",
                description=f"Package metadata changes the {label} requirement from {c.value!r} ({plan.current_version}) "
                            f"to {t.value!r} ({plan.target_version}). Installs or runtimes that do not satisfy it fail.",
                conditions=[vcond, app],
                suggested_actions=[f"Check the deployed {label} version against {t.value!r} before upgrading."],
                introduced_in=plan.target_version, primary_symbol=label, symbols=[label, field],
            ))
            if field in spec.cross_project:
                cp = spec.cross_project[field]
                reqs.append(RequiresUpgrade(
                    project=cp.project, current_version=cp.current_version, target_version=cp.target_version,
                    reason=f"{reg.project} {plan.target_version} requires {label} {t.value!r}; apps on {cp.project} "
                           f"{cp.current_version} must also upgrade {cp.project} (R7).",
                    evidence=[ev(t, "Peer dependency range of the target version.")],
                    model_ref=upgrade_slug(cp.project, cp.current_version, cp.target_version),
                ))
    return paths, reqs


def _fact_queries(field: str) -> list[SearchQuery]:
    if field == "node":
        return [SearchQuery(tool="ripgrep", query=r'"node"\s*:\s*"|FROM node:|node-version'),
                SearchQuery(tool="ripgrep", query=r"^\s*\d+(\.\d+)*\s*$ --glob .nvmrc")]
    if field == "python":
        return [SearchQuery(tool="ripgrep", query=r"python_requires|requires-python|FROM python:|python_version")]
    if field == "react_peer":
        return [SearchQuery(tool="ripgrep", query=r'"react"\s*:\s*"')]
    return []


def fact_disagreements(paths: list[RiskPath], facts: list[VersionFact], reg: Registry,
                       inventory: dict[str, SourceRecord]) -> list[Disagreement]:
    """L6: prose minimum versions that contradict package metadata for the same release."""
    out: list[Disagreement] = []
    keywords = {"node": r"node\.?js", "python": r"python", "react_peer": r"react"}
    for spec in reg.version_facts:
        for field in spec.fields:
            kw = keywords.get(field, field)
            for p in paths:
                for c in p.conditions:
                    for e in c.evidence:
                        if not e.quote or e.json_path:
                            continue
                        m = re.search(rf"minimum {kw} version has been bumped from [\d.]+ to (\d+(?:\.\d+)*)", e.quote, re.I)
                        if not m:
                            continue
                        prose = m.group(1)
                        # R2 keeps superseded evidence on the surviving path, so compare against the
                        # release the quoting source documents, not the path's release.
                        src_rel = inventory[e.source_id].release if e.source_id in inventory else None
                        rel = src_rel if src_rel and src_rel != "*" else p.introduced_in
                        rel_facts = sorted([f for f in facts if f.field == field and f.release == rel],
                                           key=lambda f: vkey(f.source_id.split("@v")[-1]))
                        if not rel_facts:
                            continue
                        first = rel_facts[0]
                        floors = {f.source_id: _floor(f.value) for f in rel_facts}
                        if _floor(first.value) and vkey(_floor(first.value)) != vkey(prose):
                            later = [sid for sid, fl in floors.items() if fl and vkey(fl) == vkey(prose)]
                            detail = (f"{inventory[e.source_id].title} says the minimum {spec.labels.get(field, field)} "
                                      f"for {rel} is {prose}; {first.source_id} ({first.json_path}) says {first.value!r}.")
                            res = ("Package metadata outranks prose. "
                                   + (f"The prose matches later {rel}.x metadata ({', '.join(later)}), so the page was "
                                      f"likely edited after release to reflect the latest {rel}.x floor."
                                      if later else "No metadata version matches the prose value."))
                            d = Disagreement(topic=f"{field} minimum for {rel}", sources=[e.source_id, first.source_id]
                                             + later, detail=detail, resolution=res)
                            if all(x.detail != d.detail for x in out):
                                out.append(d)
                            amb = f"Source disagreement: {detail} {res}"
                            if amb not in c.ambiguities:
                                c.ambiguities.append(amb)
    return out
