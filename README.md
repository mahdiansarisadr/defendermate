# URX: LLM-based upgrade risk extraction

URX reads public release notes, migration guides, changelogs, deprecation guides and package metadata for an open-source upgrade. It produces a structured, evidence-grounded **upgrade risk model**. Every risk path has at least one version condition and one checkable application- or deployment-side condition. Every condition quotes a pinned source verbatim, and the validator re-checks each quote against the cached file before anything is written.

> Documentation-derived risk conditions; not a migration plan.
> (This disclaimer is in every output. Nothing here was run against a real codebase or deployment.)

Upgrades covered: Django 3.2→4.2, React 17→18, Kubernetes 1.23→1.29, PostgreSQL 13→16, Next.js 12→14.

The required design note, answering the ten questions, is `[DESIGN_NOTE.md](DESIGN_NOTE.md)`. The full design is in `[TDD.md](TDD.md)`; section 17 lists the gaps found while building it. Eval results are in `[eval/results.md](eval/results.md)`.

## Design overview

```mermaid
flowchart LR
  R[Registry YAML<br/>official sources] --> F[Fetch, pin, hash]
  F --> P[Parse into atomic<br/>change items + dedup]
  P --> T[Triage<br/>LLM cheap]
  T --> S[Recall sweep<br/>LLM strong]
  S --> X[Extract paths<br/>LLM strong + quote check]
  X --> L[Link duplicates<br/>BM25]
  L --> C[Compose rules R1–R7<br/>reverts, supersession, ranges]
  C --> J[Judge each condition<br/>LLM strong]
  J --> Q[Confidence rubric]
  Q --> V[Validator<br/>repair or block]
  V --> O[risk_model.json<br/>inventory, report, graph]
```




| Stage               | LLM?        | What it does                                                                                                                                                                                                                           |
| ------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source gathering    | no          | The per-project registry lists official sources by type and authority tier. The fetcher pins each to a tag or commit, records a SHA-256 hash, rejects stubs and caches it.                                                             |
| Document processing | no          | Adapters (RST, Markdown/MDX, DocBook, JSON) split documents into release-tagged change items (one bullet each) with heading path and section type. Exact duplicates across sources are merged. Package metadata becomes version facts. |
| Triage              | cheap       | Labels each item risk, context or noise. A strong-model sweep re-checks noise items that contain signal words.                                                                                                                         |
| Extraction          | strong      | Builds risk paths with typed conditions, roles, verbatim quotes and search queries under a JSON schema. Unverifiable quotes get one repair round.                                                                                      |
| Composition         | no          | Links duplicates across sources, then applies rules for reverts, supersession, Kubernetes remediation, release filtering, applicability and cross-project requirements. Separates risks, context facts and disqualified candidates.    |
| Checking            | strong + no | The LLM judge checks each condition against its quotes and demotes unsupported ones to `uncertain`. A deterministic rubric sets confidence, and the validator (E1–E11, W1–W4) repairs the model or blocks the write.                   |


Key choices:

- **The LLM never does the following:**
  - parse documents
  - do version math
  - set confidence
  - validate output
- **Every quote is re-verified** against the pinned cached file.
- **Risk versus context:** a risk needs both a version-side change and a checkable app- or deployment-side condition. Everything else true becomes context.

## Results


| Upgrade              | Paths | Context facts | Gold recall | Validator errors | Strong model | LLM cost to produce |
| -------------------- | ----- | ------------- | ----------- | ---------------- | ------------ | ------------------- |
| Django 3.2→4.2       | 151   | 126           | 36/36       | 0                | Sonnet 5.5   | ~$4.74              |
| React 17→18          | 25    | 39            | 14/15       | 0                | Sonnet 5.5   | ~$1.08              |
| Kubernetes 1.23→1.29 | 83    | 48            | 30/30       | 0                | Haiku 5.5    | ~$0.22              |
| PostgreSQL 13→16     | 69    | 8             | 27/28       | 0                | Haiku 5.5    | ~$0.14              |
| Next.js 12→14        | 19    | 1             | 12/12       | 0                | Haiku 5.5    | ~$0.04              |


Costs are list-price estimates (Anthropic pricing page, 2026-10-20) applied to recorded token counts. Prompt-caching discounts are not modeled.

Kubernetes, PostgreSQL and Next.js were extracted with Haiku as the strong model, after the API credit ran out mid-run. Each model records the models it used in `pipeline.models`, and offline replay uses those recorded models.

