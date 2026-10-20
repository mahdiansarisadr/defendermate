"""Evaluation (TDD 17.4): gold matching, precision/recall, grounding, calibration, judge accuracy, ablations."""

from __future__ import annotations

import difflib
import json
import random
import re
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel

from . import config
from .judge import judge_claims
from .llm import ExtractionFailed, LLMClient
from .models import APP_SIDE_CATEGORIES, LEVEL_ORDER, RiskModel, RiskPath
from .normalize import normalize
from .validate import CacheContext, validate_model, verify_quote

TARGETS = {
    "grounding_rate": 1.0, "validator_errors": 0, "structural_completeness": 1.0, "recall_per_upgrade": 0.80,
    "recall_overall": 0.85, "estimated_precision": 0.85, "classification_accuracy": 0.85, "level_agreement": 0.80,
    "field_consistency": 0.95, "judge_accuracy": 0.90, "judge_kappa": 0.80, "drift_false_accept_exact": 0.0,
    "stability_jaccard": 0.80,
}
HARD = {"grounding_rate", "validator_errors", "structural_completeness", "recall_per_upgrade", "recall_overall",
        "classification_accuracy", "field_consistency", "drift_false_accept_exact"}


# ---------------- loading and matching ----------------

def load_models() -> dict[str, RiskModel]:
    out = {}
    for p, c, t in config.DEFAULT_UPGRADES:
        slug = config.upgrade_slug(p, c, t)
        f = config.OUTPUTS_DIR / slug / "risk_model.json"
        if f.exists():
            out[slug] = RiskModel.model_validate(json.loads(f.read_text()))
    return out


def load_gold(slug: str) -> dict | None:
    f = config.GOLD_DIR / f"{slug}.yaml"
    return yaml.safe_load(f.read_text()) if f.exists() else None


def path_blob(p: RiskPath) -> str:
    parts = [p.path_name, p.description, p.primary_symbol, " ".join(p.symbols)]
    for c in p.conditions:
        parts += [c.statement, json.dumps(c.expected_value)] + [e.quote or "" for e in c.evidence]
    return normalize(" ".join(parts)).lower()


def _release_ok(gold_release: Any, release: str) -> bool:
    if gold_release in (None, "*"):
        return True
    rels = gold_release if isinstance(gold_release, list) else [gold_release]
    return release in [str(r) for r in rels] or (release == "*" and "*" in rels)


def matches(item: dict, blob: str, release: str | None) -> bool:
    if release is not None and not _release_ok(item.get("release"), release):
        return False
    return any(all(t.lower() in blob for t in group) for group in item["match"])


def bucket_hits(item: dict, model: RiskModel) -> dict[str, list[str]]:
    hits = {"risk": [], "context": [], "disqualified": []}
    for p in model.risk_paths:
        if matches(item, path_blob(p), p.introduced_in):
            hits["risk"].append(p.path_id)
    for f in model.context_facts:
        blob = normalize(" ".join([f.statement] + [e.quote or "" for e in f.evidence])).lower()
        if matches(item, blob, f.introduced_in):
            hits["context"].append(f.fact_id)
    for d in model.disqualified_candidates:
        blob = normalize(" ".join([d.statement, d.reason] + [e.quote or "" for e in d.evidence])).lower()
        if matches(item, blob, None):  # disqualified candidates carry no release field
            hits["disqualified"].append(d.candidate_id)
    return hits


# ---------------- deterministic metrics ----------------

def grounding(model: RiskModel) -> tuple[int, int, list[str]]:
    ctx = CacheContext(model.project, [s.model_dump() for s in model.source_inventory])
    total = ok = 0
    bad = []
    evs = [e for p in model.risk_paths for c in p.conditions for e in c.evidence]
    evs += [e for f in model.context_facts for e in f.evidence]
    evs += [e for d in model.disqualified_candidates for e in d.evidence]
    from .adapters import json_meta
    for e in evs:
        total += 1
        if e.json_path:
            doc = ctx.json_doc(e.source_id)
            good = doc is not None and json_meta.lookup_str(doc, e.json_path) == e.expected
        else:
            good = bool(e.quote) and verify_quote(e.quote, ctx.corpus(e.source_id))
        ok += good
        if not good:
            bad.append(f"{e.source_id}: {(e.quote or e.json_path or '')[:80]}")
    return ok, total, bad


