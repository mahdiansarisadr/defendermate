"""Model-configuration experiments: rerun upgrades under a cheap/strong model pair, score them with a fixed
evaluator, and compare quality against cost. Each config writes to experiments/<name>/."""

from __future__ import annotations

import json
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Any

from . import config
from .llm import LLMClient
from .models import RiskModel

EXP_DIR = config.ROOT / "experiments"
HAIKU, SONNET, OPUS = "claude-haiku-5-5", "claude-sonnet-5-5", "claude-opus-5-5"
CONFIGS: dict[str, dict[str, str]] = {
    "haiku_haiku": {"label": "Haiku / Haiku", "cheap": HAIKU, "strong": HAIKU},
    "haiku_sonnet": {"label": "Haiku / Sonnet", "cheap": HAIKU, "strong": SONNET},
    "sonnet_opus": {"label": "Sonnet / Opus", "cheap": SONNET, "strong": OPUS},
}
# One yardstick for every config: the precision judge never changes with the model under test.
EVALUATOR = {"cheap": SONNET, "strong": SONNET}
SUBSET = [("React", "17", "18"), ("PostgreSQL", "13", "16"), ("Next.js", "12", "14")]


def _tiers(name: str) -> dict[str, str]:
    c = CONFIGS[name]
    return {"cheap": c["cheap"], "strong": c["strong"]}


@contextmanager
def _scoped(name: str):
    old = config.OUTPUTS_DIR, config.EVAL_DIR, dict(config.MODELS[config.PROVIDER])
    try:
        config.OUTPUTS_DIR = EXP_DIR / name / "outputs"
        config.EVAL_DIR = EXP_DIR / name / "eval"
        config.MODELS[config.PROVIDER] = _tiers(name)
        yield
    finally:
        config.OUTPUTS_DIR, config.EVAL_DIR = old[0], old[1]
        config.MODELS[config.PROVIDER] = old[2]


def _main_models(upgrades) -> dict[str, RiskModel]:
    out = {}
    for u in upgrades:
        f = config.ROOT / "outputs" / config.upgrade_slug(*u) / "risk_model.json"
        if f.exists():
            out[config.upgrade_slug(*u)] = RiskModel.model_validate(json.loads(f.read_text()))
    return out


def _reusable_stability(name: str) -> dict | None:
    """The main eval already ran the cold React rerun; reuse it when it was made with the same models."""
    res, react = config.ROOT / "eval" / "results.json", config.ROOT / "outputs" / "react_17_to_18" / "risk_model.json"
    if not (res.exists() and react.exists()):
        return None
    stab = json.loads(res.read_text()).get("extra", {}).get("stability")
    if stab and json.loads(react.read_text())["pipeline"].get("models") == _tiers(name):
        return {**stab, "reused_from": "eval/results.json (same models)"}
    return None


def run_experiment(name: str, upgrades=SUBSET, stability: bool = True, log=print) -> dict:
    from .evaluate import run_eval
    from .pipeline import run_upgrade

    models = _tiers(name)
    known = {config.upgrade_slug(*u) for u in config.DEFAULT_UPGRADES}
    runs: dict[str, Any] = {}
    calib = _main_models(upgrades)
    with _scoped(name):
        for u in upgrades:
            slug = config.upgrade_slug(*u)
            t0 = time.time()
            m = run_upgrade(*u, client=LLMClient(models=models), known_models=known)
            usage = m.pipeline.get("usage", {})
            calls = sum(s["calls"] for s in usage.values())
            hits = sum(s["cache_hits"] for s in usage.values())
            runs[slug] = {
                "paths": len(m.risk_paths), "validation": m.pipeline.get("validation"),
                "usd_to_produce": round(sum(s.get("usd_full", 0) for s in usage.values()), 4),
                "usd_this_run": round(sum(s.get("usd_estimate", 0) for s in usage.values()), 4),
                "input_tokens": sum(s["input_tokens"] for s in usage.values()),
                "output_tokens": sum(s["output_tokens"] for s in usage.values()),
                "llm_calls": calls, "cache_hits": hits, "wall_s": round(time.time() - t0, 1),
                "by_stage": {k: {kk: v[kk] for kk in ("model", "calls", "input_tokens", "output_tokens", "usd_full")
                                 if kk in v} for k, v in usage.items()},
            }
            log(f"[{name}] {slug}: {runs[slug]['paths']} paths, ${runs[slug]['usd_to_produce']:.2f}, "
                f"{hits}/{calls} cached, {runs[slug]['wall_s']}s")
        res = run_eval(use_llm=True, evaluator_models=EVALUATOR, calibration_models=calib, stability_run=stability,
                       stability_cache=EXP_DIR / name / "cold_llm_cache",
                       previous_stability=_reusable_stability(name) if stability else None)
    summary = {"name": name, "label": CONFIGS[name]["label"], "models": models, "evaluator": EVALUATOR,
               "upgrades": [config.upgrade_slug(*u) for u in upgrades], "runs": runs}
    (EXP_DIR / name / "run.json").write_text(json.dumps(summary, indent=1))
    log(f"[{name}] eval: " + ", ".join(f"{m['name']}={m['display']}" for m in res["metrics"][:6]))
    return summary