Eval summary (full table in `[eval/results.md](eval/results.md)`; hard gates are asserted in `tests/test_eval_gates.py`):


| Metric                                                            | Result                | Target                  |
| ----------------------------------------------------------------- | --------------------- | ----------------------- |
| Grounding (quotes verified against cache)                         | 1384/1384             | 1.00, hard              |
| Validator errors                                                  | 0                     | 0, hard                 |
| Structural completeness                                           | 347/347               | 1.00, hard              |
| Recall per upgrade (min) / overall                                | 0.93 / 0.98           | ≥0.80 / ≥0.85, hard     |
| Classification (risk / context / disqualified)                    | 0.97                  | ≥0.85, hard             |
| Field consistency                                                 | 0.996                 | ≥0.95, hard             |
| Drift false-accept, exact matching (fuzzy 0.9 shown for contrast) | 0.00 (fuzzy 1.00)     | 0, hard                 |
| Estimated precision (gold match or precision judge)               | 0.97                  | ≥0.85, soft             |
| Strict precision (gold matches only; lower bound)                 | 0.48                  | report                  |
| Level agreement                                                   | 0.99                  | ≥0.80, soft             |
| Calibration: valid rate for high ≥ medium ≥ low                   | 0.99 ≥ 0.96 ≥ 0.94    | monotone, soft          |
| Judge accuracy and κ on synthetic pairs                           | 1.00, 1.00 (41 pairs) | ≥0.90, κ≥0.8, soft      |
| **Stability** (path-ID Jaccard, cold React rerun)                 | **0.70**              | ≥0.80, soft: **missed** |


How to read these numbers:

- **Stability** is the one missed target. Path IDs are hashed from the primary symbol the model picks, so a cold run that names the same risk differently gets a new ID. Gold recall moved from 0.93 to 0.87 between the two runs.
- **Calibration** is monotone but weakly separated. Almost every path is judged valid, so the confidence bands mostly reflect evidence strength, not validity.
- **The judge set** is synthetic and easy (identity claims versus mutated claims), so it shows the judge isn't broken. It does not show real-world entailment accuracy.
- **The single-prompt ablation**, run over the same windowed change items, reaches similar gold recall. Its quotes ground, but it has no conditions, roles, version ranges or search queries, and no revert, supersession or remediation handling. What the decomposition buys is structure and composition, not raw recall.

## Model experiment: quality vs cost

The same pipeline ran on React, PostgreSQL and Next.js under three cheap/strong model pairs. The cheap tier does triage; the strong tier does extraction, the recall sweep, revert reconcile and the grounding judge. Every config is scored against the same gold sets (55 gold risks) by the same Sonnet 5.5 precision judge, and judge calibration uses the same claim set for every config. Full results are in `[experiments/comparison.md](experiments/comparison.md)` and on the UI's **Experiments** page, which plots quality against cost with the Pareto frontier.


| Config (cheap / strong) | Cost to produce | × cheapest | Paths | Gold recall | Est. precision | F1    | Classification | Stability |
| ----------------------- | --------------- | ---------- | ----- | ----------- | -------------- | ----- | -------------- | --------- |
| Haiku / Haiku           | $0.27           | 1×         | 115   | 53/55       | 99.1%          | 0.977 | 96.5%          | 0.74      |
| Haiku / Sonnet          | $3.25           | 12×        | 110   | 54/55       | 99.1%          | 0.986 | 98.2%          | 0.70      |
| Sonnet / Opus           | $7.65           | 28×        | 123   | 55/55       | 98.4%          | 0.992 | 100%           | 0.62      |


All three pass the hard gates: 100% grounding and 0 validator errors.

**Trade-off.** Haiku / Sonnet costs 12× as much as Haiku / Haiku and finds one more gold risk (PostgreSQL `ssl_compression`). Sonnet / Opus costs 28× as much and finds two more (that one, plus React `renderToNodeStream`). On F1 that is about $3.3 per F1 point (0.01 F1) from Haiku / Haiku to Haiku / Sonnet, and about $7.3 per point from Haiku / Sonnet to Sonnet / Opus. Every config sits on the frontier: each extra dollar buys a little more recall, with fast-diminishing returns.

Caveats:

- The differences are one or two gold items out of 55, which is within noise for a set this small.
- Estimated precision is near the ceiling for every config, so it doesn't separate them.
- The judge-calibration set is saturated (1.00 for every config).
- Stability (path-ID overlap) *drops* as the models get stronger. Stronger models emit more, and differently named, paths, and the metric penalizes renaming. It is not a reliability signal on its own.

