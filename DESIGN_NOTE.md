# Design note

URX turns public upgrade documentation into a structured risk model in which every condition is backed by a verbatim, re-verified quote. The full design is in [`TDD.md`](TDD.md); this note answers the ten required questions.

### 1. How did you decompose the extraction problem into workflow stages or agents?

There are three pipelines with narrow contracts. Each stage writes its own artifact to `outputs/<upgrade>/intermediate/`.

1. **Ingestion (deterministic).** A per-project registry lists the official sources. They are fetched, pinned to a tag or commit, and hashed, and stubs are rejected. Format adapters (RST, Markdown/MDX, DocBook, JSON) split each document into release-tagged *atomic change items*, one bullet per item, with their heading path and parent section. Exact duplicates across sources are merged. Package metadata becomes version facts.
2. **Per-release extraction (LLM).** The cheap model triages every item as risk, context or noise. A strong-model recall sweep re-checks noise items that contain signal words. The strong model extracts risk paths from risk items under a JSON schema, and each quote is verified immediately, with one repair round. A BM25 linker merges the same risk reported by several sources.
3. **Composition and checking (mostly deterministic).** A planner picks the releases crossed. Rules R1–R7 handle reverts, supersession, the Kubernetes remediation chain, release filtering, start-version applicability, future-removal context and cross-project requirements. Then an LLM judge checks each condition, a rubric sets confidence, and a validator repairs or blocks the model. Reports, the graph and the evidence summary are generated last.

### 2. What role did the LLM play?

Five bounded jobs, each with a versioned prompt in `prompts/` and a strict output schema:

- triage (cheap tier, batches of 20)
- the recall sweep
- path extraction
- linking a revert note to the change it undoes
- an entailment judge for each condition

The eval adds a precision judge and a single-prompt baseline. The LLM never parses documents, does version math, assigns confidence, or validates output. Models are set by tier (`URX_CHEAP_MODEL`, `URX_STRONG_MODEL`), and both Anthropic and OpenAI providers are supported.

### 3. What parts of the pipeline are deterministic?

Everything else is deterministic:

- fetching, pinning, hashing, parsing, item splitting, release tagging and deduplication
- version-range canonicalization, and paths derived from package metadata
- composition rules R1–R7
- the confidence rubric and the validator (E1–E11 errors, W1–W4 warnings)
- summaries, open questions, overall confidence and reports

### 4. How did you prevent hallucinated upgrade risks?

- **Quotes must exist.** Each condition needs evidence whose quote matches the pinned cached source exactly after Unicode and whitespace normalization. This is checked at extraction and again by the final validator, which blocks the write on failure. In the drift test, fuzzy matching at a 0.9 ratio accepted 100% of quotes with one number changed; exact matching accepted 0%.
- **Numbers come from metadata.** Version minimums use JSON-path evidence re-read from registry metadata.
- **Structure is enforced.** A path is dropped unless it has a version condition and an app- or deployment-side condition.
- **Unsupported claims are demoted.** The judge marks unsupported conditions `uncertain`, and the extractor is told to use `uncertain` with an explicit ambiguity rather than guess.
- **Confidence comes from the rubric, not the model.** It uses authority tier, corroboration, metadata agreement and judge verdict, with penalties for inference and ambiguity. Inferred conditions are capped below `high`.
- **Every drop is logged** with a reason in `rejected.jsonl`.

### 5. How did you decide whether something is a real risk condition versus useful context?

A **risk** needs a version-side change *and* a checkable condition on the application or deployment. For example, the app imports `force_text`, a manifest uses `flowcontrol.apiserver.k8s.io/v1beta2`, or the database relies on implicit `CREATE` on `public`.

True statements that need no action at the target become `context_facts` with a `why_not_risk`. These include deprecated-but-working APIs, additive features, background, and removals scheduled after the target.

Changes that were reverted, or superseded before the target, become `disqualified_candidates` with the quote that disqualifies them. The eval checks this three-way split against gold, with 0.97 classification accuracy.

### 6. How did you handle conflicting or incomplete public documentation?