# ---------------- comparison ----------------

def _ratio(rows: list[list[int]]) -> float | None:
    a, b = sum(r[0] for r in rows), sum(r[1] for r in rows)
    return a / b if b else None


def _row(name: str) -> dict | None:
    run_f, res_f = EXP_DIR / name / "run.json", EXP_DIR / name / "eval" / "results.json"
    if not (run_f.exists() and res_f.exists()):
        return None
    run, res = json.loads(run_f.read_text()), json.loads(res_f.read_text())
    per = res["per_upgrade"]
    rows = list(per.values())
    gold = [r for r in rows if "recall" in r]
    recall, est_p = _ratio([r["recall"] for r in gold]), _ratio([r["estimated_precision"] for r in rows
                                                                    if "estimated_precision" in r])
    f1 = 2 * recall * est_p / (recall + est_p) if recall and est_p else None
    cost = sum(r["usd_to_produce"] for r in run["runs"].values())
    found = sum(r["recall"][0] for r in gold)
    j = res["extra"].get("judge_calibration", {})
    st = res["extra"].get("stability", {})
    return {
        "name": name, "label": run["label"], "models": run["models"], "evaluator": run["evaluator"],
        "upgrades": run["upgrades"],
        "cost_usd": round(cost, 3), "input_tokens": sum(r["input_tokens"] for r in run["runs"].values()),
        "output_tokens": sum(r["output_tokens"] for r in run["runs"].values()),
        "paths": sum(r["paths"] for r in run["runs"].values()),
        "recall": recall, "recall_hits": [found, sum(r["recall"][1] for r in gold)],
        "estimated_precision": est_p, "strict_precision": _ratio([r["strict_precision"] for r in gold]),
        "f1": f1, "classification": _ratio([r["classification"] for r in gold]),
        "level_agreement": _ratio([r["level_agreement"] for r in gold]),
        "field_consistency": _ratio([r["field_consistency"] for r in rows]),
        "grounding": _ratio([r["grounding"] for r in rows]),
        "validator_errors": sum(r["validator_errors"] for r in rows),
        "judge_accuracy": j.get("accuracy"), "judge_kappa": j.get("kappa"),
        "stability": st.get("jaccard"), "stability_reused": bool(st.get("reused_from")),
        "usd_per_gold_risk_found": round(cost / found, 4) if found else None,
        "per_upgrade": {
            slug: {"paths": run["runs"][slug]["paths"], "cost_usd": run["runs"][slug]["usd_to_produce"],
                   "recall": per[slug].get("recall"), "estimated_precision": per[slug].get("estimated_precision"),
                   "strict_precision": per[slug].get("strict_precision"),
                   "missed": [g["gold_id"] for g in per[slug].get("gold_items", [])
                              if g["kind"] == "risk" and not g["hits"]["risk"]]}
            for slug in run["upgrades"] if slug in per},
    }