def field_consistency(model: RiskModel) -> tuple[int, int, list[str]]:
    ok = total = 0
    bad = []
    for p in model.risk_paths:
        for c in p.conditions:
            total += 1
            v = c.expected_value
            sv = json.dumps(v) if not isinstance(v, str) else v
            good = True
            if c.category == "version":
                good = isinstance(v, dict) and ({"current_version", "target_version"} <= v.keys() or "applies_to" in v)
            elif c.operator in ("in_range", "less_than", "greater_than"):
                good = bool(re.search(r"\d", sv))
            elif c.operator in ("present", "absent", "contains", "equals", "not_equals"):
                good = bool(sv.strip())
            if good and c.category in APP_SIDE_CATEGORIES and c.operator == "present" and c.role == "required" \
                    and isinstance(v, str) and re.fullmatch(r"[\w./:@<>-]{3,}", v.strip()) and not c.search_queries:
                good = False
            ok += good
            if not good:
                bad.append(f"{p.path_id}/{c.condition_id}: {c.category} {c.operator} {sv[:60]}")
    return ok, total, bad


def drift_test(models: dict[str, RiskModel], n: int = 200, seed: int = 7) -> dict:
    """Inject a one-number drift into verified quotes (L16); exact must reject all, fuzzy(0.9) accepts many."""
    rng = random.Random(seed)
    pairs = []
    for m in models.values():
        ctx = CacheContext(m.project, [s.model_dump() for s in m.source_inventory])
        for p in m.risk_paths:
            for c in p.conditions:
                for e in c.evidence:
                    if e.quote and re.search(r"\d", e.quote):
                        pairs.append((e.quote, ctx.corpus(e.source_id)))
    rng.shuffle(pairs)
    pairs = pairs[:n]
    exact_acc = fuzzy_acc = genuine = 0
    for q, corpus in pairs:
        nums = list(re.finditer(r"\d+", q))
        mnum = rng.choice(nums)
        mutated = q[:mnum.start()] + str(int(mnum.group()) + 1) + q[mnum.end():]
        if corpus and normalize(mutated) in normalize(corpus):
            genuine += 1  # e.g. v2beta1 -> v2beta2: the mutation is itself real source text, not drift
            continue
        exact_acc += verify_quote(mutated, corpus)
        fuzzy_acc += difflib.SequenceMatcher(None, normalize(mutated), normalize(q)).ratio() >= 0.9
    k = max(len(pairs) - genuine, 1)
    return {"n": len(pairs) - genuine, "excluded_genuine": genuine,
            "exact_false_accept": exact_acc / k, "fuzzy_false_accept": fuzzy_acc / k}


# ---------------- LLM-assisted metrics ----------------

class _Precision(BaseModel):
    valid: bool
    specific: bool
    reason: str


def precision_labels(client: LLMClient, model: RiskModel, matched_ids: set[str]) -> dict[str, dict]:
    def work(p: RiskPath):
        if p.path_id in matched_ids:
            return p.path_id, {"valid": True, "specific": True, "reason": "matches a gold risk", "by": "gold"}
        slim = {"path_name": p.path_name, "risk_type": p.risk_type, "description": p.description,
                "conditions": [{"role": c.role, "statement": c.statement,
                                "quotes": [e.quote or e.quote_or_summary for e in c.evidence]} for c in p.conditions]}
        try:
            r = client.complete("precision_judge.v1", {"project": model.project, "current_version": model.current_version,
                                                       "target_version": model.target_version, "path_json": slim},
                                _Precision, model_tier="strong", max_tokens=1000, stage="eval_precision")
            return p.path_id, {**r.model_dump(), "by": "llm_judge"}
        except ExtractionFailed as e:
            return p.path_id, {"valid": False, "specific": False, "reason": f"judge failed: {e}", "by": "error"}

    with ThreadPoolExecutor(config.MAX_WORKERS) as ex:
        return dict(ex.map(work, model.risk_paths))