- **Authority order:** registry metadata > deprecation and migration guides > release notes and changelogs. Third-party sources are not used as evidence.
- **Disagreements are recorded, not resolved silently.** A prose version that disagrees with metadata, or with another release's note, goes to `sources_with_disagreements` with a resolution. Example: Next.js Node minimums of 14.6, 16.8 and 16.14 across 13.0, 13.4 and 13.5.
- **Changes over time:** reverts found in patch notes (R1), supersession that keeps the last state (R2), and Kubernetes remediation recomputed against the target (R3), because per-release advice can point to APIs removed later.
- **Gaps are surfaced.** Missing coverage, rejected sources and unresolved reverts become `open_questions`. Conditions implied but not stated are kept as `uncertain` with the ambiguity spelled out.

### 7. How would you scale this from these upgrades to thousands of projects and versions?

- **Registries are configuration,** and most projects fit the four adapters. The next step is a bounded discovery agent that proposes registry entries for a human to approve.
- **Extraction is organized per release** and composition is deterministic, so any (current, target) pair is assembled from per-release risks. To make the *cost* per-release as well, two changes are needed:
  - drop the upgrade pair from the triage and extraction prompts, which today makes the LLM cache key pair-specific
  - store per-release results keyed by content hash, so unchanged docs skip parsing and LLM work entirely
- **Model tier is a dial.** In the experiment, Haiku for both tiers cost 1/12 as much as Haiku plus Sonnet, for one fewer gold risk out of 55.
- **Infrastructure:** a work queue, a blob store for caches, and per-ecosystem adapters (PyPI, npm, Go).

### 8. How would you evaluate precision and recall of extracted risks?

Small gold sets for all five upgrades were committed *before* the first extraction. They are matched with term groups and a release filter.

- **Hard gates (pytest):**
  - grounding 1.00
  - 0 validator errors
  - structural completeness 1.00
  - recall ≥ 0.80 per upgrade and ≥ 0.85 overall (actual: 0.93 and 0.98)
  - classification ≥ 0.85
  - field consistency ≥ 0.95
  - 0 drift false-accepts
- **Soft targets:**
  - estimated precision ≥ 0.85, using a gold match or an LLM precision judge (actual 0.97)
  - level agreement and calibration
  - judge accuracy
  - cold-rerun stability ≥ 0.80. This was missed at 0.70, because path IDs depend on the symbol the model picks.
- **Reported:** strict precision, a lower bound because gold isn't exhaustive. Also ablations against a single-prompt baseline, and a cost/quality experiment across model pairs.

### 9. What would you improve with more time?

- Make prompts independent of the upgrade pair, and add the per-release, content-hash-keyed store (see 7).
- Derive path IDs from source items, so stability measures real drift.
- Mine Kubernetes "API Change" sections, Next.js minor releases and issue trackers (as tier-2 evidence for known incompatibilities).
- Add ecosystem sources: type packages, PostgreSQL extensions, drivers.
- Build a human-labeled judge set, and feed UI review decisions back into gold.
- Add dense retrieval for the linker, and a discovery agent.

### 10. How would this output be consumed by a downstream upgrade assessment engine?

Each condition is machine-checkable:

- **category and operator,** for example `present`, `absent`, `in_range`
- **expected value:** a canonical version range such as `{"current_version": "< 4.0", "target_version": ">= 4.0"}`, a symbol, or a JSON-path fact
- **role:** `required`, `alternative`, `optional`, `disqualifying` or `uncertain`
- **search queries** for ripgrep, `kubectl` or SQL

An engine first evaluates the version conditions against the planned upgrade, honoring `applies_to.from_versions`. It then runs the app-side queries against a repo or cluster and reports the paths that fire, ranked by `risk_level` and `confidence`. `urx scan` demonstrates this on a synthetic app, where all planted usages fire and the control does not. Paths whose disqualifiers also match are marked `needs_review`, not suppressed. The output is evidence for an assessment, not a migration plan.

*What I trusted, what I did not, and where the workflow can fail are listed in the README.*
