"""URX command line (TDD C9)."""

from __future__ import annotations

import json
from pathlib import Path

import typer

from . import config

app = typer.Typer(add_completion=False, help="Upgrade Risk Extraction: evidence-grounded upgrade risk models.")


@app.command()
def extract(project: str = typer.Option(None, "--project"),
            current_version: str = typer.Option(None, "--current-version"),
            target_version: str = typer.Option(None, "--target-version"),
            all_: bool = typer.Option(False, "--all", help="Run the 5 assignment upgrades"),
            offline: bool = typer.Option(False, "--offline", help="Use only cache/ and llm_cache/"),
            provider: str = typer.Option(None, "--provider", help="anthropic | openai")) -> None:
    """Run the full pipeline and write outputs/<project>_<from>_to_<to>/."""
    from .llm import LLMClient
    from .pipeline import run_upgrade

    jobs = config.DEFAULT_UPGRADES if all_ else [(project, current_version, target_version)]
    if not all_ and not all(jobs[0]):
        raise typer.BadParameter("give --project, --current-version and --target-version, or --all")
    known = {config.upgrade_slug(*j) for j in jobs}
    for p, c, t in jobs:
        client = LLMClient(provider=provider, offline=offline)
        m = run_upgrade(p, c, t, offline=offline, client=client, known_models=known)
        v = m.pipeline.get("validation", {})
        usd = sum(s.get("usd_estimate", 0) for s in m.pipeline.get("usage", {}).values())
        typer.echo(f"{p} {c}->{t}: {len(m.risk_paths)} paths, overall {m.overall_confidence}, "
                   f"errors={v.get('errors')} warnings={v.get('warnings')}, ~${usd:.2f}")


@app.command()
def validate(paths: list[Path] = typer.Argument(..., help="risk_model.json files")) -> None:
    """Gate mode: exit 1 on any validator error."""
    from .validate import CacheContext, summarize, validate_model

    bad = 0
    for p in paths:
        data = json.loads(p.read_text())
        issues = validate_model(data, CacheContext(data["project"], data["source_inventory"]))
        s = summarize(issues)
        typer.echo(f"{p}: {s}")
        for i in issues:
            if i.level == "error":
                typer.echo(f"  {i.code} {i.where}: {i.message}")
        bad += s["errors"]
    raise typer.Exit(1 if bad else 0)


@app.command()
def report(out_dir: Path) -> None:
    """Regenerate report.md and graph.mmd from risk_model.json."""
    from .models import RiskModel
    from .report import write_graph, write_report

    m = RiskModel.model_validate(json.loads((out_dir / "risk_model.json").read_text()))
    write_report(m, out_dir / "report.md")
    write_graph(m, out_dir / "graph.mmd")
    typer.echo(f"wrote {out_dir / 'report.md'}")


@app.command(name="eval")
def eval_cmd(llm: bool = typer.Option(True, help="Run LLM-based metrics (precision judge, judge calibration)"),
             offline: bool = typer.Option(False, "--offline"),
             ablations: bool = typer.Option(False, help="Also run ablations (baseline costs extra LLM calls)"),
             stability: bool = typer.Option(False, help="Cold rerun of React for the stability metric")) -> None:
    """Compute TDD 17.4 metrics against gold/ and write eval/results.{json,md}."""
    from .evaluate import run_eval

    res = run_eval(use_llm=llm, offline=offline, ablations=ablations, stability=stability)
    for m in res["metrics"]:
        typer.echo(f"{'PASS' if m['pass'] else ('FAIL' if m['pass'] is False else 'info'):5} {m['name']}: {m['display']}")


@app.command()
def experiment(name: str = typer.Option(..., "--config", help="haiku_haiku | haiku_sonnet | sonnet_opus"),
               stability: bool = typer.Option(True, help="Cold React rerun for the stability metric")) -> None:
    """Rerun React, PostgreSQL and Next.js under one model config and evaluate into experiments/<config>/."""
    from .experiment import CONFIGS, run_experiment

    if name not in CONFIGS:
        raise typer.BadParameter(f"one of {sorted(CONFIGS)}")
    run_experiment(name, stability=stability, log=typer.echo)


@app.command(name="compare-experiments")
def compare_experiments() -> None:
    """Write experiments/comparison.{json,md} from every finished config."""
    from .experiment import compare

    out = compare()
    for r in out["rows"]:
        typer.echo(f"{r['label']:16} ${r['cost_usd']:.2f}  recall {r['recall']:.3f}  est.prec {r['estimated_precision']:.3f}"
                   f"  F1 {r['f1']:.3f}  pareto={r['pareto']}")


@app.command()
def scan(model: Path = typer.Option(..., "--model"), repo: Path = typer.Option(..., "--repo")) -> None:
    """Demo downstream consumer over fixtures/demo_app (never real repositories)."""
    from .scan import scan as run_scan

    for r in run_scan(model, repo):
        flag = ("FIRES?" if r["needs_review"] else "FIRES ") if r["fires"] else "  -   "
        typer.echo(f"{flag} [{r['risk_level']}] {r['path_name']}")
        for c in r["conditions"].values():
            for h in c["hits"][:2]:
                typer.echo(f"        {h}")


@app.command(name="export-schema")
def export_schema() -> None:
    """Write schemas/risk_model.schema.json from the Pydantic model."""
    from .models import RiskModel

    config.SCHEMAS_DIR.mkdir(exist_ok=True)
    (config.SCHEMAS_DIR / "risk_model.schema.json").write_text(json.dumps(RiskModel.model_json_schema(), indent=1))
    typer.echo("wrote schemas/risk_model.schema.json")


@app.command()
def serve(host: str = "127.0.0.1", port: int = 8765) -> None:
    """Start the API + UI server."""
    import uvicorn

    uvicorn.run("urx.server:app", host=host, port=port, log_level="info")


if __name__ == "__main__":
    app()
