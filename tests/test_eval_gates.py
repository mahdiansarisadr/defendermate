"""Hard eval gates from TDD 17.4, computed deterministically on the committed outputs."""

from __future__ import annotations

import pytest

from urx.evaluate import TARGETS, compute_deterministic, drift_test, load_models

MODELS = load_models()
pytestmark = pytest.mark.skipif(not MODELS, reason="no committed outputs")


@pytest.fixture(scope="module")
def per():
    return compute_deterministic(MODELS)


def _rate(rows, key):
    a, b = sum(r[key][0] for r in rows), sum(r[key][1] for r in rows)
    return a / b if b else 1.0


def test_grounding_rate(per):
    assert _rate(per.values(), "grounding") >= TARGETS["grounding_rate"]


def test_no_validator_errors(per):
    assert {s: r["validator_errors"] for s, r in per.items()} == {s: 0 for s in per}


def test_structural_completeness(per):
    assert _rate(per.values(), "structural") >= TARGETS["structural_completeness"]


def test_recall_per_upgrade(per):
    for slug, r in per.items():
        if "recall" in r:
            assert r["recall"][0] / r["recall"][1] >= TARGETS["recall_per_upgrade"], slug


def test_recall_overall(per):
    rows = [r for r in per.values() if "recall" in r]
    assert _rate(rows, "recall") >= TARGETS["recall_overall"]


def test_classification_accuracy(per):
    rows = [r for r in per.values() if "classification" in r]
    assert _rate(rows, "classification") >= TARGETS["classification_accuracy"]


def test_field_consistency(per):
    assert _rate(per.values(), "field_consistency") >= TARGETS["field_consistency"]


def test_drift_exact_never_accepts():
    d = drift_test(MODELS)
    assert d["n"] > 0
    assert d["exact_false_accept"] == 0