What this suggests: Haiku / Haiku for bulk or first-pass coverage, and a stronger strong tier only where the last few percent of recall matters. This is in line with the design choice that grounding and structure come from the deterministic stages, not the model.

```bash
urx experiment --config haiku_haiku     # also haiku_sonnet, sonnet_opus; writes experiments/<config>/
urx compare-experiments                 # experiments/comparison.{json,md}
```

## Quick start

You don't need an API key or network access. The fetched sources (`cache/`) and every LLM response (`llm_cache/`) are committed, so the steps below replay the committed outputs exactly and cost nothing.

**Prerequisites:**

- Python 3.11 or newer. [uv](https://docs.astral.sh/uv/) is recommended; plain `pip` works too.
- Node 20 or newer, only for the UI.
- [ripgrep](https://github.com/BurntSushi/ripgrep), only for the `urx scan` demo.

### 1. Install 

```bash
uv venv --python 3.12 && source .venv/bin/activate
uv pip install -e '.[dev]'
# without uv: python3 -m venv .venv && source .venv/bin/activate && pip install -e '.[dev]'
```

This installs the `urx` command. `extract_upgrade_risks.py` is the same CLI under the name the assignment uses.

### 2. Reproduce an upgrade 

```bash
python extract_upgrade_risks.py --project Django --current-version 3.2 --target-version 4.2 --offline
```

Expected output: `Django 3.2->4.2: 151 paths, overall medium, errors=0 warnings=7, ~$0.00`.

The results go to `outputs/django_3.2_to_4.2/`. Start with `report.md` for a readable summary; `risk_model.json` is the machine-readable model.

To reproduce all five upgrades:

```bash
urx extract --all --offline
```

### 3. Browse the results in the UI

```bash
(cd ui && npm install && npm run build)
urx serve                          # open http://127.0.0.1:8765
```

Pick an upgrade in the sidebar and click any risk path. The drawer shows its conditions, the verbatim evidence (with **show in source**) and the condition graph. If port 8765 is taken, use `urx serve --port 8800`.

### 4. Check quality

```bash
pytest -q                          # 79 tests: unit, adversarial validator, offline end-to-end, eval gates, API
urx validate outputs/django_3.2_to_4.2/risk_model.json   # exit code 1 on any validator error
urx eval --no-llm                  # recompute deterministic metrics -> eval/results.md
```

### 5. Try the downstream consumer demo

```bash
urx scan --model outputs/django_3.2_to_4.2/risk_model.json --repo fixtures/demo_app
```

This runs each condition's search queries against a synthetic Django 3.2 app and lists the risk paths that fire. It only runs inside `fixtures/`.

### 6. Run online 

```bash
echo 'ANTHROPIC_API_KEY=sk-ant-...' > .env       # gitignored
python extract_upgrade_risks.py --project React --current-version 17 --target-version 18
```

Online runs only fetch documents and call the model for content that isn't already cached. Each run prints its estimated cost; per-upgrade costs are in the Results table above. Model choices are under [Online runs](#online-runs).


|     |
| --- |
|     |


## UI

The UI is described here in more detail; to start it, see [Quick start](#quick-start), step 3. A left sidebar links to every upgrade and page.

- **Overview**: headline numbers, then one row per upgrade with its risk mix, path count, gold recall, estimated precision and confidence, followed by a legend of the risk levels.
- **Upgrade**: risk paths with search and level filters; confidence, type, release and flag filters sit under "More filters". The path drawer shows:
  - conditions grouped by role (required, alternative, uncertain), with operator, expected value, confidence, judge verdict and ripgrep search queries
  - verbatim evidence with a **show in source** view that highlights the quote inside the cached document
  - suggested actions, a Mermaid condition graph, and Accept/Reject review buttons, which write to `review/overrides.yaml`
  Other tabs cover sources (used or rejected, pinned ref, hash), the evidence summary with disagreements and open questions, context facts and disqualified candidates, the pipeline (funnel, judge stats, LLM usage per stage, timings, rejected drafts, run log) and the Markdown report.
- **Evals**: every metric grouped into hard gates, soft targets and informational, plus the per-gold-item hit and miss list for each upgrade.
- **Experiments**: quality versus cost for each model pair, with the Pareto frontier, the trade-off, and summary, all-metric and per-upgrade tables.
- **Runs**: start an online or offline run and follow its stage events live.

For UI development, run `cd ui && npm run dev`, which proxies `/api` to port 8765.



