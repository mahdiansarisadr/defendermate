"""FastAPI backend for the UI (TDD 17.3). Local only; serves outputs/, eval/ and review decisions."""

from __future__ import annotations

import json
import threading
import uuid
from collections import Counter
from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from . import config
from .models import RiskModel
from .normalize import normalize
from .overrides import Override, delete_override, load_overrides, save_override
from .registry import list_projects, load_registry
from .report import path_mermaid
from .validate import CacheContext

app = FastAPI(title="URX", version="0.1.0")
RUNS: dict[str, dict] = {}
_LOCK = threading.Lock()


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _model_path(slug: str):
    p = config.OUTPUTS_DIR / slug / "risk_model.json"
    if not p.exists():
        raise HTTPException(404, f"no risk model for {slug}")
    return p


def _load(slug: str) -> dict:
    return json.loads(_model_path(slug).read_text())


def _eval() -> dict:
    p = config.EVAL_DIR / "results.json"
    return json.loads(p.read_text()) if p.exists() else {}


@app.get("/api/upgrades")
def upgrades() -> list[dict]:
    ev = _eval().get("per_upgrade", {})
    slugs = [config.upgrade_slug(*u) for u in config.DEFAULT_UPGRADES]
    slugs += sorted(p.name for p in config.OUTPUTS_DIR.glob("*") if p.is_dir() and p.name not in slugs
                    and (p / "risk_model.json").exists())
    out = []
    for slug in slugs:
        f = config.OUTPUTS_DIR / slug / "risk_model.json"
        row: dict = {"slug": slug, "exists": f.exists()}
        if f.exists():
            m = json.loads(f.read_text())
            pipe = m.get("pipeline", {})
            row.update({
                "project": m["project"], "current_version": m["current_version"], "target_version": m["target_version"],
                "paths": len(m["risk_paths"]), "by_level": Counter(p["risk_level"] for p in m["risk_paths"]),
                "by_confidence": Counter(p["confidence"] for p in m["risk_paths"]),
                "by_type": Counter(p["risk_type"] for p in m["risk_paths"]),
                "overall_confidence": m["overall_confidence"], "validation": pipe.get("validation", {}),
                "generated_at": pipe.get("generated_at"), "funnel": pipe.get("funnel", {}),
                "usd_estimate": round(sum(s.get("usd_estimate", 0) for s in pipe.get("usage", {}).values()), 2),
                "usd_full": round(sum(s.get("usd_full", 0) for s in pipe.get("usage", {}).values()), 2),
                "context_facts": len(m.get("context_facts", [])), "disqualified": len(m.get("disqualified_candidates", [])),
                "open_questions": len(m.get("open_questions", [])),
                "sources_used": sum(s["status"] == "used" for s in m["source_inventory"]),
                "sources_rejected": sum(s["status"] == "rejected" for s in m["source_inventory"]),
                "review_flags": sum(bool(p.get("review_flags")) for p in m["risk_paths"]),
            })
            e = ev.get(slug, {})
            for k in ("recall", "strict_precision", "estimated_precision", "grounding"):
                if k in e:
                    row[k] = e[k]
        out.append(row)
    return out


@app.get("/api/upgrades/{slug}")
def upgrade(slug: str) -> dict:
    return _load(slug)


@app.get("/api/upgrades/{slug}/report", response_class=PlainTextResponse)
def report(slug: str) -> str:
    p = config.OUTPUTS_DIR / slug / "report.md"
    if not p.exists():
        raise HTTPException(404)
    return p.read_text()


@app.get("/api/upgrades/{slug}/paths/{path_id}/graph", response_class=PlainTextResponse)
def path_graph(slug: str, path_id: str) -> str:
    m = RiskModel.model_validate(_load(slug))
    p = next((p for p in m.risk_paths if p.path_id == path_id), None)
    if not p:
        raise HTTPException(404)
    return path_mermaid(p)


@app.get("/api/upgrades/{slug}/evidence")
def evidence_context(slug: str, source_id: str, quote: str, window: int = 400) -> dict:
    m = _load(slug)
    ctx = CacheContext(m["project"], m["source_inventory"])
    corpus = ctx.corpus(source_id)
    if corpus is None:
        raise HTTPException(404, "source not cached")
    q = normalize(quote)
    i = corpus.find(q)
    src = next((s for s in m["source_inventory"] if s["source_id"] == source_id), {})
    if i < 0:
        return {"found": False, "source": src}
    return {"found": True, "before": corpus[max(0, i - window):i], "match": q, "after": corpus[i + len(q):i + len(q) + window],
            "source": src}


