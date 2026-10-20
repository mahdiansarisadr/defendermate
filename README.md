# URX: LLM-based upgrade risk extraction

URX reads public release notes, migration guides, changelogs, deprecation guides and package metadata for an open-source upgrade. It produces a structured, evidence-grounded **upgrade risk model**. Every risk path has at least one version condition and one checkable application- or deployment-side condition. Every condition quotes a pinned source verbatim, and the validator re-checks each quote against the cached file before anything is written.

> Documentation-derived risk conditions; not a migration plan.
> (This disclaimer is in every output. Nothing here was run against a real codebase or deployment.)

Upgrades covered: Django 3.2→4.2, React 17→18, Kubernetes 1.23→1.29, PostgreSQL 13→16, Next.js 12→14.

The design is in [`TDD.md`](TDD.md); section 17 lists the gaps found while building it. The ten design questions are answered in [`DESIGN_NOTE.md`](DESIGN_NOTE.md). Eval results are in [`eval/results.md`](eval/results.md).

## Results

| Upgrade | Paths | Context facts | Gold recall | Validator errors | Strong model | LLM cost to produce |
|---|---|---|---|---|---|---|
| Django 3.2→4.2 | 151 | 126 | 36/36 | 0 | Sonnet 5.5 | ~$7.33 |
| React 17→18 | 25 | 39 | 14/15 | 0 | Sonnet 5.5 | ~$1.70 |
| Kubernetes 1.23→1.29 | 83 | 48 | 30/30 | 0 | Haiku 5.5 | ~$2.21 |
| PostgreSQL 13→16 | 69 | 8 | 27/28 | 0 | Haiku 5.5 | ~$1.38 |
| Next.js 12→14 | 19 | 1 | 12/12 | 0 | Haiku 5.5 | ~$0.40 |

Costs are estimates from token counts; the LLM evals added about $3–5.

Kubernetes, PostgreSQL and Next.js were extracted with Haiku as the strong model, after the API credit ran out mid-run. Each model records the models it used in `pipeline.models`, and offline replay uses those recorded models.

Eval summary (full table in [`eval/results.md`](eval/results.md); hard gates are asserted in `tests/test_eval_gates.py`):

| Metric | Result | Target |
|---|---|---|
| Grounding (quotes verified against cache) | 1384/1384 | 1.00, hard |
| Validator errors | 0 | 0, hard |
| Structural completeness | 347/347 | 1.00, hard |
| Recall per upgrade (min) / overall | 0.93 / 0.98 | ≥0.80 / ≥0.85, hard |
| Classification (risk / context / disqualified) | 0.97 | ≥0.85, hard |
| Field consistency | 0.996 | ≥0.95, hard |
| Drift false-accept, exact matching (fuzzy 0.9 shown for contrast) | 0.00 (fuzzy 1.00) | 0, hard |
| Estimated precision (gold match or precision judge) | 0.97 | ≥0.85, soft |
| Strict precision (gold matches only; lower bound) | 0.48 | report |
| Level agreement | 0.99 | ≥0.80, soft |
| Calibration: valid rate for high ≥ medium ≥ low | 0.99 ≥ 0.96 ≥ 0.94 | monotone, soft |
| Judge accuracy and κ on synthetic pairs | 1.00, 1.00 (41 pairs) | ≥0.90, κ≥0.8, soft |
| **Stability** (path-ID Jaccard, cold React rerun) | **0.70** | ≥0.80, soft: **missed** |

How to read these numbers:

- **Stability** is the one missed target. Path IDs are hashed from the primary symbol the model picks, so a cold run that names the same risk differently gets a new ID. Gold recall moved from 0.93 to 0.87 between the two runs.
- **Calibration** is monotone but weakly separated. Almost every path is judged valid, so the confidence bands mostly reflect evidence strength, not validity.
- **The judge set** is synthetic and easy (identity claims versus mutated claims), so it shows the judge isn't broken. It does not show real-world entailment accuracy.
- **The single-prompt ablation**, run over the same windowed change items, reaches similar gold recall. Its quotes ground, but it has no conditions, roles, version ranges or search queries, and no revert, supersession or remediation handling. What the decomposition buys is structure and composition, not raw recall.

