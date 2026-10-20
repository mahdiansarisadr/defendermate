from __future__ import annotations

import json

from urx import experiment


def _write(root, name, cost, recall, est_p):
    run = {"name": name, "label": name, "models": {}, "evaluator": experiment.EVALUATOR, "upgrades": ["x_1_to_2"],
           "runs": {"x_1_to_2": {"paths": 10, "usd_to_produce": cost, "input_tokens": 1, "output_tokens": 1}}}
    per = {"x_1_to_2": {"recall": recall, "estimated_precision": est_p, "strict_precision": [5, 10],
                        "classification": [9, 10], "level_agreement": [8, 8], "field_consistency": [10, 10],
                        "grounding": [20, 20], "validator_errors": 0, "structural": [10, 10], "gold_items": []}}
    (root / name / "eval").mkdir(parents=True)
    (root / name / "run.json").write_text(json.dumps(run))
    (root / name / "eval" / "results.json").write_text(json.dumps({"per_upgrade": per, "extra": {}}))


def test_compare_pareto_and_multiples(tmp_path, monkeypatch):
    monkeypatch.setattr(experiment, "EXP_DIR", tmp_path)
    _write(tmp_path, "haiku_haiku", 0.5, [8, 10], [9, 10])
    _write(tmp_path, "haiku_sonnet", 2.0, [9, 10], [9, 10])
    _write(tmp_path, "sonnet_opus", 8.0, [9, 10], [8, 10])  # costlier and worse than haiku_sonnet
    rows = {r["name"]: r for r in experiment.compare(write=False)["rows"]}
    assert rows["haiku_haiku"]["pareto"] and rows["haiku_sonnet"]["pareto"]
    assert not rows["sonnet_opus"]["pareto"]
    assert rows["sonnet_opus"]["cost_multiple"] == 16.0
    assert abs(rows["haiku_sonnet"]["f1"] - 0.9) < 1e-9
    assert rows["haiku_haiku"]["usd_per_gold_risk_found"] == 0.0625