@app.get("/api/upgrades/{slug}/intermediate/{name}")
def intermediate(slug: str, name: str, limit: int = 2000) -> list[dict]:
    allowed = {"items", "triage", "triage_disagreements", "rejected", "release_risks", "revert_candidates",
               "version_facts", "extractions"}
    if name not in allowed:
        raise HTTPException(400, f"one of {sorted(allowed)}")
    p = config.OUTPUTS_DIR / slug / "intermediate" / f"{name}.jsonl"
    if not p.exists():
        return []
    return [json.loads(l) for l in p.read_text().splitlines()[:limit] if l]


@app.get("/api/upgrades/{slug}/compose_log")
def compose_log(slug: str) -> dict:
    p = config.OUTPUTS_DIR / slug / "intermediate" / "compose_log.json"
    return json.loads(p.read_text()) if p.exists() else {}


@app.get("/api/upgrades/{slug}/runlog")
def runlog(slug: str, run_id: str | None = None) -> list[dict]:
    p = config.OUTPUTS_DIR / slug / "run_log.jsonl"
    if not p.exists():
        return []
    rows = [json.loads(l) for l in p.read_text().splitlines() if l]
    return [r for r in rows if not run_id or r.get("run_id") == run_id]


@app.get("/api/eval")
def eval_results() -> dict:
    return _eval()


@app.post("/api/eval/run")
def eval_run(llm: bool = False) -> dict:
    from .evaluate import run_eval

    return run_eval(use_llm=llm)


@app.get("/api/registry")
def registry() -> list[dict]:
    out = []
    for name in list_projects():
        r = load_registry(name)
        out.append({"project": r.project, "known_releases": r.known_releases, "mode": r.traversal.mode,
                    "sources": [{"id": s.id, "type": s.type, "tier": s.tier, "url": s.url_template} for s in r.sources],
                    "coverage_gaps": r.coverage_gaps})
    return out


class RunRequest(BaseModel):
    project: str
    current_version: str
    target_version: str
    offline: bool = True


def _run_thread(run_id: str, req: RunRequest) -> None:
    from .llm import LLMClient
    from .pipeline import run_upgrade

    try:
        known = {config.upgrade_slug(*u) for u in config.DEFAULT_UPGRADES}
        m = run_upgrade(req.project, req.current_version, req.target_version, offline=req.offline,
                        client=LLMClient(offline=req.offline), run_id=run_id, known_models=known)
        with _LOCK:
            RUNS[run_id].update(status="ok", ended=_now(), paths=len(m.risk_paths),
                                validation=m.pipeline.get("validation"))
    except Exception as e:  # surfaced to the UI
        with _LOCK:
            RUNS[run_id].update(status="error", ended=_now(), error=f"{type(e).__name__}: {e}"[:2000])


@app.post("/api/runs")
def start_run(req: RunRequest) -> dict:
    load_registry(req.project)
    slug = config.upgrade_slug(req.project, req.current_version, req.target_version)
    with _LOCK:
        if any(r["slug"] == slug and r["status"] == "running" for r in RUNS.values()):
            raise HTTPException(409, f"a run for {slug} is already in progress")
        run_id = uuid.uuid4().hex[:10]
        RUNS[run_id] = {"run_id": run_id, "slug": slug, "status": "running", "started": _now(), **req.model_dump()}
    threading.Thread(target=_run_thread, args=(run_id, req), daemon=True).start()
    return RUNS[run_id]


@app.get("/api/runs")
def list_runs() -> list[dict]:
    return sorted(RUNS.values(), key=lambda r: r["started"], reverse=True)


@app.get("/api/runs/{run_id}")
def get_run(run_id: str) -> dict:
    r = RUNS.get(run_id)
    if not r:
        raise HTTPException(404)
    return {**r, "events": runlog(r["slug"], run_id)}


@app.get("/api/overrides")
def overrides() -> list[dict]:
    return [o.model_dump() for o in load_overrides()]


@app.post("/api/overrides")
def add_override(o: Override) -> list[dict]:
    return [x.model_dump() for x in save_override(o)]


@app.delete("/api/overrides/{oid:path}")
def remove_override(oid: str) -> list[dict]:
    delete_override(oid)
    return [o.model_dump() for o in load_overrides()]


if config.UI_DIST.exists():
    app.mount("/assets", StaticFiles(directory=config.UI_DIST / "assets"), name="assets")

    @app.get("/{full_path:path}")
    def spa(full_path: str):
        f = config.UI_DIST / full_path
        if full_path and f.is_file():
            return FileResponse(f)
        return FileResponse(config.UI_DIST / "index.html")
