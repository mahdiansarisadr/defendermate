"""End-to-end orchestration of pipelines A (ingest), B (per-release extraction) and C (composition)."""

from __future__ import annotations

import json
import time
import uuid
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from . import compose, config, items as items_mod
from .extract import ItemResult, extract_item, short_hash
from .facts import extract_facts, facts_for_release
from .fetch import fetch_all
from .judge import judge_paths
from .link import full_symbol, merge_duplicates
from .llm import LLMClient
from .models import (
    APP_SIDE_CATEGORIES, ChangeItem, ContextFact, Disagreement, Evidence, EvidenceSummary, RiskModel, RiskPath,
    SourceRecord, TriageLabel,
)
from .normalize import opening_quote
from .overrides import apply_overrides, load_overrides
from .planner import plan as make_plan
from .registry import load_registry, expand_sources
from .report import write_graph, write_report
from .rubric import apply_rubric, overall_confidence
from .triage import triage
from .validate import CacheContext, summarize, validate_model, verify_quote
from .adapters import json_meta

CONTEXT_SECTIONS = {"removed", "deprecated", "incompatible", "urgent", "requirements", "changed"}


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class RunLog:
    def __init__(self, out_dir: Path, run_id: str, project: str, upgrade: str) -> None:
        self.path = out_dir / "run_log.jsonl"
        self.run_id, self.project, self.upgrade = run_id, project, upgrade
        out_dir.mkdir(parents=True, exist_ok=True)
        self.path.write_text("")
        self.t0 = time.time()
        self.stage_t: dict[str, float] = {}
        self.timings: dict[str, float] = {}

    def __call__(self, event: str, **data: Any) -> None:
        rec = {"ts": _now(), "elapsed_s": round(time.time() - self.t0, 2), "run_id": self.run_id,
               "upgrade": self.upgrade, "event": event, **data}
        with self.path.open("a") as f:
            f.write(json.dumps(rec, default=str) + "\n")

    def stage(self, name: str):
        log = self

        class _S:
            def __enter__(self_inner):
                log.stage_t[name] = time.time()
                log("stage_start", stage=name)

            def __exit__(self_inner, et, ev, tb):
                dt = round(time.time() - log.stage_t[name], 2)
                log.timings[name] = dt
                log("stage_error" if et else "stage_end", stage=name, seconds=dt,
                    **({"error": str(ev)[:500]} if et else {}))
                return False

        return _S()


def _write_jsonl(path: Path, rows) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as f:
        for r in rows:
            f.write(json.dumps(r.model_dump() if hasattr(r, "model_dump") else r, ensure_ascii=False, default=str) + "\n")


def _ensure_unique_path_ids(paths: list[RiskPath]) -> None:
    """Distinct risks can share a risk_key (norm_symbol keeps only the last dotted component)."""
    seen: set[str] = set()
    for p in sorted(paths, key=lambda p: (p.path_id, full_symbol(p.primary_symbol), p.path_name)):
        if p.path_id in seen:
            p.path_id = f"{p.path_id}_{short_hash(full_symbol(p.primary_symbol), p.path_name, n=4)}"
        seen.add(p.path_id)


def _ensure_unique_condition_ids(paths: list[RiskPath]) -> None:
    """One statement can be emitted under two categories. Runs after the judge, whose cache key
    includes condition ids."""
    for p in paths:
        cids: set[str] = set()
        for c in p.conditions:
            if c.condition_id in cids:
                c.condition_id = f"{c.condition_id}_{c.category}"
            cids.add(c.condition_id)


def _repair(model: RiskModel, ctx: CacheContext, rejected: list[dict]) -> None:
    """G15: deterministic repair before the final gate. Every drop is logged."""
    used = {s.source_id for s in model.source_inventory if s.status == "used"}

    def ok(ev: Evidence) -> bool:
        if ev.source_id not in used:
            return False
        if ev.json_path:
            doc = ctx.json_doc(ev.source_id)
            return doc is not None and json_meta.lookup_str(doc, ev.json_path) == ev.expected
        return ev.quote is not None and verify_quote(ev.quote, ctx.corpus(ev.source_id))

    keep_paths = []
    for p in model.risk_paths:
        conds = []
        for c in p.conditions:
            good = [e for e in c.evidence if ok(e)]
            for e in c.evidence:
                if e not in good:
                    rejected.append({"kind": "evidence_failed_validation", "path_id": p.path_id,
                                     "condition_id": c.condition_id, "quote": e.quote, "source_id": e.source_id})
            c.evidence = good
            for e in good:
                e.verified = True
            if c.evidence or (c.role == "uncertain" and c.ambiguities):
                conds.append(c)
            else:
                rejected.append({"kind": "condition_dropped_no_evidence", "path_id": p.path_id, "statement": c.statement})
        p.conditions = conds
        cats = {c.category for c in conds}
        if "version" in cats and cats & APP_SIDE_CATEGORIES:
            keep_paths.append(p)
        else:
            rejected.append({"kind": "path_dropped_structure", "path_id": p.path_id, "path_name": p.path_name})
    model.risk_paths = keep_paths
    model.context_facts = [f for f in model.context_facts if all(ok(e) for e in f.evidence) and f.evidence]
    model.disqualified_candidates = [d for d in model.disqualified_candidates if all(ok(e) for e in d.evidence)]