def judge_calibration(client: LLMClient, models: dict[str, RiskModel], n: int = 40, seed: int = 11) -> dict:
    """G19 synthetic adversarial set: identity claims (supported) vs mutated claims (not supported)."""
    rng = random.Random(seed)
    quotes = [(m.project, e.quote) for m in models.values() for p in m.risk_paths for c in p.conditions
              for e in c.evidence if e.quote and len(e.quote.split()) >= 8]
    rng.shuffle(quotes)
    cases = []
    swaps = [("removed", "added"), ("no longer", "still"), ("deprecated", "recommended"), ("now", "never"),
             ("must", "need not"), ("required", "optional"), ("default", "non-default")]
    for proj, q in quotes:
        if len(cases) >= n:
            break
        cases.append({"id": f"s{len(cases)}", "claim": f"{proj} documentation states that {q}", "quote": q, "label": 1})
        mutated = None
        nums = list(re.finditer(r"\d+(\.\d+)?", q))
        if nums:
            mm = rng.choice(nums)
            mutated = q[:mm.start()] + str(int(float(mm.group())) + 3) + q[mm.end():]
        else:
            for a, b in swaps:
                if re.search(rf"\b{a}\b", q, re.I):
                    mutated = re.sub(rf"\b{a}\b", b, q, count=1, flags=re.I)
                    break
        if mutated and mutated != q:
            cases.append({"id": f"m{len(cases)}", "claim": f"{proj} documentation states that {mutated}", "quote": q, "label": 0})
    claims = [{"condition_id": c["id"], "claim": c["claim"], "evidence": [{"quote": c["quote"], "source": "official docs"}]}
              for c in cases]
    verdicts = {}
    for i in range(0, len(claims), 10):
        verdicts.update(judge_claims(client, claims[i:i + 10], stage="eval_judge"))
    tp = tn = fp = fn = 0
    for c in cases:
        v = verdicts.get(c["id"])
        pred = 1 if v and v.verdict == "supported" else 0
        tp += pred and c["label"]
        tn += (not pred) and (not c["label"])
        fp += pred and not c["label"]
        fn += (not pred) and c["label"]
    n_all = max(tp + tn + fp + fn, 1)
    acc = (tp + tn) / n_all
    pe = ((tp + fp) * (tp + fn) + (tn + fn) * (tn + fp)) / (n_all * n_all)
    kappa = (acc - pe) / (1 - pe) if pe < 1 else 0.0
    return {"n": n_all, "accuracy": acc, "kappa": kappa, "tp": tp, "tn": tn, "fp": fp, "fn": fn}


# ---------------- ablations ----------------

class _BaseRisk(BaseModel):
    path_name: str
    risk_type: str
    risk_level: str
    introduced_in: str
    primary_symbol: str
    description: str
    quote: str


class _Baseline(BaseModel):
    risks: list[_BaseRisk]


def baseline_ablation(client: LLMClient, slug: str, model: RiskModel, gold: dict) -> dict:
    """Single unstructured prompt over the same windowed documents (no triage, no per-item extraction)."""
    items = [json.loads(l) for l in (config.OUTPUTS_DIR / slug / "intermediate" / "items.jsonl").read_text().splitlines()]
    docs = "\n".join(f"[{i['release']}] {i['text']}" for i in items)[:180_000]
    try:
        res = client.complete("baseline.v1", {"project": model.project, "current_version": model.current_version,
                                              "target_version": model.target_version, "documents": docs},
                              _Baseline, model_tier="strong", max_tokens=32000, stage="ablation_baseline")
    except ExtractionFailed as e:
        return {"error": str(e)[:300]}
    ctx = CacheContext(model.project, [s.model_dump() for s in model.source_inventory])
    corpora = [ctx.corpus(s.source_id) or "" for s in model.source_inventory if s.status == "used"]
    grounded = sum(any(normalize(r.quote) in c for c in corpora) for r in res.risks)
    gold_risks = [g for g in gold["items"] if g["kind"] == "risk"]
    blobs = [(normalize(" ".join([r.path_name, r.primary_symbol, r.description, r.quote])).lower(), r.introduced_in)
             for r in res.risks]
    # The baseline's release labels are unreliable, so both sides ignore the release filter (generous to the baseline).
    found = sum(any(matches(g, b, None) for b, _ in blobs) for g in gold_risks)
    matched_paths = sum(any(matches(g, b, None) for g in gold_risks) for b, _ in blobs)
    return {"risks": len(res.risks), "recall": found / max(len(gold_risks), 1),
            "strict_precision": matched_paths / max(len(res.risks), 1),
            "grounding_rate": grounded / max(len(res.risks), 1), "checkable_conditions": 0}


