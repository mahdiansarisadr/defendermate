# Design note

**1. Decomposition.** The work runs as three pipelines with narrow contracts, and each stage writes its own artifact.

- **Ingestion** is deterministic. The registry lists sources, then come fetch and pin, format adapters, release-tagged atomic change items, and version facts from package metadata.
- **Per-release extraction** uses the LLM. Every item is triaged, and a recall sweep re-checks items labeled noise that contain signal words. Paths are extracted under a JSON schema, then the linker merges duplicates across sources.
- **Composition and serving** is mostly deterministic. A planner picks the releases crossed. Rules R1–R7 handle reverts, supersession, the Kubernetes remediation chain, release filtering, start-version applicability, future-removal context and cross-project requirements. After that come the LLM judge, the rubric, the validator and the reports.

Extraction runs once per release, not once per upgrade pair. Any (current, target) pair is composed from the per-release risks.

**2. Role of the LLM.**

- Triage (cheap model, batches of 20).
- Path extraction (strong model, schema-constrained, prompted to quote verbatim).
- Linking a revert note to the change it reverts (reconcile).
- Entailment judging of each condition against its quotes.
- In eval only: a precision judge and a single-prompt baseline.

The LLM never parses documents, does version math, sets confidence or validates output.

**3. Deterministic parts.** Fetching, pinning and hashing, stub detection, parsing, normalization, item splitting, symbol extraction, release assignment, planning, version-condition canonicalization, rule-derived metadata paths, composition rules, the confidence rubric, the validator and repair, summary, evidence summary, open questions, overall confidence, reports and the scan demo.

**4. Preventing hallucinated risks.**

- Every condition needs evidence. A quote must match the pinned cached source exactly after Unicode normalization. It is checked at extraction (one repair round) and again by the final validator.
- Version facts use JSON-path evidence with the expected value, re-read from the registry JSON.
- The judge demotes unsupported claims to `uncertain`.
- A path is dropped unless it has both a version condition and an app-side condition.
- Confidence comes from a rubric, never from the model: authority tier, independent corroboration, metadata agreement, penalties for inference and ambiguity, and a cap so inferred conditions are never high.
- Every drop is logged in `intermediate/rejected.jsonl`.
- In the drift test, exact matching accepted 0% of quotes with one injected number change; fuzzy matching at a 0.9 ratio accepted 100%.

**5. Risk versus context.** A risk needs a version-side change *and* a checkable condition on the application or deployment under which it matters. Examples: the app imports `force_text`, a manifest uses `flowcontrol.apiserver.k8s.io/v1beta2`, or the database relies on implicit `public` schema CREATE. Other true statements become `context_facts` with a `why_not_risk` reason. That covers deprecations that still work, background, and removals that land after the target. Reverted changes, and removals superseded before the target, become `disqualified_candidates` with the quote that disqualifies them.

**6. Conflicting or incomplete documentation.**

- **Trust order:** registry metadata > deprecation and migration guides > release notes. A prose version that contradicts metadata goes to `sources_with_disagreements` with a resolution. Example: Next.js Node minimums of 14.6, 16.8 and 16.14 across 13.0, 13.4 and 13.5.
- **Reverts** (R1) are found by scanning patch notes. **Supersession** (R2) keeps the last state.
- **Kubernetes remediation** (R3) is recomputed against the target, because per-release guidance can name APIs that are themselves removed later.
- **Undocumented areas, rejected sources and unresolved reconciles** become `open_questions`. These include registry coverage gaps such as unmined Kubernetes sections and ecosystem packages.
- **Implied-only gates** are marked `uncertain` with the ambiguity spelled out.

**7. Scaling to thousands of projects.**

- **Configuration:** the registry is configuration, and most projects fit the four adapters.
- **Cost:** extraction is per release and cached, so cost grows with the number of releases, not with the number of upgrade pairs. A new release triggers one batch job. Composing any pair is deterministic and cheap.
- **Registries:** generating registries is the next step. A bounded discovery agent would propose sources, and a human would approve them.
- **Throughput:** batching, worker pools, the response cache and per-stage cost logs keep spend visible. At this scale I would add a queue, a blob store for the caches, and per-ecosystem adapters (PyPI, npm, Go modules).

**8. Evaluating precision and recall.** Small gold sets were written for all five upgrades *before* the first extraction and committed separately. Gold items use term-group (DNF) matching with a release filter. Metrics are split into hard gates and soft targets.

- **Hard gates, asserted in pytest:**
  - grounding 1.00
  - validator errors 0
  - structural completeness 1.00
  - recall ≥ 0.80 per upgrade and ≥ 0.85 overall
  - classification ≥ 0.85
  - field consistency ≥ 0.95
  - drift false-accept 0
- **Soft targets:**
  - estimated precision (gold match or precision judge) ≥ 0.85
  - level agreement ≥ 0.80
  - calibration monotone
  - judge accuracy ≥ 0.90 and κ ≥ 0.8 on a synthetic supported-versus-mutated set
  - cold-rerun stability ≥ 0.80
- **Reported only:** strict precision, which is a lower bound because gold sets are not exhaustive.
- **Ablations:** compare against a single-prompt baseline, and against heading or keyword pre-filters instead of LLM triage.

Results are in `eval/results.md` and on the UI's Evals page.

**9. With more time.**

- Mine Kubernetes "API Change" and "Feature" sections, Next.js minor releases, and issue trackers, the last as tier-2 evidence for known incompatibilities.
- Add ecosystem sources: type packages, PostgreSQL extensions, drivers.
- Build a human-labeled judge set and feed review overrides back into the gold.
- Use dense retrieval for the linker and add more adapters.
- Make cold runs reproducible by seeding the response cache from a reviewed baseline.

**10. Downstream consumption.** Each condition carries:

- a category and an operator (`present`, `absent`, `in_range` and others)
- an expected value: a canonical version range such as `{"current_version": "< 4.0", "target_version": ">= 4.0"}`, a symbol, or a JSON-path fact
- a role (`required`, `alternative`, `disqualifying`, `uncertain`)
- ripgrep search queries

An assessment engine first evaluates the version conditions against the planned upgrade. It then evaluates app-side conditions against a repo or cluster, honors `applies_to.from_versions`, and reports the paths that fire, using `risk_level` and `confidence` for triage. `urx scan` demonstrates this on a synthetic app. Paths whose disqualifiers also match are marked `needs_review` rather than suppressed, because LLM-written disqualifier queries are sometimes inverted.