## Quick start (offline, no API key)

The source cache (`cache/`) and the LLM response cache (`llm_cache/`) are committed, so every committed output can be reproduced with no network access and no key.

```bash
uv venv --python 3.12 && source .venv/bin/activate
uv pip install -e '.[dev]'

python extract_upgrade_risks.py --project Django --current-version 3.2 --target-version 4.2 --offline
urx extract --all --offline        # all five
urx validate outputs/django_3.2_to_4.2/risk_model.json
urx eval --no-llm                  # deterministic metrics -> eval/results.{json,md}
pytest -q                          # unit, adversarial, e2e replay, eval gates, server
```

## UI

```bash
cd ui && npm install && npm run build && cd ..
urx serve                          # http://127.0.0.1:8765
```

- **Overview**: one card per upgrade, showing risk counts by level, overall confidence, gold recall, validator errors, sources and cost.
- **Upgrade**: risk paths with level, type, release, confidence and flag filters. The path drawer shows:
  - conditions grouped by role (required, alternative, uncertain), with operator, expected value, confidence, judge verdict and ripgrep search queries
  - verbatim evidence with a **show in source** view that highlights the quote inside the cached document
  - suggested actions, a Mermaid condition graph, and Accept/Reject review buttons, which write to `review/overrides.yaml`

  Other tabs cover sources (used or rejected, pinned ref, hash), the evidence summary with disagreements and open questions, context facts and disqualified candidates, the pipeline (funnel, judge stats, LLM usage per stage, timings, rejected drafts, run log) and the Markdown report.
- **Evals**: every TDD 17.4 metric with its target and gate type, plus the per-gold-item hit and miss list linking to the matched paths.
- **Runs**: start an online or offline run and follow its stage events live.

For UI development, run `cd ui && npm run dev`, which proxies `/api` to port 8765.

## Online runs

Add `ANTHROPIC_API_KEY=...` to `.env` (gitignored) and drop `--offline`. Network fetches and model calls happen only for content that isn't cached.

| Variable | Default | Purpose |
|---|---|---|
| `URX_PROVIDER` | `anthropic` | `anthropic` or `openai` (`pip install -e '.[openai]'`, `OPENAI_API_KEY`) |
| `URX_CHEAP_MODEL` | `claude-haiku-5-5` | triage, precision judge |
| `URX_STRONG_MODEL` | `claude-sonnet-5-5` | extraction, revert reconcile, grounding judge |

`urx eval` with no flags also runs the LLM-based metrics (precision judge and judge calibration). Add `--ablations` for the single-prompt baseline and the filter ablations, and `--stability` for a cold React rerun.

## Other commands

```bash
urx scan --model outputs/django_3.2_to_4.2/risk_model.json --repo fixtures/demo_app
urx report outputs/django_3.2_to_4.2
urx export-schema                  # schemas/risk_model.schema.json
```

`urx scan` is a small demo of a downstream consumer. It runs each condition's ripgrep queries and reports which paths fire. It refuses any directory outside `fixtures/`. `fixtures/demo_app` is a synthetic Django 3.2 app with planted usages; all of them fire, and the `urlquote` control does not.

## Outputs

`outputs/<project>_<cur>_to_<tgt>/` contains:

| File | Content |
|---|---|
| `risk_model.json` | The final model: the assignment schema plus additive fields (`role`, `derived_by`, `search_queries`, `judge`, `context_facts`, `disqualified_candidates`, `requires_upgrades`, `plan`, `pipeline`) |
| `source_inventory.json` | Every source with type, authority tier, pinned ref, content hash, and used or rejected status with a reason |
| `report.md`, `graph.mmd` | Human-readable report and Mermaid graph |
| `run_log.jsonl` | Stage events, timings, token usage and cost estimates |
| `intermediate/` | `items` (parsed change items), `triage`, `triage_disagreements`, `extractions`, `release_risks` (linked), `revert_candidates`, `version_facts`, `rejected` (every dropped draft or evidence item with a reason), `compose_log.json`, `validation.json` |

