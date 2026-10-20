"""TDD 13.5: every validator rule has a negative test with a specific error code (L17)."""

import copy

from urx.validate import validate_model

from conftest import FakeCtx, CORPUS


def codes(model, ctx, **kw):
    return {i.code for i in validate_model(model, ctx, **kw) if i.level == "error"}


def test_clean_model_passes(model, ctx):
    assert codes(model, ctx) == set()


def test_drifted_quote_rejected(model, ctx):
    ev = model["risk_paths"][0]["conditions"][0]["evidence"][0]
    ev["quote"] = ev["quote_or_summary"] = "Django 4.0 supports Python 3.9, 3.10, and 3.11."  # 3.8 dropped
    assert "E3_quote_not_found" in codes(model, ctx)


def test_plausible_invented_quote_rejected(model, ctx):
    ev = model["risk_paths"][0]["conditions"][1]["evidence"][0]
    ev["quote"] = ev["quote_or_summary"] = "CSRF_TRUSTED_ORIGINS now requires a scheme for every origin."
    assert "E3_quote_not_found" in codes(model, ctx)


def test_tier2_only_condition_marked_high(model, ctx):
    model["source_inventory"].append({**model["source_inventory"][0], "source_id": "dj_tier2", "authority_tier": 2,
                                      "source_type": "community_writeup"})
    c = model["risk_paths"][0]["conditions"][1]
    for e in c["evidence"]:
        e["source_id"], e["source_type"] = "dj_tier2", "community_writeup"
    c["confidence"] = "high"
    assert "E7_high_without_tier1" in codes(model, ctx)


def test_path_without_version_condition(model, ctx):
    model["risk_paths"][0]["conditions"] = model["risk_paths"][0]["conditions"][1:]
    assert "E5_structure" in codes(model, ctx)


def test_path_without_app_condition(model, ctx):
    model["risk_paths"][0]["conditions"] = model["risk_paths"][0]["conditions"][:1]
    assert "E5_structure" in codes(model, ctx)


def test_json_path_mismatch_next14_node():
    from conftest import base_model
    m = base_model()
    m["source_inventory"].append({**m["source_inventory"][0], "source_id": "next_pkg@v14.0.0",
                                  "source_type": "package_registry_metadata", "registry_source": "next_pkg"})
    m["risk_paths"][0]["conditions"][1]["evidence"] = [{
        "source_id": "next_pkg@v14.0.0", "source_type": "package_registry_metadata",
        "quote_or_summary": "engines.node = '>=16.14.0'", "relevance": "r", "quote": None, "verified": True,
        "json_path": "engines.node", "expected": ">=16.14.0"}]
    ctx = FakeCtx({"dj_notes@4.0": CORPUS}, json_docs={"next_pkg@v14.0.0": {"engines": {"node": ">=18.17.0"}}})
    assert "E4_json_path" in codes(m, ctx)


def test_dangling_requires_upgrades(model, ctx):
    model["requires_upgrades"] = [{"project": "React", "current_version": "17", "target_version": "18", "reason": "r",
                                   "evidence": [], "model_ref": "react_17_to_18"}]
    assert "E8_dangling_requires" in codes(model, ctx)
    assert "E8_dangling_requires" not in codes(model, ctx, extra_models={"react_17_to_18"})


def test_unknown_source_id(model, ctx):
    model["risk_paths"][0]["conditions"][1]["evidence"][0]["source_id"] = "made_up@1"
    assert "E2_unknown_source" in codes(model, ctx)


def test_rejected_source_used_as_evidence(model, ctx):
    model["source_inventory"][0]["status"] = "rejected"
    assert "E2_unknown_source" in codes(model, ctx)


def test_invalid_enum_removed_configuration(model, ctx):
    model["risk_paths"][0]["conditions"][1]["category"] = "removed_configuration"
    assert "E1_schema" in codes(model, ctx)


def test_condition_without_evidence_or_ambiguity(model, ctx):
    model["risk_paths"][0]["conditions"][1]["evidence"] = []
    assert "E6_no_evidence" in codes(model, ctx)
    c = model["risk_paths"][0]["conditions"][1]
    c.update(role="uncertain", required=False, ambiguities=["not stated"], confidence="low")
    assert "E6_no_evidence" not in codes(model, ctx)


def test_duplicate_ids(model, ctx):
    model["risk_paths"].append(copy.deepcopy(model["risk_paths"][0]))
    assert "E9_duplicate_id" in codes(model, ctx)


def test_role_required_mismatch(model, ctx):
    model["risk_paths"][0]["conditions"][1]["role"] = "alternative"
    assert "E11_role_mismatch" in codes(model, ctx)


def test_context_fact_with_unverifiable_evidence(model, ctx):
    model["context_facts"] = [{"fact_id": "f", "statement": "s", "introduced_in": "4.0", "why_not_risk": "w",
                               "fires_at": None, "evidence": [{**model["risk_paths"][0]["conditions"][0]["evidence"][0],
                                                               "quote": "never said", "quote_or_summary": "never said"}]}]
    assert "E3_quote_not_found" in codes(model, ctx)


def test_altered_disclaimer(model, ctx):
    model["disclaimer"] = "This is a migration plan."
    assert "E1_schema" in codes(model, ctx)
