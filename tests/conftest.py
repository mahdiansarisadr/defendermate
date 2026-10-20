from __future__ import annotations

import copy
from pathlib import Path

import pytest

from urx import config
from urx.adapters import doc_text, parse

CACHE = config.CACHE_DIR


def cached(rel: str) -> Path:
    p = CACHE / rel
    if not p.exists():
        pytest.skip(f"cache file {rel} missing; run `urx extract` online once")
    return p


def blocks_of(rel: str, fmt: str):
    return parse(cached(rel).read_text(), fmt)


class FakeCtx:
    """Validator context backed by in-memory corpora."""

    def __init__(self, corpora: dict[str, str], json_docs: dict | None = None, models: set[str] | None = None):
        self.corpora, self.json_docs, self.models = corpora, json_docs or {}, models or set()

    def corpus(self, sid):
        return self.corpora.get(sid)

    def json_doc(self, sid):
        return self.json_docs.get(sid)

    def model_exists(self, ref):
        return ref in self.models


CORPUS = ("Django 4.0 supports Python 3.8, 3.9, and 3.10. "
          "Values in the CSRF_TRUSTED_ORIGINS setting must include the scheme (e.g. 'http://' or 'https://') "
          "instead of only the hostname.")


def base_model() -> dict:
    ev = {"source_id": "dj_notes@4.0", "source_type": "official_release_notes",
          "quote_or_summary": "Values in the CSRF_TRUSTED_ORIGINS setting must include the scheme",
          "quote": "Values in the CSRF_TRUSTED_ORIGINS setting must include the scheme",
          "relevance": "states the change", "verified": True, "json_path": None, "expected": None}
    cond_v = {"condition_id": "v_1", "statement": "Upgrade crosses 4.0", "category": "version", "required": True,
              "operator": "in_range", "expected_value": {"current_version": "< 4.0", "target_version": ">= 4.0"},
              "evidence": [copy.deepcopy(ev)], "confidence": "high", "ambiguities": [], "role": "required",
              "derived_by": "extraction", "search_queries": [], "judge": None}
    cond_a = {**copy.deepcopy(cond_v), "condition_id": "a_1", "statement": "App sets CSRF_TRUSTED_ORIGINS without scheme",
              "category": "configuration", "operator": "present", "expected_value": "CSRF_TRUSTED_ORIGINS",
              "search_queries": [{"tool": "ripgrep", "query": "CSRF_TRUSTED_ORIGINS"}]}
    src = {"source_id": "dj_notes@4.0", "title": "Django 4.0 release notes", "url": "https://docs.djangoproject.com/en/4.2/releases/4.0/",
           "source_type": "official_release_notes", "retrieved_at": "2026-10-20T00:00:00Z", "why_relevant": "notes",
           "authority_tier": 1, "content_hash": "sha256:x", "pinned_ref": "stable/4.2.x", "status": "used",
           "rejection_reason": None, "release": "4.0", "raw_url": "", "registry_source": "dj_notes"}
    path = {"path_id": "django_abc", "path_name": "CSRF_TRUSTED_ORIGINS scheme", "risk_type": "configuration_change",
            "risk_level": "high", "affected_surface": "configuration", "description": "d",
            "conditions": [cond_v, cond_a], "suggested_actions": ["Add schemes"], "confidence": "high",
            "applies_to": None, "fires_at": "upgrade", "introduced_in": "4.0", "primary_symbol": "CSRF_TRUSTED_ORIGINS",
            "symbols": [], "superseded_by": None, "reverted_in": None, "merged_from": [], "source_item_ids": [],
            "review_status": "unreviewed", "review_flags": []}
    return {"project": "Django", "current_version": "3.2", "target_version": "4.2", "upgrade": "3.2_to_4.2",
            "disclaimer": config.DISCLAIMER, "summary": "s", "source_inventory": [src], "risk_paths": [path],
            "open_questions": [], "overall_confidence": "high",
            "evidence_summary": {"high_confidence_risks": [], "medium_confidence_risks": [],
                                 "low_confidence_or_disputed_risks": [], "sources_with_disagreements": [],
                                 "open_questions": []},
            "context_facts": [], "disqualified_candidates": [], "requires_upgrades": [], "plan": {}, "pipeline": {}}


@pytest.fixture
def model():
    return base_model()


@pytest.fixture
def ctx():
    return FakeCtx({"dj_notes@4.0": CORPUS, "dj_tier2": CORPUS})


__all__ = ["cached", "blocks_of", "doc_text", "FakeCtx", "base_model", "CORPUS"]
