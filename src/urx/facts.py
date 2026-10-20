"""Deterministic version facts from package metadata (TDD A5)."""

from __future__ import annotations

from .adapters import json_meta
from .fetch import Fetched
from .models import VersionFact
from .registry import Registry


def extract_facts(reg: Registry, fetched: list[Fetched]) -> list[VersionFact]:
    out: list[VersionFact] = []
    by_reg = {}
    for f in fetched:
        by_reg.setdefault(f.source.registry_source, []).append(f)
    for spec in reg.version_facts:
        for f in by_reg.get(spec.source_id, []):
            doc = json_meta.load(f.text)
            for field, path in spec.fields.items():
                v = json_meta.lookup_str(doc, path)
                if v is not None:
                    out.append(VersionFact(release=f.source.release or "", field=field, value=v,
                                           source_id=f.source.inventory_id, json_path=path))
    return out


def facts_for_release(facts: list[VersionFact], release: str) -> list[VersionFact]:
    return [f for f in facts if f.release == release]