def filter_ablation(slug: str, model: RiskModel, gold: dict) -> dict:
    """Would a heading or keyword pre-filter (instead of LLM triage on all items) have lost gold risks?"""
    items = {json.loads(l)["item_id"]: json.loads(l)
             for l in (config.OUTPUTS_DIR / slug / "intermediate" / "items.jsonl").read_text().splitlines()}
    kw = re.compile(r"\b(removed?|no longer|deprecat\w*|incompatib\w*|breaking|must|requires?|default)\b", re.I)
    heading_types = {"removed", "incompatible", "deprecated", "urgent", "requirements"}
    res = {"llm_triage": 0, "heading_filter": 0, "keyword_filter": 0}
    gold_risks = [g for g in gold["items"] if g["kind"] == "risk"]
    for g in gold_risks:
        pids = bucket_hits(g, model)["risk"]
        if not pids:
            continue
        srcs = [items[i] for p in model.risk_paths if p.path_id in pids for i in p.source_item_ids if i in items]
        res["llm_triage"] += 1
        res["heading_filter"] += any(s["section_type"] in heading_types for s in srcs) or not srcs
        res["keyword_filter"] += any(kw.search(s["text"]) for s in srcs) or not srcs
    n = max(len(gold_risks), 1)
    return {k: v / n for k, v in res.items()}


def stability_rerun(client_factory, project="React", current="17", target="18") -> dict:
    """G21: cold rerun (empty LLM cache, separate outputs dir) and path-ID Jaccard."""
    from . import pipeline

    base = load_models().get(config.upgrade_slug(project, current, target))
    with tempfile.TemporaryDirectory() as tmp:
        old_out = config.OUTPUTS_DIR
        try:
            config.OUTPUTS_DIR = Path(tmp)
            client = client_factory(Path(tmp) / "llm_cache")
            m2 = pipeline.run_upgrade(project, current, target, client=client,
                                      known_models={config.upgrade_slug(*u) for u in config.DEFAULT_UPGRADES})
        finally:
            config.OUTPUTS_DIR = old_out
    a = {p.path_id for p in base.risk_paths} if base else set()
    b = {p.path_id for p in m2.risk_paths}
    gold = load_gold(config.upgrade_slug(project, current, target))
    def rec(m):
        gr = [g for g in gold["items"] if g["kind"] == "risk"]
        return sum(bool(bucket_hits(g, m)["risk"]) for g in gr) / len(gr)
    return {"jaccard": len(a & b) / max(len(a | b), 1), "paths_a": len(a), "paths_b": len(b),
            "recall_a": rec(base) if base else None, "recall_b": rec(m2)}


# ---------------- driver ----------------

def _metric(name: str, value: float | int | None, display: str, target_key: str | None = None, higher=True) -> dict:
    t = TARGETS.get(target_key or name)
    passed = None
    if t is not None and value is not None:
        passed = (value >= t) if higher else (value <= t)
    return {"name": name, "value": value, "display": display, "target": t, "pass": passed,
            "gate": "hard" if (target_key or name) in HARD else ("soft" if t is not None else "report")}


