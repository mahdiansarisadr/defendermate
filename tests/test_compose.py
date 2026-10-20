"""TDD 13.3 composition rules on synthetic fixtures (R1-R7) and duplicate merging."""

from pydantic import BaseModel

from urx import compose
from urx.link import merge_duplicates, symbols_equal
from urx.models import AppliesTo, ChangeItem, Condition, Evidence, RiskPath, SourceRecord, VersionFact
from urx.planner import plan
from urx.registry import load_registry


def ev(sid="s@1", q="quote text here"):
    return Evidence(source_id=sid, source_type="official_release_notes", quote_or_summary=q, quote=q, relevance="r",
                    verified=True)


def path(pid, release, primary, risk_type="removed_api", actions=None, name=None, applies=None):
    v = Condition(condition_id=f"v_{pid}", statement="crosses", category="version", required=True,
                  operator="in_range", expected_value={"current_version": f"< {release}", "target_version": f">= {release}"},
                  evidence=[ev()], confidence="low")
    a = Condition(condition_id=f"a_{pid}", statement=f"uses {primary}", category="api_usage", required=True,
                  operator="present", expected_value=primary, evidence=[ev(q=f"about {primary}")], confidence="low")
    return RiskPath(path_id=pid, path_name=name or f"{primary} risk", risk_type=risk_type, risk_level="high",
                    affected_surface="application_code", description="d", conditions=[v, a],
                    suggested_actions=actions or [], introduced_in=release, primary_symbol=primary,
                    applies_to=applies)


def item(text, release, heading, sid="k8s_deprecation_guide", section="removed"):
    return ChangeItem(item_id=str(abs(hash(text)))[:12], project="Kubernetes", release=release, source_id=sid,
                      registry_source=sid, heading_path=heading, section_type=section, text=text, raw_span=(1, 1),
                      symbols=[])


INV = {s: SourceRecord(source_id=s, title=s, url="u", source_type="official_deprecation_notice", retrieved_at="",
                       why_relevant="", authority_tier=1) for s in ("k8s_deprecation_guide", "dj_patch@4.1.2", "s@1")}


class _Link(BaseModel):
    path_id: str | None
    quote: str
    explanation: str


class FakeLLM:
    def __init__(self, answer):
        self.answer = answer

    def complete(self, prompt_id, variables, schema, **kw):
        return schema.model_validate(self.answer(variables))


def test_revert_moves_path_to_disqualified():
    p = path("dj_cache", "4.1", "related managers cache", risk_type="changed_behavior")
    it = ChangeItem(item_id="r1", project="Django", release="4.1", source_id="dj_patch@4.1.2", registry_source="dj_patch",
                    heading_path=["Bugfixes"], section_type="other", text="Reverted caching related managers for ForeignKey.",
                    raw_span=(1, 1), symbols=[], revert_candidate=True)
    llm = FakeLLM(lambda v: {"path_id": "dj_cache", "quote": "Reverted caching related managers", "explanation": "full revert"})
    kept, disq, unresolved, _ = compose.r1_reverts(llm, [p], [it], "4.2", {"dj_patch@4.1.2": it.text}, INV, {})
    assert kept == [] and disq[0].candidate_id == "dj_cache" and not unresolved


def test_revert_with_unverifiable_quote_stays_unresolved():
    p = path("dj_cache", "4.1", "related managers cache")
    it = ChangeItem(item_id="r1", project="Django", release="4.1", source_id="dj_patch@4.1.2", registry_source="dj_patch",
                    heading_path=[], section_type="other", text="Reverted caching related managers.", raw_span=(1, 1),
                    symbols=[], revert_candidate=True)
    llm = FakeLLM(lambda v: {"path_id": "dj_cache", "quote": "made up words", "explanation": "x"})
    kept, disq, unresolved, _ = compose.r1_reverts(llm, [p], [it], "4.2", {"dj_patch@4.1.2": it.text}, INV, {})
    assert kept and not disq and unresolved


def test_supersession_keeps_latest_with_history():
    a = path("p40", "4.0", "Expression.get_group_by_cols", risk_type="changed_behavior")
    b = path("p42", "4.2", "Expression.get_group_by_cols", risk_type="changed_behavior")
    kept, log = compose.r2_supersession([a, b])
    assert [p.path_id for p in kept] == ["p42"]
    assert any("History" in x for x in kept[0].conditions[0].ambiguities) and a.superseded_by == "p42"


def test_remediation_chain_flowschema_targets_v1beta3_or_v1():
    items = [
        item("The flowcontrol.apiserver.k8s.io/v1beta2 API version of FlowSchema and PriorityLevelConfiguration is no longer served as of v1.29.", "1.29", ["v1.29", "Flow control resources"]),
        item("Migrate manifests and API clients to use the flowcontrol.apiserver.k8s.io/v1 API version, available since v1.29.", "1.29", ["v1.29", "Flow control resources"]),
        item("The flowcontrol.apiserver.k8s.io/v1beta3 API version of FlowSchema and PriorityLevelConfiguration is no longer served as of v1.32.", "1.32", ["v1.32", "Flow control resources"]),
        item("Migrate manifests and API clients to use the flowcontrol.apiserver.k8s.io/v1 API version, available since v1.29.", "1.32", ["v1.32", "Flow control resources"]),
    ]
    rmap = compose.removal_map(items)
    p = path("fs", "1.26", "flowcontrol.apiserver.k8s.io/v1beta1",
             actions=["Migrate manifests to use the flowcontrol.apiserver.k8s.io/v1beta2 API version."])
    compose.r3_remediation([p], rmap, "1.29", INV)
    assert "remediation_rewritten" in p.review_flags
    assert any("flowcontrol.apiserver.k8s.io/v1" in a and "v1beta2" not in a.split("Migrate directly")[-1]
               for a in p.suggested_actions)


def test_deprecated_not_removed_becomes_future_context():
    it = item("``django.utils.baseconv`` module will be removed.", "5.0", ["5.0"], sid="s@1", section="other")
    facts = compose.r6_future_context([it], INV, "4.2")
    assert facts and facts[0].fires_at == "future_removal"


def test_start_applicability_drops_risk():
    p = path("x", "4.0", "sym", applies=AppliesTo(from_versions="<3.1"))
    kept, dropped = compose.r5_start_applicability([p], "3.2")
    assert not kept and dropped


def test_cross_project_requires_react_upgrade():
    reg = load_registry("Next.js")
    pl = plan(reg, "12", "14")
    facts = [VersionFact(release="12", field="react_peer", value="^17.0.2 || ^18.0.0-0", source_id="next_pkg@v12.3.4", json_path="peerDependencies.react"),
             VersionFact(release="14", field="react_peer", value="^18.2.0", source_id="next_pkg@v14.0.0", json_path="peerDependencies.react")]
    paths, reqs = compose.fact_paths(reg, facts, pl, "nextjs", {})
    assert reqs and reqs[0].project == "React" and reqs[0].model_ref == "react_17_to_18"
    assert paths[0].conditions[0].evidence[0].json_path == "peerDependencies.react"


def test_merge_duplicates_merges_same_symbol_not_short_dotted():
    a = path("a", "4.0", "django.utils.encoding.force_text")
    b = path("b", "4.0", "force_text")
    c = path("c", "18", "ReactDOM.render")
    d = path("d", "18", "root.render")
    merged, log = merge_duplicates([a, b, c, d])
    assert len(merged) == 3 and log[0]["merged"] in ("a", "b")
    assert symbols_equal("Strict Mode", "StrictMode")
    assert not symbols_equal("ReactDOM.render", "render")
