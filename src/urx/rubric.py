"""C3 deterministic confidence rubric. LLM outputs never carry confidence."""

from __future__ import annotations

from .models import Condition, Confidence, RiskPath

_RANK = {"low": 0, "medium": 1, "high": 2}


def base_source(source_id: str) -> str:
    return source_id.split("@")[0]


def condition_confidence(c: Condition, tiers: dict[str, int]) -> tuple[Confidence, int, list[str]]:
    score, why = 0, []
    ev_tiers = [tiers.get(e.source_id, 3) for e in c.evidence]
    if any(t == 1 for t in ev_tiers):
        score += 2
        why.append("+2 tier-1 evidence")
    if len({base_source(e.source_id) for e in c.evidence}) >= 2:
        score += 1
        why.append("+1 corroborated by 2+ independent sources")
    if any(e.json_path and e.verified for e in c.evidence):
        score += 1
        why.append("+1 package-metadata json_path agrees")
    if c.derived_by == "inference":
        score -= 2
        why.append("-2 inferred, not stated")
    if c.ambiguities:
        score -= 1
        why.append("-1 has ambiguities")
    if c.judge and c.judge.verdict == "partially_supported":
        score -= 1
        why.append("-1 judge: partially supported")
    conf: Confidence = "high" if score >= 2 else "medium" if score >= 0 else "low"
    if c.role == "uncertain" or (c.judge and c.judge.verdict == "not_supported"):
        conf = "low"
        why.append("cap: uncertain or judge not supported -> low")
    elif ev_tiers and min(ev_tiers) > 1 and conf == "high":
        conf = "medium"
        why.append("cap: tier 2/3 only -> at most medium")
    elif not ev_tiers:
        conf = "low"
    return conf, score, why


def apply_rubric(paths: list[RiskPath], tiers: dict[str, int]) -> None:
    for p in paths:
        for c in p.conditions:
            c.confidence = condition_confidence(c, tiers)[0]
        core = [c for c in p.conditions if c.role in ("required", "alternative")] or p.conditions
        p.confidence = min((c.confidence for c in core), key=lambda x: _RANK[x])


def overall_confidence(paths: list[RiskPath], failures: int, rejected_tier1: int) -> Confidence:
    if not paths:
        return "low"
    share = sum(p.confidence == "high" for p in paths) / len(paths)
    if share >= 0.7 and failures == 0 and rejected_tier1 == 0:
        return "high"
    return "medium" if share >= 0.4 else "low"
