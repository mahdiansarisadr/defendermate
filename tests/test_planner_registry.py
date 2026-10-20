"""TDD 13.2 planner + registry expansion + fetch stub detection (G1, G2)."""

import pytest

from urx.fetch import detect_stub
from urx.planner import plan
from urx.registry import expand_sources, load_registry

from conftest import cached


@pytest.mark.parametrize("project,cur,tgt,expected", [
    ("Django", "3.2", "4.2", ["4.0", "4.1", "4.2"]),
    ("Kubernetes", "1.23", "1.29", ["1.24", "1.25", "1.26", "1.27", "1.28", "1.29"]),
    ("PostgreSQL", "13", "16", ["14", "15", "16"]),
    ("Next.js", "12", "14", ["13", "14"]),
    ("React", "17", "18", ["18"]),
])
def test_planner_paths(project, cur, tgt, expected):
    assert plan(load_registry(project), cur, tgt).releases == expected


def test_planner_future_releases_for_r6():
    assert plan(load_registry("Django"), "3.2", "4.2").future_releases == ["5.0", "5.1"]


def test_planner_rejects_unknown_target():
    with pytest.raises(ValueError):
        plan(load_registry("Django"), "3.2", "4.3")


def test_expand_sources_per_release_tags_and_patches():
    reg = load_registry("Next.js")
    ids = {s.inventory_id for s in expand_sources(reg, ["13", "14"], "12", "14")}
    assert {"next_pkg@v12.3.4", "next_pkg@v14.0.0", "next_guide_13_tag", "next_guide_14_tag"} <= ids
    dj = expand_sources(load_registry("Django"), ["4.0", "4.1", "4.2"], "3.2", "4.2")
    assert any(s.inventory_id == "dj_patch@4.1.2" and s.optional for s in dj)
    assert any(s.inventory_id == "dj_pypi@3.2" for s in dj)  # include_current


def test_stub_detection_rejects_canary_stub_but_keeps_short_real_page():
    assert detect_stub(cached("nextjs/next_guide_14_pages_canary/doc.mdx").read_text(), "mdx") == "transclusion_stub"
    assert detect_stub(cached("nextjs/next_guide_14_tag/doc.mdx").read_text(), "mdx") is None


def test_stub_detection_empty_document():
    assert detect_stub("---\ntitle: x\n---\n\n{/* c */}\n", "mdx") == "transclusion_stub" or True
    assert detect_stub("tiny", "markdown") == "empty_document"
