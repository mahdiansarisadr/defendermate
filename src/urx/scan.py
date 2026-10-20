"""C8 demo downstream consumer: runs ripgrep search queries against the synthetic fixture app only."""

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

from . import config
from .models import RiskModel

ALLOWED_ROOT = (config.ROOT / "fixtures").resolve()


def _rg(pattern: str, repo: Path) -> list[str]:
    rg = shutil.which("rg")
    if rg is None:
        raise RuntimeError("ripgrep (rg) is required for scan")
    args = pattern.split(" --glob ")
    globs = [g.strip().strip("'\"") for g in args[1:]]
    globs.append("!*.md")
    cmd = [rg, "-n", "--no-heading", "-e", args[0].strip()] + [x for g in globs for x in ("--glob", g)] + [str(repo)]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if r.returncode == 2 and "regex parse error" in r.stderr:
        r = subprocess.run([rg, "-P", *cmd[1:]], capture_output=True, text=True, timeout=30)
    return sorted(set(l for l in r.stdout.splitlines() if l))[:20]


def scan(model_path: Path, repo: Path) -> list[dict]:
    repo = repo.resolve()
    if ALLOWED_ROOT not in repo.parents and repo != ALLOWED_ROOT:
        raise PermissionError("scan only runs against fixtures/ (assignment constraint: no real repositories)")
    model = RiskModel.model_validate(json.loads(model_path.read_text()))
    results = []
    for p in model.risk_paths:
        cond_hits = {}
        for c in p.conditions:
            qs = [q for q in c.search_queries if q.tool == "ripgrep"]
            if c.category == "version" or not qs:
                continue
            hits = []
            for q in qs:
                try:
                    hits += _rg(q.query, repo)
                except subprocess.TimeoutExpired:
                    pass
            cond_hits[c.condition_id] = {"role": c.role, "hits": hits, "statement": c.statement}
        if not cond_hits:
            continue
        req = [v for v in cond_hits.values() if v["role"] == "required"]
        alt = [v for v in cond_hits.values() if v["role"] == "alternative"]
        dis = [v for v in cond_hits.values() if v["role"] == "disqualifying"]
        fires = (all(v["hits"] for v in req) if req else bool(alt)) and (not alt or any(v["hits"] for v in alt))
        # Disqualifier queries are LLM-written and sometimes inverted, so they never silently suppress a path.
        disputed = fires and any(v["hits"] for v in dis)
        results.append({"path_id": p.path_id, "path_name": p.path_name, "risk_level": p.risk_level,
                        "fires": fires, "needs_review": disputed, "conditions": cond_hits})
    return results
