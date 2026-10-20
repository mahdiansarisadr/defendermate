"""C7 human review decisions, keyed by stable IDs and re-applied on every run."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Literal

import yaml
from pydantic import BaseModel, Field

from . import config
from .models import LEVEL_ORDER, DisqualifiedCandidate, RiskPath

_RANK = {"low": 0, "medium": 1, "high": 2}


class Override(BaseModel):
    id: str                                    # path_id or path_id/condition_id
    decision: Literal["accept", "reject", "edit"]
    edits: dict = Field(default_factory=dict)  # statement, risk_level, confidence_floor
    reviewer: str = "reviewer"
    note: str = ""
    at: str = ""


def load_overrides(path=None) -> list[Override]:
    p = path or config.REVIEW_FILE
    if not p.exists():
        return []
    return [Override.model_validate(x) for x in (yaml.safe_load(p.read_text()) or [])]


def save_override(ov: Override, path=None) -> list[Override]:
    p = path or config.REVIEW_FILE
    items = [o for o in load_overrides(p) if o.id != ov.id]
    ov.at = ov.at or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    items.append(ov)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(yaml.safe_dump([o.model_dump() for o in items], sort_keys=False, allow_unicode=True))
    return items


def delete_override(oid: str, path=None) -> None:
    p = path or config.REVIEW_FILE
    items = [o for o in load_overrides(p) if o.id != oid]
    p.write_text(yaml.safe_dump([o.model_dump() for o in items], sort_keys=False, allow_unicode=True))


def apply_overrides(paths: list[RiskPath], overrides: list[Override]) -> list[DisqualifiedCandidate]:
    by_id = {o.id: o for o in overrides}
    disq: list[DisqualifiedCandidate] = []
    keep: list[RiskPath] = []
    for p in paths:
        o = by_id.get(p.path_id)
        if o and o.decision == "reject":
            ev = [e for c in p.conditions if c.category != "version" for e in c.evidence][:1] or p.conditions[0].evidence[:1]
            disq.append(DisqualifiedCandidate(candidate_id=p.path_id, statement=p.path_name,
                                              reason=f"Rejected in human review by {o.reviewer}: {o.note}", evidence=ev))
            continue
        if o:
            p.review_status = "accepted" if o.decision == "accept" else "edited"
            if lvl := o.edits.get("risk_level"):
                if lvl in LEVEL_ORDER:
                    p.risk_level = lvl
            if desc := o.edits.get("description"):
                p.description = desc
        for c in p.conditions:
            co = by_id.get(f"{p.path_id}/{c.condition_id}")
            if not co:
                continue
            if co.decision == "reject":
                c.role, c.required = "uncertain", False
                c.ambiguities.append(f"Rejected in human review: {co.note}")
                c.confidence = "low"
            if st := co.edits.get("statement"):
                c.statement = st
            floor = co.edits.get("confidence_floor")
            if floor in ("medium", "low") and _RANK[c.confidence] < _RANK[floor]:
                c.confidence = floor
        keep.append(p)
    paths[:] = keep
    return disq