## Pipeline in one paragraph

A per-project registry YAML lists the official sources, their formats, the sections to mine and the known release list. The fetcher pins each source to a tag or commit, hashes it and detects transclusion stubs. Format adapters (RST, Markdown/MDX, DocBook, JSON) turn documents into blocks, and blocks into atomic change items (one bullet is one item), each tagged with its release. The cheap model triages every item into risk, context or noise, and a strong-model recall sweep re-checks noise items that contain signal words. The strong model extracts paths from risk items under a JSON schema, and quotes are verified immediately, with one repair round. A BM25 linker merges duplicates across sources. Deterministic composition rules then handle reverts, supersession, the Kubernetes remediation chain, release filtering, start-version applicability, future-removal context, and cross-project requirements. Rule-derived paths come from package metadata (Python, Node and React peer ranges). An LLM judge checks entailment for each condition: a claim it finds unsupported is demoted to `uncertain`. A deterministic rubric sets confidence. Finally, a deterministic validator (E1–E11 and W1–W4) repairs the model or blocks it from being written.

## What I trusted, what I did not

**Trusted, in order:** package registry metadata (JSON-path evidence) > official deprecation and migration guides > official release notes and changelogs. Tier-2 and tier-3 sources were not used for evidence.

**Not trusted:**
- the LLM's own confidence (confidence is rubric-only)
- unpinned "latest" docs (everything is pinned to a tag or commit)
- search snippets
- any quote that fails exact match after normalization (fuzzy matching accepted 100% of injected one-number drifts in the drift test, exact matching accepted 0%)
- LLM-written disqualifier queries in the scan demo

## Assumptions and limitations

- **Policy:** something that is only deprecated in the target, and still works there, is context, not a risk, unless the docs describe a behavior change. Two gold items sit on this boundary and disagree with the pipeline: `index_together` (gold says context, extracted as a risk) and `renderToNodeStream` (gold says risk, extracted as context). The gold was committed before extraction and was not edited afterwards.
- **Coverage gaps** (also listed as `open_questions` in each model):
  - Kubernetes "API Change" and "Feature" sections are not mined.
  - Next.js minor-release notes and GitHub issues are not mined.
  - Ecosystem risks are out of scope: `@types/react`, PostgreSQL extensions, drivers, managed-service behavior, and third-party packages pinned to old versions.
- **Strict precision is a lower bound:** gold sets are small and not exhaustive. Estimated precision adds an LLM precision judge. Both are reported.
- **Determinism:** current models reject `temperature`, so replays are deterministic only through the cache. Cold-run stability is measured, not assumed (TDD G27).
- **Cut for the time budget:** discovery agent, Ollama provider, dense retrieval, mining tier-2 issue trackers, and the Postgres/pgvector linker. BM25 runs in process instead (TDD G22, G25).

## Where it can fail

- An adapter drops entities in a new format, so quotes verify against broken text. Each adapter has golden-sentence tests.
- Docs edited retroactively. Mitigated by tag and commit pinning and content hashes.
- Gates or scopes the docs only imply, such as React behaviors that apply only under Strict Mode or `createRoot`. These are marked `uncertain` with an ambiguity rather than asserted.
- A revert whose original change was never extracted as a risk. It is recorded as a disqualified candidate quoting the revert note (TDD G29).
- Over- or under-merging in the linker. The merge log is in `intermediate/compose_log.json`.

## Constraints respected

Public documentation only. No issues or comments were filed upstream. No private or real repositories were analyzed: `scan` is hard-limited to `fixtures/`. Every output states that it is not a migration plan.
