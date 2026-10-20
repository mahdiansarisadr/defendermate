"""TDD 13.4 deterministic confidence rubric."""

from urx.models import Condition, Evidence, JudgeResult
from urx.rubric import condition_confidence, overall_confidence


def cond(sources, **kw):
    ev = [Evidence(source_id=s, source_type="official_release_notes", quote_or_summary="q", quote="q",
                   relevance="r", json_path=jp, expected="x" if jp else None, verified=True) for s, jp in sources]
    base = dict(condition_id="c", statement="s", category="api_usage", required=True, operator="present",
                expected_value="x", evidence=ev, confidence="low")
    base.update(kw)
    return Condition(**base)


TIERS = {"a@1": 1, "b@1": 1, "t2": 2, "t3": 3}


def test_tier2_only_never_high():
    c = cond([("t2", None)])
    assert condition_confidence(c, TIERS)[0] != "high"
    c2 = cond([("t2", None), ("t3", None)])
    assert condition_confidence(c2, TIERS)[0] != "high"


def test_inference_never_high():
    assert condition_confidence(cond([("a@1", None), ("b@1", "x.y")], derived_by="inference"), TIERS)[0] != "high"


def test_uncertain_always_low():
    assert condition_confidence(cond([("a@1", None), ("b@1", "x.y")], role="uncertain", required=False), TIERS)[0] == "low"


def test_judge_not_supported_low():
    c = cond([("a@1", None)], judge=JudgeResult(verdict="not_supported"))
    assert condition_confidence(c, TIERS)[0] == "low"


def test_two_tier1_sources_plus_json_path_high():
    assert condition_confidence(cond([("a@1", None), ("b@1", "engines.node")]), TIERS)[0] == "high"


def test_partial_judge_and_ambiguity_lower_to_medium():
    c = cond([("a@1", None)], ambiguities=["x"], judge=JudgeResult(verdict="partially_supported"))
    assert condition_confidence(c, TIERS)[0] == "medium"


def test_overall_confidence_bands():
    class P:
        def __init__(self, c):
            self.confidence = c
    assert overall_confidence([P("high")] * 8 + [P("medium")] * 2, 0, 0) == "high"
    assert overall_confidence([P("high")] * 8 + [P("medium")] * 2, 1, 0) == "medium"
    assert overall_confidence([P("low")] * 5 + [P("medium")] * 5, 0, 0) == "low"
