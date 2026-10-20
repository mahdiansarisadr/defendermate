"""JSON metadata adapter: dotted-path lookups for version facts (TDD A5)."""

from __future__ import annotations

import json
from typing import Any

_MISSING = object()


def load(raw: str) -> Any:
    return json.loads(raw)


def lookup(doc: Any, dotted: str) -> Any:
    cur = doc
    for part in dotted.split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        elif isinstance(cur, list) and part.isdigit() and int(part) < len(cur):
            cur = cur[int(part)]
        else:
            return _MISSING
    return cur


def lookup_str(doc: Any, dotted: str) -> str | None:
    v = lookup(doc, dotted)
    if v is _MISSING or v is None:
        return None
    return v if isinstance(v, str) else json.dumps(v, sort_keys=True)
