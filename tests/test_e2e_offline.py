"""Offline replay: the committed outputs are reproducible from the source + LLM caches alone."""

from __future__ import annotations

import json

import pytest

from urx import config, pipeline
from urx.llm import LLMClient

UPGRADES = [u for u in config.DEFAULT_UPGRADES
            if (config.OUTPUTS_DIR / config.upgrade_slug(*u) / "risk_model.json").exists()]


@pytest.fixture
def tmp_outputs(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "OUTPUTS_DIR", tmp_path)
    return tmp_path


@pytest.mark.parametrize("upgrade", UPGRADES, ids=[config.upgrade_slug(*u) for u in UPGRADES])
def test_offline_replay_matches_committed(upgrade, tmp_outputs):
    slug = config.upgrade_slug(*upgrade)
    committed = json.loads((config.ROOT / "outputs" / slug / "risk_model.json").read_text())
    m = pipeline.run_upgrade(*upgrade, offline=True, client=LLMClient(offline=True),
                             known_models={config.upgrade_slug(*u) for u in config.DEFAULT_UPGRADES})
    assert m.pipeline["validation"]["errors"] == 0
    assert m.disclaimer == config.DISCLAIMER
    assert {p.path_id for p in m.risk_paths} == {p["path_id"] for p in committed["risk_paths"]}
    for name in ("risk_model.json", "source_inventory.json", "report.md", "graph.mmd", "run_log.jsonl",
                 "intermediate/items.jsonl", "intermediate/triage.jsonl", "intermediate/extractions.jsonl",
                 "intermediate/validation.json"):
        assert (tmp_outputs / slug / name).exists(), name
