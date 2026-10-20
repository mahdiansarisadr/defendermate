"""C6 markdown report with review checklist, and Mermaid risk graph."""

from __future__ import annotations

import json
from pathlib import Path

from .models import RiskModel, RiskPath


def _esc(s: str) -> str:
    return s.replace('"', "'").replace("\n", " ")[:90]


def path_mermaid(p: RiskPath) -> str:
    lines = ["graph LR", f'  P["{_esc(p.path_name)}<br/>{p.risk_level} / {p.confidence}"]']
    req = [c for c in p.conditions if c.role == "required"]
    alt = [c for c in p.conditions if c.role == "alternative"]
    if req:
        lines.append('  AND{{"AND"}} --> P')
        for i, c in enumerate(req):
            lines.append(f'  R{i}["{_esc(c.statement)}"] --> AND')
    if alt:
        lines.append('  OR{{"ANY OF"}} --> P' if not req else '  OR{{"ANY OF"}} --> AND')
        for i, c in enumerate(alt):
            lines.append(f'  A{i}["{_esc(c.statement)}"] --> OR')
    for i, c in enumerate(c for c in p.conditions if c.role == "disqualifying"):
        lines.append(f'  D{i}["NOT: {_esc(c.statement)}"] -.-x P')
    for i, c in enumerate(c for c in p.conditions if c.role in ("optional", "uncertain")):
        lines.append(f'  O{i}["{c.role}: {_esc(c.statement)}"] -.-> P')
    return "\n".join(lines)


def write_graph(model: RiskModel, path: Path) -> None:
    lines = ["graph LR", f'  U["{model.project} {model.current_version} -> {model.target_version}"]']
    for i, p in enumerate(model.risk_paths):
        lines.append(f'  U --> P{i}["{_esc(p.path_name)} ({p.risk_level})"]')
        for j, c in enumerate(p.conditions):
            if c.category == "version":
                continue
            edge = "-.-x" if c.role == "disqualifying" else "-->"
            lines.append(f'  P{i} {edge} C{i}_{j}["{c.role}: {_esc(c.statement)}"]')
    for r in model.requires_upgrades:
        lines.append(f'  U ==> X_{r.project.replace(".", "")}["requires {r.project} {r.current_version} -> {r.target_version}"]')
    path.write_text("\n".join(lines) + "\n")


def write_report(model: RiskModel, path: Path) -> None:
    m = model
    out = [f"# {m.project} {m.current_version} → {m.target_version}: upgrade risk report", "",
           f"> {m.disclaimer}", "", m.summary, "",
           f"Overall confidence: **{m.overall_confidence}**. Validation: `{json.dumps(m.pipeline.get('validation', {}))}`", ""]
    out += ["## Risk paths", "", "| Level | Confidence | Type | Surface | Release | Path |", "|---|---|---|---|---|---|"]
    for p in m.risk_paths:
        out.append(f"| {p.risk_level} | {p.confidence} | {p.risk_type} | {p.affected_surface} | {p.introduced_in} | "
                   f"`{p.path_id}` {p.path_name} |")
    out.append("")
    for p in m.risk_paths:
        out += [f"### {p.path_name}", "", f"`{p.path_id}` · {p.risk_level} · confidence {p.confidence} · "
                f"introduced in {p.introduced_in} · fires at {p.fires_at}", "", p.description, ""]
        for c in p.conditions:
            out.append(f"- **[{c.role}] {c.category}** `{c.operator}` `{json.dumps(c.expected_value)}`: {c.statement} "
                       f"(confidence {c.confidence}{', judge ' + c.judge.verdict if c.judge else ''})")
            for e in c.evidence:
                q = e.quote or e.quote_or_summary
                out.append(f"  - {e.source_id}: \"{q}\"")
            for a in c.ambiguities:
                out.append(f"  - ⚠ {a}")
        if p.suggested_actions:
            out += ["", "Actions:"] + [f"- {a}" for a in p.suggested_actions]
        out.append("")
    es = m.evidence_summary
    out += ["## Review checklist", ""]
    lows = es.low_confidence_or_disputed_risks
    out += ["### Low confidence or disputed", ""] + [f"- [ ] {x}" for x in lows] + [""]
    inferred = [f"{p.path_id}: {c.statement}" for p in m.risk_paths for c in p.conditions if c.derived_by == "inference"]
    out += ["### Inferred conditions", ""] + [f"- [ ] {x}" for x in inferred] + [""]
    out += ["### Source disagreements", ""] + [f"- {d.topic}: {d.detail} → {d.resolution}" for d in es.sources_with_disagreements] + [""]
    out += ["### Open questions", ""] + [f"- {q}" for q in m.open_questions] + [""]
    out += ["## Context facts (not risks)", ""] + [f"- ({c.introduced_in}) {c.statement} — _{c.why_not_risk}_" for c in m.context_facts] + [""]
    out += ["## Disqualified candidates", ""] + [f"- {d.statement}: {d.reason}" for d in m.disqualified_candidates] + [""]
    out += ["## Sources", "", "| Source | Type | Tier | Status | Pinned ref |", "|---|---|---|---|---|"]
    for s in m.source_inventory:
        out.append(f"| [{s.source_id}]({s.url}) | {s.source_type} | {s.authority_tier} | {s.status}"
                   f"{' (' + s.rejection_reason + ')' if s.rejection_reason else ''} | `{s.pinned_ref}` |")
    out += ["", "## What we trusted and what we did not", "",
            "- Trusted: package metadata for version numbers; official guides, release notes and changelogs pinned to a tag, branch or commit.",
            "- Not trusted: LLM self-reported confidence, unpinned current pages when they disagree with pinned ones, any quote that fails exact match, transclusion stubs.",
            ""]
    path.write_text("\n".join(out))