def compare(write: bool = True) -> dict:
    rows = [r for n in CONFIGS if (r := _row(n))]
    rows.sort(key=lambda r: r["cost_usd"])
    for r in rows:
        r["pareto"] = not any(o is not r and o["cost_usd"] <= r["cost_usd"] and (o["f1"] or 0) >= (r["f1"] or 0)
                              and (o["cost_usd"] < r["cost_usd"] or (o["f1"] or 0) > (r["f1"] or 0)) for o in rows)
    base = rows[0] if rows else None
    for r in rows:
        r["cost_multiple"] = round(r["cost_usd"] / base["cost_usd"], 1) if base and base["cost_usd"] else None
        r["delta_f1_vs_cheapest"] = (r["f1"] - base["f1"]) if base and r["f1"] is not None and base["f1"] else None
    out = {"rows": rows, "quality_score": "F1 of gold recall and estimated precision (fixed Sonnet 5.5 precision judge)",
           "subset": rows[0]["upgrades"] if rows else []}
    if write and rows:
        EXP_DIR.mkdir(exist_ok=True)
        (EXP_DIR / "comparison.json").write_text(json.dumps(out, indent=1))
        (EXP_DIR / "comparison.md").write_text(render(out))
    return out


def _f(x, pct=False):
    if x is None:
        return "–"
    return f"{100 * x:.1f}%" if pct else (f"{x:.3f}" if isinstance(x, float) else str(x))


def render(out: dict) -> str:
    rows = out["rows"]
    L = ["# Model configuration experiment", "",
         f"Upgrades: {', '.join(out['subset'])}. Each config runs the full pipeline with its own cheap tier "
         "(triage) and strong tier (extraction, recall sweep, revert reconcile, grounding judge). "
         "Every config is scored with the same gold sets and the same Sonnet 5.5 precision judge; "
         "judge calibration uses the same claim set for every config.", "",
         "| Config (cheap / strong) | Cost to produce | × cheapest | Paths | Gold recall | Est. precision | F1 | "
         "Strict precision | Classification | Level agreement | Judge acc. / κ | Stability | $ per gold risk found | Pareto |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        L.append(f"| {r['label']} | ${r['cost_usd']:.2f} | {r['cost_multiple']}× | {r['paths']} | "
                 f"{r['recall_hits'][0]}/{r['recall_hits'][1]} ({_f(r['recall'], True)}) | {_f(r['estimated_precision'], True)} | "
                 f"{_f(r['f1'])} | {_f(r['strict_precision'], True)} | {_f(r['classification'], True)} | "
                 f"{_f(r['level_agreement'], True)} | {_f(r['judge_accuracy'])} / {_f(r['judge_kappa'])} | "
                 f"{_f(r['stability'])}{' (reused)' if r['stability_reused'] else ''} | "
                 f"${r['usd_per_gold_risk_found']:.3f} | {'yes' if r['pareto'] else 'no'} |")
    L += ["", "Hard gates (grounding, validator errors) for every config: "
          + "; ".join(f"{r['label']}: grounding {_f(r['grounding'], True)}, {r['validator_errors']} errors" for r in rows),
          "", "## Per upgrade", "", "| Upgrade | " + " | ".join(r["label"] for r in rows) + " |",
          "|---|" + "---|" * len(rows)]
    for slug in out["subset"]:
        cells = []
        for r in rows:
            u = r["per_upgrade"].get(slug, {})
            rec = u.get("recall") or [0, 0]
            ep = u.get("estimated_precision") or [0, 0]
            cells.append(f"{u.get('paths', '–')} paths, recall {rec[0]}/{rec[1]}, est. prec. {ep[0]}/{ep[1]}, ${u.get('cost_usd', 0):.2f}"
                         + (f"; missed {', '.join(u['missed'])}" if u.get("missed") else ""))
        L.append(f"| {slug} | " + " | ".join(cells) + " |")
    L += ["", "Pareto = no other config is at least as cheap and at least as good on F1 (and strictly better on one).",
          "Costs are list-price estimates from recorded token counts (prompt-caching discounts not modeled).", ""]
    return "\n".join(L)