def compute_deterministic(models: dict[str, RiskModel]) -> dict:
    per = {}
    for slug, m in models.items():
        gold = load_gold(slug)
        ctx = CacheContext(m.project, [s.model_dump() for s in m.source_inventory])
        issues = validate_model(json.loads(m.model_dump_json()), ctx, extra_models=set(models))
        g_ok, g_tot, g_bad = grounding(m)
        f_ok, f_tot, f_bad = field_consistency(m)
        struct = sum(any(c.category == "version" for c in p.conditions)
                     and any(c.category in APP_SIDE_CATEGORIES for c in p.conditions) for p in m.risk_paths)
        row: dict[str, Any] = {
            "project": m.project, "paths": len(m.risk_paths), "context_facts": len(m.context_facts),
            "disqualified": len(m.disqualified_candidates), "overall_confidence": m.overall_confidence,
            "validator_errors": sum(i.level == "error" for i in issues),
            "validator_warnings": sum(i.level == "warning" for i in issues),
            "grounding": [g_ok, g_tot], "grounding_failures": g_bad[:10],
            "field_consistency": [f_ok, f_tot], "field_failures": f_bad[:10],
            "structural": [struct, len(m.risk_paths)],
            "usage": m.pipeline.get("usage", {}), "timings_s": m.pipeline.get("timings_s", {}),
            "funnel": m.pipeline.get("funnel", {}),
        }
        if gold:
            items = []
            matched_paths: set[str] = set()
            for g in gold["items"]:
                h = bucket_hits(g, m)
                found_any = any(h.values())
                best_level = None
                if h["risk"]:
                    lv = [p.risk_level for p in m.risk_paths if p.path_id in h["risk"]]
                    best_level = max(lv, key=LEVEL_ORDER.index)
                    if g["kind"] == "risk":
                        matched_paths.update(h["risk"])
                items.append({"gold_id": g["gold_id"], "kind": g["kind"], "min_level": g.get("min_level"),
                              "hits": h, "found": found_any, "correct_bucket": bool(h[g["kind"]]),
                              "extracted_level": best_level})
            risks = [i for i in items if i["kind"] == "risk"]
            found = [i for i in items if i["found"]]
            lvl = [i for i in risks if i["hits"]["risk"] and i["min_level"]]
            row.update({
                "gold_items": items,
                "recall": [sum(bool(i["hits"]["risk"]) for i in risks), len(risks)],
                "classification": [sum(i["correct_bucket"] for i in found), len(found)],
                "level_agreement": [sum(LEVEL_ORDER.index(i["extracted_level"]) >= LEVEL_ORDER.index(i["min_level"]) - 1
                                        for i in lvl), len(lvl)],
                "strict_precision": [len(matched_paths), len(m.risk_paths)],
                "matched_path_ids": sorted(matched_paths),
            })
        per[slug] = row
    return per


def run_eval(use_llm: bool = True, offline: bool = False, ablations: bool = False, stability_run: bool = False,
             stability: bool | None = None, evaluator_models: dict[str, str] | None = None,
             calibration_models: dict[str, RiskModel] | None = None, stability_cache: Path | None = None,
             previous_stability: dict | None = None) -> dict:
    """evaluator_models fixes the precision judge, and calibration_models fixes the judge-calibration claims,
    so that runs with different extraction models are scored by the same yardstick."""
    stability_run = stability_run or bool(stability)
    models = load_models()
    per = compute_deterministic(models)
    client = LLMClient(offline=offline) if use_llm else None
    evaluator = LLMClient(offline=offline, models=evaluator_models) if use_llm and evaluator_models else client
    extra: dict[str, Any] = {"drift": drift_test(models)}
    if client:
        extra["models"] = client.model_map()
        extra["evaluator_models"] = evaluator.model_map()

    if client:
        for slug, m in models.items():
            labels = precision_labels(evaluator, m, set(per[slug].get("matched_path_ids", [])))
            per[slug]["precision_labels"] = labels
            valid = sum(v["valid"] for v in labels.values())
            per[slug]["estimated_precision"] = [valid, len(labels)]
            buckets: dict[str, list[int]] = {"high": [0, 0], "medium": [0, 0], "low": [0, 0]}
            for p in m.risk_paths:
                buckets[p.confidence][0] += labels[p.path_id]["valid"]
                buckets[p.confidence][1] += 1
            per[slug]["calibration"] = buckets
            flagged = [p for p in m.risk_paths if "judge_not_supported" in p.review_flags]
            per[slug]["judge_flagged_valid"] = [sum(labels[p.path_id]["valid"] for p in flagged), len(flagged)]
        extra["judge_calibration"] = judge_calibration(client, calibration_models or models)
    if ablations:
        extra["ablations"] = {}
        for slug, m in models.items():
            gold = load_gold(slug)
            if not gold:
                continue
            ab = {"filters": filter_ablation(slug, m, gold)}
            if client:
                ab["baseline_single_prompt"] = baseline_ablation(client, slug, m, gold)
            extra["ablations"][slug] = ab
    if previous_stability:
        extra["stability"] = previous_stability
    elif stability_run and client:
        extra["stability"] = stability_rerun(lambda d: LLMClient(cache_dir=stability_cache or d))
    elif (config.EVAL_DIR / "results.json").exists():
        prev = json.loads((config.EVAL_DIR / "results.json").read_text())
        for key in ("stability", "ablations"):
            if key in prev.get("extra", {}) and key not in extra:
                extra[key] = prev["extra"][key]

    metrics = summarize_metrics(per, extra)
    res = {"per_upgrade": per, "extra": extra, "metrics": metrics}
    config.EVAL_DIR.mkdir(parents=True, exist_ok=True)
    (config.EVAL_DIR / "results.json").write_text(json.dumps(res, indent=1, default=str))
    (config.EVAL_DIR / "results.md").write_text(render_markdown(res))
    return res