def _summary(project: str, plan, paths: list[RiskPath], n_ctx: int, n_disq: int) -> str:
    lv = Counter(p.risk_level for p in paths)
    types = Counter(p.risk_type for p in paths).most_common(3)
    crit = [p.path_name for p in paths if p.risk_level == "critical"][:5]
    return (f"{project} {plan.current_version} -> {plan.target_version} crosses {plan.hops} release(s) "
            f"({', '.join(plan.releases)}). {len(paths)} risk paths: "
            + ", ".join(f"{lv[k]} {k}" for k in ("critical", "high", "medium", "low") if lv[k])
            + ". Main risk types: " + ", ".join(f"{t} ({n})" for t, n in types) + "."
            + (f" Critical: {'; '.join(crit)}." if crit else "")
            + f" {n_ctx} context facts and {n_disq} disqualified candidates are listed separately. {config.DISCLAIMER}")


def run_upgrade(project: str, current: str, target: str, offline: bool = False, client: LLMClient | None = None,
                run_id: str | None = None, known_models: set[str] | None = None) -> RiskModel:
    reg = load_registry(project)
    slug = config.upgrade_slug(project, current, target)
    pslug = config.slugify(project)
    out = config.OUTPUTS_DIR / slug
    inter = out / "intermediate"
    run_id = run_id or uuid.uuid4().hex[:10]
    log = RunLog(out, run_id, project, slug)
    client = client or LLMClient(offline=offline)
    log("run_start", project=project, current=current, target=target, offline=offline,
        models=config.MODELS[client.provider_name])
    ctx_vars = {"project": project, "current_version": current, "target_version": target}
    rejected: list[dict] = []
    funnel: dict[str, int] = {}

    try:
        with log.stage("plan"):
            plan = make_plan(reg, current, target)
            log("plan", releases=plan.releases, future=plan.future_releases)

        with log.stage("fetch"):
            fetched = fetch_all(project, expand_sources(reg, plan.releases, current, target), offline=offline, log=log)

        with log.stage("parse"):
            inventory: dict[str, SourceRecord] = {}
            corpora: dict[str, str] = {}
            section_texts: dict[str, str] = {}
            all_items: list[ChangeItem] = []
            patch_scanned = 0
            for f in fetched:
                s = f.source
                rec = SourceRecord(
                    source_id=s.inventory_id, title=s.title, url=s.url, source_type=s.spec.type,
                    retrieved_at=f.meta.get("retrieved_at", ""),
                    why_relevant=s.spec.why_relevant.replace("{release}", s.version_label),
                    authority_tier=s.spec.tier, content_hash=f.meta.get("content_hash", ""),
                    pinned_ref=f.meta.get("pinned_ref", ""), release=s.release, raw_url=s.raw_url,
                    registry_source=s.registry_source,
                )
                if f.stub_reason:
                    rec.status, rec.rejection_reason = "rejected", f.stub_reason
                    inventory[rec.source_id] = rec
                    continue
                if s.spec.format == "json":
                    inventory[rec.source_id] = rec
                    continue
                ps = items_mod.build_items(project, f)
                if not ps.windows_found:
                    rec.status, rec.rejection_reason = "rejected", "section_not_found"
                    inventory[rec.source_id] = rec
                    continue
                if s.spec.revert_scan:
                    patch_scanned += 1
                    if not ps.items:
                        continue
                inventory[rec.source_id] = rec
                corpora[rec.source_id] = ps.corpus
                section_texts.update(ps.section_texts)
                all_items += ps.items
            all_items = items_mod.dedup(all_items)
            revert_items = [i for i in all_items if i.revert_candidate]
            base_items = [i for i in all_items if not i.revert_candidate]
            on_path, future, dropped = compose.r4_on_path(base_items, plan)
            funnel.update(items_total=len(base_items), items_on_path=len(on_path), items_future=len(future),
                          items_dropped_r4=len(dropped), revert_candidates=len(revert_items),
                          patch_notes_scanned=patch_scanned)
            _write_jsonl(inter / "items.jsonl", on_path)
            _write_jsonl(inter / "revert_candidates.jsonl", revert_items)
            log("parsed", **funnel)
            facts = extract_facts(reg, fetched)
            _write_jsonl(inter / "version_facts.jsonl", facts)

        with log.stage("triage"):
            titles = {k: v.title for k, v in inventory.items()}
            labels, disagreements = triage(client, on_path, ctx_vars, titles, log=log)
            label_by = {l.item_id: l for l in labels}
            _write_jsonl(inter / "triage.jsonl", labels)
            _write_jsonl(inter / "triage_disagreements.jsonl", disagreements)
            c = Counter(l.label for l in labels)
            funnel.update(triage_risk=c["risk"], triage_context=c["context"], triage_noise=c["noise"],
                          sweep_flipped=len(disagreements))

        with log.stage("extract"):
            risk_items = [i for i in on_path if label_by[i.item_id].label == "risk"]

            def work(it: ChangeItem) -> ItemResult:
                parent = section_texts.get(it.parent_id or "", "")
                return extract_item(client, it, parent, facts_for_release(facts, it.release),
                                    inventory[it.source_id], corpora[it.source_id], ctx_vars, pslug)

            with ThreadPoolExecutor(config.MAX_WORKERS) as ex:
                results = list(ex.map(work, risk_items))
            raw_paths: list[RiskPath] = []
            contexts: list[ContextFact] = []
            failures = []
            for r in results:
                raw_paths += r.paths
                rejected += r.rejected
                if r.context:
                    contexts.append(r.context)
                if r.failed:
                    failures.append({"item_id": r.item.item_id, "error": r.failed[:500]})
            _write_jsonl(inter / "extractions.jsonl", [
                {"item_id": r.item.item_id, "source_id": r.item.source_id, "release": r.item.release,
                 "paths": [p.model_dump() for p in r.paths], "context": r.context.model_dump() if r.context else None,
                 "failed": r.failed} for r in results])
            funnel.update(extracted_items=len(risk_items), extracted_paths=len(raw_paths),
                          extractor_context=len(contexts), extraction_failures=len(failures))
            log("extracted", paths=len(raw_paths), failures=len(failures))

            for it in on_path:
                l = label_by[it.item_id]
                if l.label == "context" and it.section_type in CONTEXT_SECTIONS:
                    q = opening_quote(it.text, 40)
                    contexts.append(ContextFact(
                        fact_id=f"ctx_{it.item_id}", statement=q, introduced_in=it.release,
                        evidence=[Evidence(source_id=it.source_id, source_type=inventory[it.source_id].source_type,
                                           quote_or_summary=q, quote=q, verified=True,
                                           relevance="Item text in the release documentation.")],
                        why_not_risk=l.reason, fires_at="future_removal" if it.section_type == "deprecated" else None))

        with log.stage("link"):
            fpaths, requires = compose.fact_paths(reg, facts, plan, pslug, inventory)
            linked, merge_log = merge_duplicates(raw_paths + fpaths)
            _ensure_unique_path_ids(linked)
            _write_jsonl(inter / "release_risks.jsonl", linked)
            funnel.update(fact_paths=len(fpaths), linked_paths=len(linked), merged=len(merge_log))

        with log.stage("compose"):
            paths, r5_log = compose.r5_start_applicability(linked, current)
            paths, disq, unresolved, r1_log = compose.r1_reverts(client, paths, revert_items, target, corpora,
                                                                 inventory, ctx_vars)
            paths, r2_log = compose.r2_supersession(paths)
            k8s_guide = [i for i in base_items if i.registry_source.endswith("deprecation_guide")]
            rmap = compose.removal_map(k8s_guide)
            r3_log = compose.r3_remediation(paths, rmap, target, inventory)
            contexts += compose.r6_future_context(
                [i for i in future if inventory[i.source_id].source_type == "official_deprecation_notice"],
                inventory, target)
            disagreements_src: list[Disagreement] = compose.fact_disagreements(paths, facts, reg, inventory)
            for e in r3_log:
                if "itself removed" in e["note"]:
                    disagreements_src.append(Disagreement(
                        topic=f"remediation for {e['path_id']}", sources=[],
                        detail=f"Per-release guidance names {e['api']}, which is removed in v{e['removed_in']}.",
                        resolution="Remediation recomputed against the target version (R3)."))
            (inter / "compose_log.json").write_text(json.dumps(
                {"r5": r5_log, "r1": r1_log, "r1_unresolved": unresolved, "r2": r2_log, "r3": r3_log,
                 "merge": merge_log}, indent=1, default=str))
            funnel.update(composed_paths=len(paths), disqualified=len(disq), superseded=len(r2_log))

        with log.stage("judge"):
            judge_stats = judge_paths(client, paths, titles={k: v.title for k, v in inventory.items()}, log=log)
            _ensure_unique_condition_ids(paths)

        with log.stage("rubric"):
            tiers = {k: v.authority_tier for k, v in inventory.items()}
            apply_rubric(paths, tiers)
            ov = load_overrides()
            disq += apply_overrides(paths, ov)

        with log.stage("assemble"):
            paths.sort(key=lambda p: (["critical", "high", "medium", "low", "unknown"].index(p.risk_level), p.path_id))
            seen_ctx: set[str] = set()
            uniq_ctx = []
            for cf in contexts:
                if cf.fact_id not in seen_ctx:
                    seen_ctx.add(cf.fact_id)
                    uniq_ctx.append(cf)
            open_q = list(reg.coverage_gaps)
            for s in inventory.values():
                if s.status == "rejected":
                    open_q.append(f"Source {s.source_id} was rejected ({s.rejection_reason}); its content was not used.")
            open_q += [f"Extraction failed for item {f['item_id']}; it was not analysed." for f in failures]
            open_q += unresolved
            for p in paths:
                for c in p.conditions:
                    if c.role == "uncertain":
                        open_q.append(f"[{p.path_id}] Unconfirmed: {c.statement}"
                                      + (f" ({c.ambiguities[0][:200]})" if c.ambiguities else ""))
            disputed = {p.path_id for p in paths if "judge_not_supported" in p.review_flags
                        or any(c.ambiguities and "disagreement" in " ".join(c.ambiguities).lower() for c in p.conditions)}
            label = lambda p: f"{p.path_id}: {p.path_name}"
            es = EvidenceSummary(
                high_confidence_risks=[label(p) for p in paths if p.confidence == "high" and p.path_id not in disputed],
                medium_confidence_risks=[label(p) for p in paths if p.confidence == "medium" and p.path_id not in disputed],
                low_confidence_or_disputed_risks=[label(p) for p in paths if p.confidence == "low" or p.path_id in disputed],
                sources_with_disagreements=disagreements_src, open_questions=open_q,
            )
            n_rej = sum(1 for s in inventory.values() if s.status == "rejected" and s.rejection_reason != "transclusion_stub")
            model = RiskModel(
                project=project, current_version=current, target_version=target,
                upgrade=f"{current}_to_{target}", disclaimer=config.DISCLAIMER, summary="",
                source_inventory=sorted(inventory.values(), key=lambda s: s.source_id), risk_paths=paths,
                open_questions=open_q, overall_confidence=overall_confidence(paths, len(failures), n_rej),
                evidence_summary=es, context_facts=uniq_ctx, disqualified_candidates=disq, requires_upgrades=requires,
                plan=plan.model_dump(),
            )
            vctx = CacheContext(project, [s.model_dump() for s in model.source_inventory])
            _repair(model, vctx, rejected)
            model.summary = _summary(project, plan, model.risk_paths, len(model.context_facts),
                                     len(model.disqualified_candidates))
            keep = {p.path_id for p in model.risk_paths}
            for lst in (es.high_confidence_risks, es.medium_confidence_risks, es.low_confidence_or_disputed_risks):
                lst[:] = [x for x in lst if x.split(":")[0] in keep]
            funnel["final_paths"] = len(model.risk_paths)
            funnel["context_facts"] = len(model.context_facts)
            model.pipeline = {
                "run_id": run_id, "generated_at": _now(), "provider": client.provider_name,
                "models": config.MODELS[client.provider_name],
                "prompts": ["triage.v1", "extract.v1", "judge.v1", "reconcile.v1"],
                "funnel": funnel, "judge": judge_stats, "usage": client.usage.by_stage, "timings_s": log.timings,
            }

        with log.stage("validate"):
            data = json.loads(model.model_dump_json())
            issues = validate_model(data, vctx, extra_models=known_models)
            model.pipeline["validation"] = summarize(issues)
            data["pipeline"]["validation"] = model.pipeline["validation"]
            _write_jsonl(inter / "rejected.jsonl", rejected)
            (inter / "validation.json").write_text(json.dumps([i.to_dict() for i in issues], indent=1))

        out.mkdir(parents=True, exist_ok=True)
        (out / "risk_model.json").write_text(json.dumps(data, indent=2, ensure_ascii=False))
        (out / "source_inventory.json").write_text(json.dumps({
            "project": project, "current_version": current, "target_version": target,
            "sources": data["source_inventory"]}, indent=2, ensure_ascii=False))
        write_report(model, out / "report.md")
        write_graph(model, out / "graph.mmd")
        log("run_end", status="ok", final_paths=len(model.risk_paths), validation=model.pipeline["validation"],
            usage=client.usage.by_stage)
        return model
    except Exception as e:
        log("run_end", status="error", error=f"{type(e).__name__}: {e}"[:1000])
        raise