def _ratio(rows: list[list[int]]) -> tuple[float | None, str]:
    a = sum(r[0] for r in rows)
    b = sum(r[1] for r in rows)
    return (a / b if b else None), f"{a}/{b}" + (f" = {a / b:.3f}" if b else "")


def summarize_metrics(per: dict, extra: dict) -> list[dict]:
    rows = list(per.values())
    out = []
    v, d = _ratio([r["grounding"] for r in rows])
    out.append(_metric("grounding_rate", v, d))
    errs = sum(r["validator_errors"] for r in rows)
    out.append(_metric("validator_errors", errs, str(errs), higher=False))
    v, d = _ratio([r["structural"] for r in rows])
    out.append(_metric("structural_completeness", v, d))
    rec_rows = [r for r in rows if "recall" in r]
    per_up = {r["project"]: r["recall"][0] / r["recall"][1] for r in rec_rows if r["recall"][1]}
    worst = min(per_up.values()) if per_up else None
    out.append(_metric("recall_per_upgrade (min)", worst,
                       ", ".join(f"{k} {v:.2f}" for k, v in per_up.items()), "recall_per_upgrade"))
    v, d = _ratio([r["recall"] for r in rec_rows])
    out.append(_metric("recall_overall", v, d))
    v, d = _ratio([r["strict_precision"] for r in rec_rows])
    out.append(_metric("strict_precision (lower bound)", v, d, "none"))
    if all("estimated_precision" in r for r in rows):
        v, d = _ratio([r["estimated_precision"] for r in rows])
        out.append(_metric("estimated_precision", v, d))
    v, d = _ratio([r["classification"] for r in rec_rows])
    out.append(_metric("classification_accuracy", v, d))
    v, d = _ratio([r["level_agreement"] for r in rec_rows])
    out.append(_metric("level_agreement", v, d))
    v, d = _ratio([r["field_consistency"] for r in rows])
    out.append(_metric("field_consistency", v, d))
    if all("calibration" in r for r in rows):
        agg = {k: [sum(r["calibration"][k][0] for r in rows), sum(r["calibration"][k][1] for r in rows)]
               for k in ("high", "medium", "low")}
        rate = {k: (a / b if b else None) for k, (a, b) in agg.items()}
        present = [rate[k] for k in ("high", "medium", "low") if rate[k] is not None]
        mono = all(x >= y - 1e-9 for x, y in zip(present, present[1:]))
        out.append({"name": "calibration (valid-rate high ≥ medium ≥ low)", "value": rate,
                    "display": ", ".join(f"{k} {a}/{b}" for k, (a, b) in agg.items()), "target": "monotone",
                    "pass": mono, "gate": "soft"})
    if "judge_calibration" in extra:
        j = extra["judge_calibration"]
        out.append(_metric("judge_accuracy", j["accuracy"], f"{j['accuracy']:.3f} on {j['n']} synthetic pairs"))
        out.append(_metric("judge_kappa", j["kappa"], f"{j['kappa']:.3f}"))
    dr = extra["drift"]
    out.append(_metric("drift_false_accept_exact", dr["exact_false_accept"],
                       f"exact {dr['exact_false_accept']:.3f} vs fuzzy(0.9) {dr['fuzzy_false_accept']:.3f} on {dr['n']} drifted quotes"
                       f" ({dr.get('excluded_genuine', 0)} mutations excluded because they are real source text)",
                       higher=False))
    if "stability" in extra:
        s = extra["stability"]
        out.append(_metric("stability_jaccard", s["jaccard"],
                           f"{s['jaccard']:.3f} (React cold rerun; recall {s['recall_a']:.2f} vs {s['recall_b']:.2f})"))
    usd = sum(st.get("usd_full", st.get("usd_estimate", 0)) for r in rows for st in r["usage"].values())
    calls = sum(st.get("calls", 0) for r in rows for st in r["usage"].values())
    secs = sum(sum(r["timings_s"].values()) for r in rows)
    out.append({"name": "cost_latency", "value": {"usd_full": usd, "llm_calls": calls, "seconds": secs},
                "display": f"~${usd:.2f} for {calls} LLM calls to produce {len(rows)} models; "
                           f"{secs:.0f}s stage time on the last (possibly cached) run",
                "target": None, "pass": None, "gate": "report"})
    return out


def render_markdown(res: dict) -> str:
    L = ["# Evaluation results", "", "Generated by `urx eval`. Hard gates are asserted in `tests/test_eval_gates.py`.", "",
         "| Metric | Result | Target | Gate | Pass |", "|---|---|---|---|---|"]
    for m in res["metrics"]:
        L.append(f"| {m['name']} | {m['display']} | {m['target'] if m['target'] is not None else '–'} | {m['gate']} | "
                 f"{'✅' if m['pass'] else ('❌' if m['pass'] is False else '–')} |")
    L += ["", "## Per upgrade", "", "| Upgrade | Paths | Recall | Strict precision | Est. precision | Classification | Grounding | Validator errors | Overall confidence |",
          "|---|---|---|---|---|---|---|---|---|"]
    for slug, r in res["per_upgrade"].items():
        f = lambda k: f"{r[k][0]}/{r[k][1]}" if k in r else "–"
        L.append(f"| {slug} | {r['paths']} | {f('recall')} | {f('strict_precision')} | {f('estimated_precision')} | "
                 f"{f('classification')} | {f('grounding')} | {r['validator_errors']} | {r['overall_confidence']} |")
    L += ["", "## Missed gold items", ""]
    for slug, r in res["per_upgrade"].items():
        for g in r.get("gold_items", []):
            if g["kind"] == "risk" and not g["hits"]["risk"]:
                where = [k for k, v in g["hits"].items() if v]
                L.append(f"- {slug} `{g['gold_id']}`" + (f" (found as {', '.join(where)})" if where else " (not found)"))
            elif g["kind"] != "risk" and not g["correct_bucket"]:
                where = [k for k, v in g["hits"].items() if v]
                L.append(f"- {slug} `{g['gold_id']}` expected {g['kind']}, found as {', '.join(where) or 'nothing'}")
    ab = res["extra"].get("ablations")
    if ab:
        L += ["", "## Ablations", "", "| Upgrade | Pipeline recall | Single-prompt recall | Single-prompt grounding | Single-prompt strict precision | Heading-filter recall ceiling | Keyword-filter recall ceiling |",
              "|---|---|---|---|---|---|---|"]
        for slug, a in ab.items():
            r = res["per_upgrade"][slug]
            rec = r["recall"][0] / r["recall"][1] if r.get("recall") and r["recall"][1] else 0
            b = a.get("baseline_single_prompt", {})
            fmt = lambda x: f"{x:.2f}" if isinstance(x, (int, float)) else "–"
            L.append(f"| {slug} | {rec:.2f} | {fmt(b.get('recall'))} | {fmt(b.get('grounding_rate'))} | "
                     f"{fmt(b.get('strict_precision'))} | {fmt(a['filters']['heading_filter'])} | {fmt(a['filters']['keyword_filter'])} |")
        L += ["", "Single-prompt outputs have no conditions, roles or search queries at all, so they are not consumable by the downstream engine regardless of recall.",
              "Filter ceilings show how much of the pipeline's gold recall would survive if items were pre-filtered by heading or keyword instead of LLM triage over every item."]
    return "\n".join(L) + "\n"
