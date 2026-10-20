# Technical Design Document: Upgrade Risk Extraction (URX)

> Build guide for Cursor. Read sections 1–3 before writing any code. Build in the milestone order of section 14; every milestone has acceptance tests that must pass before the next one starts.
>
> **Revision 1.1:** section 17 records gaps found while reviewing this document against the live sources and the assignment, and how each was resolved. Where section 17 conflicts with an earlier section, section 17 wins.

---

## 0. Instructions for the coding agent

- **Never invent URLs, versions or quotes.** Every source URL comes from `registry/*.yaml`. Every risk condition must carry evidence that the validator can verify against a cached file.
- **Keep the assignment's schema intact.** Do not rename or drop any field or enum value from section 6.1. Only add fields listed in 6.2.
- **Deterministic first.** If a step can be done with parsing, rules or lookups, do not use an LLM.
- **Test first.** For each component, write the tests in section 13 before the implementation.
- **Offline by default.** The whole pipeline must run with no network and no API key from `cache/` and `llm_cache/`.
- **Python 3.11+, Pydantic v2, Typer for the CLI, pytest.** No other framework is required. No LangChain needed.

---

## 1. Problem and goals

Given `(project, current_version, target_version)`, produce a machine-readable **upgrade risk model**: risk paths made of evidence-grounded conditions, for consumption by a downstream engine that checks whether a specific codebase or deployment is affected.

**Required upgrades:** Django 3.2→4.2, React 17→18, Kubernetes 1.23→1.29, PostgreSQL 13→16, Next.js 12→14.

**Goals**
1. Specific, checkable risks (symbols, settings, versions), never vague summaries.
2. Every condition grounded in verifiable evidence; unsupported claims are marked `uncertain` or dropped.
3. Explicit handling of conflicts, gaps and uncertainty.
4. A decomposed workflow, not a single prompt.
5. Scales to thousands of projects through configuration, not code.

**Non-goals:** analyzing real or private codebases, running upgrades, producing migration plans, filing issues upstream.

---

## 2. Lessons learned from the prototype run (design drivers)

A hand-run prototype covered all five upgrades (70 risk paths, 247 verified quotes). Each lesson below drives a design rule and a guarding test.

| # | Lesson | Design rule | Guarding test |
|---|---|---|---|
| L1 | Target-version notes miss most breaks (Django 4.2 removes almost nothing; 4.0/4.1 do). | Process every release on the path (planner). | `test_planner_django_walks_4_0_4_1_4_2` |
| L2 | Changes compose across versions: superseded (Django `alias` in `get_group_by_cols`), reverted (4.1 related-manager cache, reverted in 4.1.2). | Net-effect composition rules R1–R6. | `test_compose_revert_dropped`, `test_compose_supersession` |
| L3 | Per-hop remediation can be wrong at target (K8s 1.26 says migrate FlowSchema to v1beta2, removed in 1.29). | Remediation is computed against the target. | `test_remediation_flowschema_targets_v1beta3_or_v1` |
| L4 | Remediation can itself be a risk (PDB `policy/v1` empty selector selects all pods). | Extraction prompt asks for "notable changes in the replacement." | Gold item present |
| L5 | Official docs omit dominant real-world triggers (Django 4.0 CSRF behind TLS proxy; Trac #34855 closed wontfix). | Tier-2 sources allowed for conditions, capped at medium confidence. | `test_rubric_tier2_never_high` |
| L6 | Official sources contradict each other (Next 13 Node floor: 14.6.0 vs 16.14.0). | Package metadata outranks prose for version facts; JSON-path evidence. | `test_jsonpath_evidence_resolves` |
| L7 | Docs are edited retroactively; current pages can be stubs (Next v14 canary page = 504-byte transclusion pointer). | Pin every source to the release tag; detect stubs. | `test_stub_detection` |
| L8 | Heading-based filtering leaks recall (zoneinfo default, CSRF_COOKIE_MASKED live in "What's new"). | LLM triage on all items plus a recall sweep. | Recall metric vs gold |
| L9 | Heading depth isn't semantic (React uses `##` for both versions and subsections). | Adapters decide version boundaries by anchors, not depth. | `test_react_section_boundaries` |
| L10 | Format conversion can delete entities (DocBook `<xref linkend="guc-password-encryption"/>` vanished). | Format adapters resolve link targets; golden-sentence tests per format. | `test_docbook_keeps_password_encryption` |
| L11 | Many risks are gated (React 18 changes only with `createRoot`). | `role: disqualifying` conditions. | Schema + gold |
| L12 | Applicability depends on upgrade method (PG15 public schema: new DBs only; pg_upgrade preserves). | `applies_to.upgrade_method`. | Gold item |
| L13 | Some risks are latent (PG14 scram default fires on password rotation). | `fires_at` field. | Schema |
| L14 | Path rules differ per project (K8s walks every minor; PG jumps majors and skips minor-release notes). | `traversal` rule in registry. | `test_planner_pg_skips_minors` |
| L15 | Biggest blockers are often third-party (`@types/react`, PG extensions, backup tools). | Open questions list; never invent versions. | Validator: uncertain conditions need ambiguity text |
| L16 | Fuzzy quote matching passes wrong facts (dropped "3.8" scored 0.91 similarity). | Exact match after normalization. | `test_validator_rejects_drifted_quote` |
| L17 | The validator had a bug only bad input exposed. | Every validator rule has a negative test. | `tests/test_validator_adversarial.py` |
| L18 | Search returns mirrors and SEO noise; GitHub API rate-limits unauthenticated calls. | Registry seeds first; search is discovery only; token-authenticated API. | Inventory `rejected` entries |
| L19 | Structure filtering is a huge cost lever (K8s 2.7 MB → 17k chars of Urgent Upgrade Notes). | Structure-aware selection before any LLM call. | Cost metric |
| L20 | "No user action required" items appear in urgent sections. | Triage label `context`. | Gold context items |

---

## 3. Architecture

Three pipelines, with the LLM confined to fixed steps.

```
                 (A) BATCH INGESTION  -- triggered per release / nightly
registry.yaml -> Fetcher -> Raw cache (pinned, hashed)
              -> Format adapter -> DocTree -> Item splitter -> ChangeItems (+metadata, symbols)
              -> Metadata extractor (package.json / PyPI) -> VersionFacts

                 (B) BATCH EXTRACTION  -- per release, once
ChangeItems(project, release) -> Triage (LLM, cheap) -> Extractor (LLM, strong, tool-use)
              -> Linker (hybrid search: dedup, corroborate) -> ReleaseRisks (stored)

                 (C) COMPOSITION / SERVING  -- per (project, from, to)
Planner(traversal) -> collect ReleaseRisks -> Net-effect rules R1-R6 (+ LLM reconcile, rare, cached)
              -> Confidence rubric -> Validator (deterministic + LLM judge) -> RiskModel JSON + report
```

Why this shape:
- **Batch, release-triggered ingestion**: releases are discrete and immutable once pinned. No streaming.
- **Per-release extraction**: LLM cost grows with releases, not with (from, to) pairs.
- **Exhaustive selection, not top-k retrieval**: for extraction, every change item on the path is processed. Retrieval is used only for linking and corroboration.
- **Agentic behavior is bounded**: only source discovery and open-question follow-up (stage A6), with a tool whitelist and step budget.

---

## 4. Repository layout

```
urx/
  README.md
  DESIGN_NOTE.md
  pyproject.toml
  registry/                   # one YAML per project (section 5)
    django.yaml kubernetes.yaml react.yaml postgresql.yaml nextjs.yaml
  prompts/                    # versioned prompt templates (section 9)
    triage.v1.md extract.v1.md judge.v1.md reconcile.v1.md
  schemas/
    risk_model.schema.json    # exported from Pydantic
  src/urx/
    models.py                 # Pydantic models (section 6)
    registry.py               # load + validate registry
    fetch.py                  # fetcher, pinning, hashing, stub detection
    adapters/                 # format adapters -> DocTree
      base.py rst.py markdown.py docbook.py json_meta.py
    normalize.py              # canonical text for quote matching
    items.py                  # DocTree -> ChangeItems, symbol extraction
    planner.py                # version paths, traversal rules
    llm/
      client.py               # provider interface + cache
      providers/anthropic.py providers/openai.py providers/local.py
    triage.py extract.py link.py
    compose.py                # net-effect rules R1-R6
    rubric.py                 # confidence
    validate.py               # deterministic checks
    judge.py                  # LLM entailment judge
    report.py                 # markdown report + mermaid graph
    overrides.py              # human review decisions
    scan.py                   # demo downstream consumer
    pipeline.py               # stage orchestration + run_log.jsonl events (17.3)
    server.py                 # FastAPI for the UI (17.3)
    evaluate.py               # metrics of 17.4
    cli.py
  ui/                         # React + Vite + TypeScript frontend (17.3)
  cache/                      # raw + normalized sources (committed)
  llm_cache/                  # LLM responses keyed by hash (committed)
  outputs/<project>_<from>_to_<to>/
    risk_model.json source_inventory.json report.md graph.mmd
    intermediate/items.jsonl intermediate/triage.jsonl intermediate/release_risks.jsonl
  gold/ django_3.2_4.2.yaml kubernetes_1.23_1.29.yaml
  review/overrides.yaml
  eval/run_eval.py eval/ablations.py eval/results.md
  tests/
  fixtures/demo_app/          # tiny synthetic app for scan demo
```

---

## 5. Project registry

The registry is the scaling mechanism: adding a project is a YAML file plus, at most, a new format adapter.

### 5.1 Schema

```yaml
project: string
format_defaults: rst | markdown | mdx | docbook
traversal:
  mode: walk_minors | walk_majors | jump_majors | single
  release_unit: minor | major          # what counts as a "release" for extraction
  skip_patch_sections: bool            # PG: ignore minor-release migration sections
version_scheme: semver | pep440 | k8s
sources:
  - id: string                         # stable short id
    title: string
    type: official_release_notes | official_migration_guide | official_changelog |
          official_deprecation_notice | official_api_docs | package_registry_metadata |
          github_issue | maintainer_blog | community_writeup
    tier: 1 | 2 | 3
    url_template: string               # public URL shown in inventory
    raw_template: string               # raw fetch URL, pinned (tag/branch per release)
    format: rst | markdown | mdx | docbook | json
    per_release: bool                  # one fetch per release vs once
    section:                           # optional extraction window
      start: string                    # literal anchor text (templated)
      end: string | null
    pin: tag | branch | commit
version_facts:                         # deterministic metadata
  - source_id: string
    fields: {node: "engines.node", react_peer: "peerDependencies.react"}
```

### 5.2 Seed registries (verified in prototype unless marked VERIFY)

**django.yaml**
```yaml
project: Django
traversal: {mode: walk_minors, release_unit: minor, skip_patch_sections: true}
version_scheme: pep440
sources:
  - id: dj_notes
    type: official_release_notes
    tier: 1
    url_template: "https://docs.djangoproject.com/en/{target}/releases/{release}/"
    raw_template: "https://raw.githubusercontent.com/django/django/stable/{target}.x/docs/releases/{release}.txt"
    format: rst
    per_release: true
    pin: branch
  - id: dj_deprecation
    type: official_deprecation_notice
    tier: 1
    url_template: "https://docs.djangoproject.com/en/{target}/internals/deprecation/"
    raw_template: "https://raw.githubusercontent.com/django/django/stable/{target}.x/docs/internals/deprecation.txt"
    format: rst
    per_release: false
    pin: branch
  - id: dj_pypi                        # VERIFY field names
    type: package_registry_metadata
    tier: 1
    raw_template: "https://pypi.org/pypi/Django/{release}/json"
    format: json
    per_release: true
```

**kubernetes.yaml**
```yaml
project: Kubernetes
traversal: {mode: walk_minors, release_unit: minor, skip_patch_sections: true}
version_scheme: k8s
sources:
  - id: k8s_deprecation_guide
    type: official_deprecation_notice
    tier: 1
    url_template: "https://kubernetes.io/docs/reference/using-api/deprecation-guide/"
    raw_template: "https://raw.githubusercontent.com/kubernetes/website/main/content/en/docs/reference/using-api/deprecation-guide.md"
    format: markdown
    per_release: false
    pin: commit                        # record SHA in inventory
  - id: k8s_changelog
    type: official_changelog
    tier: 1
    url_template: "https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-{release}.md"
    raw_template: "https://raw.githubusercontent.com/kubernetes/kubernetes/master/CHANGELOG/CHANGELOG-{release}.md"
    format: markdown
    per_release: true
    section: {start: "# v{release}.0\n", end: "# v{release}.0-rc"}
    subsection: {start: "## Urgent Upgrade Notes", end: "## Changes by Kind"}
  - id: k8s_skew
    type: official_api_docs
    tier: 1
    url_template: "https://kubernetes.io/releases/version-skew-policy/"
    raw_template: "https://raw.githubusercontent.com/kubernetes/website/main/content/en/releases/version-skew-policy.md"
    format: markdown
    per_release: false
```

**react.yaml**
```yaml
project: React
traversal: {mode: single, release_unit: major}
sources:
  - id: react_changelog
    type: official_changelog
    tier: 1
    url_template: "https://github.com/facebook/react/blob/main/CHANGELOG.md"
    raw_template: "https://raw.githubusercontent.com/facebook/react/main/CHANGELOG.md"
    format: markdown
    section: {start: "## {release}.0.0", end: "## {prev_major}.0."}   # anchors, not heading depth (L9)
  - id: react_upgrade_guide
    type: official_migration_guide
    tier: 1
    url_template: "https://react.dev/blog/2022/03/08/react-18-upgrade-guide"
    raw_template: "https://raw.githubusercontent.com/reactjs/react.dev/main/src/content/blog/2022/03/08/react-18-upgrade-guide.md"
    format: mdx
```

**postgresql.yaml**
```yaml
project: PostgreSQL
traversal: {mode: jump_majors, release_unit: major, skip_patch_sections: true}
sources:
  - id: pg_release_notes
    type: official_release_notes
    tier: 1
    url_template: "https://www.postgresql.org/docs/release/{release}.0/"
    raw_template: "https://raw.githubusercontent.com/postgres/postgres/REL_{release}_STABLE/doc/src/sgml/release-{release}.sgml"
    format: docbook
    per_release: true
    section: {docbook_sect2_title: "Migration to Version {release}"}   # exact title; excludes 14.x minors
```

**nextjs.yaml**
```yaml
project: Next.js
traversal: {mode: walk_majors, release_unit: major}
sources:
  - id: next_guide_13_tag
    type: official_migration_guide
    tier: 1
    url_template: "https://github.com/vercel/next.js/blob/v13.0.0/docs/upgrading.md"
    raw_template: "https://raw.githubusercontent.com/vercel/next.js/v13.0.0/docs/upgrading.md"
    format: markdown
    release: "13"
    section: {start: "## Upgrading from 12 to 13", end: "## Upgrading to 12.2"}
  - id: next_guide_13_current
    type: official_migration_guide
    tier: 1
    url_template: "https://nextjs.org/docs/pages/guides/upgrading/version-13"
    raw_template: "https://raw.githubusercontent.com/vercel/next.js/canary/docs/02-pages/02-guides/upgrading/version-13.mdx"
    format: mdx
    release: "13"
  - id: next_guide_14_tag
    type: official_migration_guide
    tier: 1
    url_template: "https://github.com/vercel/next.js/blob/v14.2.0/docs/02-app/01-building-your-application/11-upgrading/03-version-14.mdx"
    raw_template: "https://raw.githubusercontent.com/vercel/next.js/v14.2.0/docs/02-app/01-building-your-application/11-upgrading/03-version-14.mdx"
    format: mdx
    release: "14"
  - id: next_pkg
    type: package_registry_metadata
    tier: 1
    raw_template: "https://raw.githubusercontent.com/vercel/next.js/{tag}/packages/next/package.json"
    format: json
    tags: [v12.3.4, v13.0.0, v13.4.0, v13.5.0, v14.0.0]
version_facts:
  - {source_id: next_pkg, fields: {node: "engines.node", react_peer: "peerDependencies.react"}}
```

---

## 6. Data model

### 6.1 Assignment schema (must not change)

Risk path fields: `path_id, path_name, risk_type, risk_level, affected_surface, description, conditions, suggested_actions`.

Condition fields: `condition_id, statement, category, required, operator, expected_value, evidence[], confidence, ambiguities[]`.

Evidence fields: `source_id, source_type, quote_or_summary, relevance`.

Enums (exact):
- `risk_type`: removed_api, changed_behavior, changed_default, dependency_requirement, runtime_requirement, configuration_change, data_migration, operational_risk, unknown
- `risk_level`: critical, high, medium, low, unknown
- `affected_surface`: application_code, configuration, dependencies, runtime, database, deployment, tests, unknown
- `category`: version, api_usage, configuration, dependency, runtime, deployment, database, behavior, test_coverage, unknown
- `operator`: equals, not_equals, in_range, less_than, greater_than, contains, absent, present, unknown
- `confidence`: high, medium, low

Top level: `project, current_version, target_version, summary, source_inventory[], risk_paths[], open_questions[], overall_confidence`, plus `evidence_summary {high_confidence_risks, medium_confidence_risks, low_confidence_or_disputed_risks, sources_with_disagreements, open_questions}`.

Note: the assignment's own example uses `category: removed_configuration`, which is not in its enum. We normalize to `configuration` and say so in the README.

### 6.2 Extensions (additive only)

| Field | On | Purpose | Lesson |
|---|---|---|---|
| `role` | condition | `required, alternative, optional, disqualifying, uncertain` (the five values the assignment text names). `required` bool kept and derived. | L11 |
| `derived_by` | condition | `extraction` (quoted), `rule` (deterministic derivation), `inference` | L5 |
| `search_queries[]` | condition | ripgrep/kubectl/SQL queries for downstream checks | Bonus |
| `quote` + `verified` | evidence | verbatim quote; `quote_or_summary` mirrors it for compatibility | L16 |
| `json_path` + `expected` | evidence | structured metadata evidence | L6 |
| `applies_to` | path | `{cluster_type, upgrade_method, from_versions}` | L12 |
| `fires_at` | path | `upgrade, first_use, rotation, rollout, future_removal` | L13 |
| `introduced_in` | path | release where the change happened | L1 |
| `superseded_by` / `reverted_in` | path | composition provenance | L2 |
| `context_facts[]` | top | useful non-risks with evidence + `why_not_risk` | Part 3 |
| `disqualified_candidates[]` | top | rejected risks with reason + evidence | Part 3 |
| `requires_upgrades[]` | top | cross-project dependency (Next → React) | L6 |
| `authority_tier`, `content_hash`, `pinned_ref`, `status`, `rejection_reason` | source | trust and reproducibility | L7, L18 |

### 6.3 Internal models

```python
class ChangeItem(BaseModel):
    item_id: str              # sha1(project|release|source_id|normalized_text)[:12]
    project: str
    release: str              # e.g. "4.0", "1.25"
    source_id: str
    heading_path: list[str]
    section_type: Literal["removed","deprecated","incompatible","changed","new","requirements","urgent","other"]
    text: str                 # normalized text
    raw_span: tuple[int, int] # line range in raw cache
    symbols: list[str]        # ``x``, `x`, <literal>x</literal>, apiVersion strings
    parent_id: str | None     # small-to-big context

class TriageLabel(BaseModel):
    item_id: str
    label: Literal["risk","context","noise"]
    reason: str

class ReleaseRisk(BaseModel):     # stored per release, version-parameterized
    risk_key: str                 # stable: sha1(project|introduced_in|primary_symbol|risk_type)
    introduced_in: str
    applies_if_from: str | None   # e.g. "<4.0"; start-dependent applicability
    reverted_in: str | None
    symbols: list[str]
    path: RiskPath                # assignment shape, version condition templated
```

Stable IDs: `path_id = f"{project_slug}_{risk_key}"`; `condition_id` is a slug plus a short hash of the normalized statement. Reruns must not reshuffle IDs (required for overrides and gold matching).

---

## 7. Pipeline A: ingestion

### A1. Fetcher (`fetch.py`)
- Resolve `raw_template` per release from the registry; fetch with `httpx`, retries, timeout 30 s.
- Save raw bytes to `cache/<project>/<source_id>/<release>.<ext>`; record `content_hash` (sha256), `pinned_ref` (tag/branch/commit SHA), `retrieved_at`.
- **Stub detection (L7):** if the normalized body is under 1,500 chars, or the frontmatter contains `source:` with no body, mark `status: rejected, rejection_reason: transclusion_stub`.
- **Offline mode:** if `--offline` or no network, read only from `cache/`; fail loudly if missing.
- GitHub API calls (discovery only) require `GITHUB_TOKEN`; never depend on the API for core fetching (L18).

### A2. Format adapters (`adapters/`)
All adapters return a `DocTree`: nodes `{kind: heading|para|list_item|code|table_row, text, level, children, raw_span}`.

| Adapter | Must handle |
|---|---|
| `rst.py` | Underline headings (level by order of first appearance); roles `:setting:`x``, `:py:attr:`x <y>``, `:meth:`~a.b``, leading `.` and `~`; `.. _label:` anchors; `::` code blocks; bullet lists with continuation lines. |
| `markdown.py` / MDX | ATX headings; JSX comments `{/* */}`; frontmatter; `{#anchor}` suffixes; links `[t](u)` → `t`; PR refs `([#123](...), [@user](...))` stripped. |
| `docbook.py` | `<sect1>/<sect2>` with `<title>`; `<xref linkend="..."/>` **resolved, never dropped** (L10); `<link linkend>` → inner text; `<listitem>`, `<para>`, `<literal>`, `<varname>`, `<application>`; `§` commit links removed; HTML entities. |
| `json_meta.py` | Load JSON; expose dotted-path lookups for version facts. |

**xref resolution map (DocBook):** `guc-<name>` → `<name>` with `-`→`_`; `pgupgrade` → `pg_upgrade`; `app-pgdump` → `pg_dump`; `app-pgdumpall` → `pg_dumpall`; unknown linkend → linkend text verbatim (never empty). Log every unknown linkend.

**Section windows:** applied by anchors from the registry (`section.start/end`, `docbook_sect2_title`), never by heading depth (L9).

### A3. Normalizer (`normalize.py`)
One function used by both the item builder and the validator, so quotes match what the LLM saw:
roles → inner text, links → text, strip backticks / `**` / literal `\n`, collapse whitespace. Do **not** strip single `*` (breaks `https://*.example.com`).

### A4. Item splitter (`items.py`)
- Split each section into atomic items: one bullet = one item; a short headed section (under 1,200 chars) = one item; long sections are split by paragraph with `parent_id` set.
- `section_type` from heading text (e.g. "Backwards incompatible" → incompatible, "Features removed" → removed, "Urgent Upgrade Notes" → urgent).
- Symbols: RST/MD code spans, DocBook `<literal>/<varname>/<function>`, `apiVersion`-like `group/vNbetaM`, settings in CAPS_SNAKE, CLI flags `--x`.
- Deduplicate across sources by `(normalized symbol set, sha1(normalized text))`. Keep all sources as evidence; dedup never deletes provenance.

### A5. Version facts
Deterministic extraction from package metadata into `VersionFacts{release, field, value, source_id, json_path}`. Used as tier-1 evidence and to resolve prose conflicts (L6).

### A6. Discovery agent (optional, bounded)
For projects without a complete registry, or to chase open questions.
- Tools: `web_search`, `fetch_url` (registry domains + github.com only), `list_repo_tags`, `read_cached`.
- Budget: 12 steps, 0 writes; outputs a **proposed** registry patch + rationale for human approval. Never feeds extraction directly.

---

## 8. Pipeline B: per-release extraction

### B1. Triage (`triage.py`, cheap model)
Run on **every** item of a release (not only keyword hits; L8). Batch 20 items per call. Output `TriageLabel`.
- `risk`: a change that can break, require migration, or create operational risk for some user.
- `context`: true and useful, but no user action or impact at this target (e.g. "No user action required", deprecations that still work, new optional features).
- `noise`: bug-fix-only, credits, install commands, marketing.

Recall sweep: re-triage items labeled `noise` that contain signal regexes (`removed|no longer|now raises|default|deprecat|must|requires`) with the strong model. Log disagreements.

### B2. Extraction (`extract.py`, strong model, tool-use)
Input: one `risk` item plus its parent context plus version facts for that release. Output via a forced tool schema (Pydantic → JSON Schema): one or more draft paths with conditions. Rules enforced by prompt **and** validator:
- Every condition needs ≥1 evidence with a **verbatim** quote from the provided text (≤40 words).
- Each path has a version-side condition (`category: version`) and at least one app/deployment-side condition.
- Use `role` for alternatives/gates; `uncertain` with ambiguity text when not stated.
- Extract replacement/remediation and any "notable changes" in the replacement (L4).
- Emit `search_queries` for app-side conditions.
- Never output confidence; the rubric computes it.

### B3. Linker (`link.py`)
Hybrid search over `ChangeItems` (+ cached tier-2 docs):
- Sparse: Postgres `tsvector` / BM25 (exact symbols like `CSRF_TRUSTED_ORIGINS`, `policy/v1beta1`).
- Dense: embeddings (pgvector or FAISS locally) for paraphrases.
- Fuse with Reciprocal Rank Fusion (k=60).

Uses: corroborate a risk with other sources (adds evidence and raises the rubric score), detect duplicates across releases, find same-symbol chains for composition, and find tier-2 real-world triggers. Query rewriting is used only for tier-2 search: generate symbol, error-message and symptom variants.

---

## 9. Prompts (`prompts/*.md`, versioned)

Prompt files carry a version suffix; the version is part of the LLM cache key. All calls use temperature 0.

**triage.v1.md**
```
You classify release-note items for software upgrade risk.
Project: {project}. Release: {release}. Section: {heading_path}.
For each item return label in {risk, context, noise} and a one-sentence reason.
risk = could break an application, require migration work, or create operational risk.
context = accurate and useful but needs no action at this release (e.g. "no user action required",
deprecated but still working, optional new feature).
noise = credits, install commands, pure bug fixes that cannot change correct behavior.
When unsure between risk and context, choose risk.
Items:
{items_jsonl}
```

**extract.v1.md**
```
You extract upgrade risk conditions from official documentation. Use ONLY the text provided.
Project {project}; change introduced in release {release}; version facts: {facts}.
Item: {item_text}
Parent context: {parent_text}

Produce risk paths via the tool. Hard rules:
1. Each condition cites at least one verbatim quote copied exactly from the item or parent text (max 40 words).
2. Each path has one condition with category "version" and at least one condition about the
   application or deployment (api_usage, configuration, dependency, runtime, deployment, database,
   behavior, test_coverage).
3. If the text does not state something, do not assert it. Use role "uncertain" and explain in ambiguities.
4. Alternatives (any one is enough) use role "alternative". Conditions that make the risk NOT apply use role "disqualifying".
5. If a replacement API/setting is given, record it in suggested_actions and add a condition for any
   behavior that differs in the replacement.
6. Provide search_queries (ripgrep, kubectl, or SQL) for app-side conditions when a literal symbol exists.
7. Do not output confidence.
```

**judge.v1.md** (entailment)
```
Claim: {statement}
Evidence quote: {quote}
Does the quote, on its own, support the claim? Answer JSON:
{"verdict": "supported" | "partially_supported" | "not_supported", "missing": "<what the claim adds beyond the quote>"}
Be strict: added specifics (versions, impacts, scopes) not in the quote make it partially_supported.
```

**reconcile.v1.md** (rare; same-symbol conflicts the rules can't resolve)
```
These items from releases {releases} affect the same symbol {symbol}, in order:
{items}
Target version is {target}. State the net requirement at the target, which earlier guidance is
superseded, and quote the evidence for each part. If unresolved, say "unresolved" and why.
```

---

## 10. Pipeline C: composition and serving

### C1. Planner (`planner.py`)
`plan(project, from, to) -> list[release]` using `traversal.mode`:
- `walk_minors` (Django, K8s): every minor in `(from, to]`.
- `walk_majors` (Next.js): every major in `(from, to]`.
- `jump_majors` (PostgreSQL): every major's migration section in `(from, to]`; never minor-release sections (L14).
- `single` (React): the target major.

Also emits path-level constraints (e.g. K8s skew: control plane one minor at a time; kubelet < 1.25 may lag only two minors).

### C2. Net-effect rules (`compose.py`)
| Rule | Logic |
|---|---|
| R1 Revert | `reverted_in <= target` → move to `disqualified_candidates` with evidence. |
| R2 Supersession | Same primary symbol, later release changes it → keep the latest requirement; earlier one goes to `ambiguities` as history; set `superseded_by`. |
| R3 Remediation chain | For removed API versions, choose a replacement **not removed at or before target** (FlowSchema: v1beta3 or v1, never v1beta2). Data comes from extracted replacement + availability facts. |
| R4 Traversal filter | Drop items not on the planned release list. |
| R5 Start applicability | Drop risks whose `applies_if_from` excludes `from`. |
| R6 Deprecated-not-removed | Deprecated at or before target but removed after target → `context_facts` with `fires_at: future_removal`. |
| R7 Cross-project | If version facts require another project upgrade (Next 13 → React 18), add `requires_upgrades` and link that risk model. |

Unresolved same-symbol conflicts → `reconcile` prompt; result cached by `(symbol chain hash, target)`.

### C3. Confidence rubric (`rubric.py`), deterministic
```
score = 0
+2 if any evidence is tier 1 (official or package metadata)
+1 if evidence comes from 2+ independent sources
+1 if json_path evidence agrees
-2 if derived_by == "inference"
-1 if ambiguities non-empty
-1 if judge verdict == partially_supported
role == "uncertain" or judge == not_supported  -> low (hard cap)
only tier 2/3 evidence                         -> at most medium (hard cap, L5)
high if score >= 2; medium if score in {0, 1}; low otherwise
```
Path confidence = minimum over its `required` + `alternative` conditions. `overall_confidence` = share of high paths, with source coverage gaps noted in open questions.

### C4. Validator (`validate.py`), deterministic, runs before output is written
Errors (reject):
1. Schema/enum violation (JSON Schema).
2. Evidence `source_id` not in inventory with status `used`.
3. Quote not found verbatim in the normalized cached source (exact match, no fuzzy; L16).
4. `json_path` value ≠ `expected`.
5. Path without a `version` condition, or without an app/deployment condition.
6. Condition without evidence unless `role == uncertain` **and** ambiguities non-empty.
7. Confidence `high` without tier-1 evidence.
8. `requires_upgrades` pointing to a missing model.
9. Duplicate `path_id`/`condition_id`.
10. Context facts / disqualified candidates with unverifiable evidence.

Warnings: no suggested actions; quote over 40 words; inferred condition marked high; no search queries for symbol-bearing conditions.

### C5. LLM judge (`judge.py`)
Runs on every condition's (statement, quote). `not_supported` → downgrade to `uncertain` and flag for review; `partially_supported` → rubric penalty. Calibrated against human labels (section 12).

### C6. Outputs (`report.py`)
- `risk_model.json` (validated), `source_inventory.json`, intermediate JSONL artifacts.
- `report.md`: summary, risk table by level, each path with conditions and quotes, **review checklist** (low confidence, disputed, inferred, open questions), what we trusted / didn't trust.
- `graph.mmd`: Mermaid graph: path → AND of required conditions; alternatives as OR nodes; disqualifying conditions as dashed NOT edges; cross-project links.

### C7. Human review (`overrides.py`)
`review/overrides.yaml` keyed by stable IDs:
```yaml
- id: django_ab12cd34/tls_terminated_upstream_no_proxy_header
  decision: accept | reject | edit
  edits: {confidence_floor: medium, statement: "..."}
  reviewer: mehdi
  note: "confirmed by Trac #34855"
```
Applied after composition on every run; accepted and rejected decisions are exported to `gold/` (learning loop).

### C8. Demo downstream consumer (`scan.py`)
`urx scan --model outputs/django_3.2_to_4.2/risk_model.json --repo fixtures/demo_app` runs each condition's `search_queries` (ripgrep only) against a synthetic fixture app with planted usages and prints which paths fire. Shows how a downstream engine consumes the output. Never run against real or private repos (assignment constraint).

### C9. CLI (`cli.py`)
```
urx extract --project Django --current-version 3.2 --target-version 4.2 [--offline] [--provider anthropic|openai|local]
urx ingest  --project Django --releases 4.0,4.1,4.2
urx validate outputs/*/risk_model.json
urx report  outputs/django_3.2_to_4.2
urx eval    --gold gold/django_3.2_4.2.yaml
urx scan    --model ... --repo fixtures/demo_app
```
Also `python extract_upgrade_risks.py --project Django --current-version 3.2 --target-version 4.2` as a thin wrapper (the exact form the assignment shows).

### C10. LLM client (`llm/client.py`)
- Interface: `complete(prompt_id, variables, schema=None, model_tier="cheap"|"strong") -> dict`.
- Providers: Anthropic (default), OpenAI, local (Ollama). Model names come from config, not code.
- Cache: key = sha256(provider, model, prompt_version, rendered_prompt, schema_hash). Store request + response in `llm_cache/`. On cache hit, no network.
- Retries with backoff; on schema-validation failure, one repair attempt with the error message, then mark the item `extraction_failed` (logged, never silently dropped).
- Log tokens and cost per stage for the cost report.

---

## 11. Trust model and known failure modes

**Trust order:** package metadata (version facts) > official deprecation guides and migration guides > official release notes and changelogs > maintainer issue trackers (tier 2) > community writeups (tier 3, discovery only). Third-party mirrors of official text are rejected.

**What we do not trust:** LLM self-reported confidence; unpinned "latest" docs; search-result snippets as evidence; any quote that fails exact match.

**Known failure modes (document in README):**
- Normalizer drops entities in a new format → quotes verify against broken text. Mitigation: golden-sentence tests per adapter; log unknown linkends.
- Retroactively edited docs or transclusion stubs. Mitigation: tag pinning, stub detection.
- Recall gaps in unmined sources (K8s "Changes by Kind", Next.js minor release notes). Mitigation: stated in `open_questions`; recall measured against gold.
- Ecosystem risks outside project docs (`@types/react`, PG extensions, backup tools, third-party packages pinned to old versions, managed-service behavior). Mitigation: listed as open questions, never invented.
- Gates and scopes inferred rather than stated (React Strict Mode gating). Mitigation: `uncertain` role + ambiguity.

---

## 12. Evaluation plan

### 12.1 Gold sets
- **Kubernetes 1.23→1.29 (semi-automatic):** API removals generated from the structured deprecation guide; urgent-note items added by hand. See Appendix B.
- **Django 3.2→4.2 (manual):** from "Backwards incompatible", "Features removed", "Python compatibility" sections, the deprecation timeline, plus the "What's new" behavior changes. See Appendix A.
- Each gold item: `{gold_id, release, symbols[], kind: risk|context|disqualified, min_level, notes}`.
- Reviewer overrides append to gold over time (C7).

### 12.2 Matching
An extracted path matches a gold item if `introduced_in == release` and symbol sets overlap. Unmatched pairs go to an LLM matcher; its matches are listed for human adjudication in `eval/results.md`.

### 12.3 Metrics (`eval/run_eval.py`)
| Metric | Definition | Target |
|---|---|---|
| Risk recall | matched gold risks / gold risks | ≥ 0.90 |
| Risk precision | extracted paths matching a gold risk or adjudicated valid / extracted paths | ≥ 0.85 |
| Classification accuracy | risk vs context vs disqualified agreement with gold | ≥ 0.85 |
| Condition field accuracy | category, operator, expected_value correct on a 40-condition sample | ≥ 0.80 |
| Grounding rate | quotes verified / quotes | 1.00 (hard) |
| Entailment precision | judge "supported" agrees with human label (50 labeled pairs) | report agreement + Cohen's κ |
| Calibration | precision(high) > precision(medium) > precision(low) | must hold |
| Stability | Jaccard of path IDs across two cold runs (cache off) | ≥ 0.90 |
| Cost / latency | tokens and wall time per upgrade, per stage | report |

### 12.4 Ablations (`eval/ablations.py`)
1. Single-prompt baseline (whole doc → JSON) vs pipeline: recall, precision, grounding rate.
2. Keyword filter vs LLM triage + recall sweep: recall.
3. With vs without judge: precision, calibration.
4. Per-pair extraction vs per-release + composition: equal outputs, cost ratio.
5. Fuzzy vs exact quote matching on injected drift: false-accept rate.

Results go to `eval/results.md` and are summarized in the design note.

---

## 13. Test plan (write these first)

### 13.1 Adapters and normalizer (`tests/test_adapters.py`), golden sentences
- RST: ``:setting:`CSRF_TRUSTED_ORIGINS` `` → text contains `CSRF_TRUSTED_ORIGINS`.
- RST: ``:py:attr:`hostname <ssl.SSLContext.check_hostname>` `` → `hostname`.
- RST: ``:meth:`.Expression.get_group_by_cols` `` → `Expression.get_group_by_cols`.
- DocBook (PG14 cached): migration text contains `password_encryption`; PG15/16 contain `pg_upgrade`; no empty-slot artifacts (regex ` ,|, ,| or use of or `).
- DocBook: only the sect2 titled exactly `Migration to Version 14` is extracted (not `14.24`).
- MDX: `{/* ... */}` removed; Next v14 canary file flagged `transclusion_stub`.
- Markdown K8s: v1.24.0 Urgent Upgrade Notes contain `dockershim`; PR refs stripped.
- React: 18.0.0 window contains `## Breaking Changes` and excludes `## 17.0.2`.
- Normalizer: `https://*.example.com` survives.

### 13.2 Planner (`tests/test_planner.py`)
- Django 3.2→4.2 → `[4.0, 4.1, 4.2]`.
- K8s 1.23→1.29 → `[1.24 … 1.29]` + skew constraints.
- PG 13→16 → `[14, 15, 16]`, minor sections excluded.
- Next 12→14 → `[13, 14]`; React 17→18 → `[18]`.

### 13.3 Composition (`tests/test_compose.py`), synthetic fixtures
- Revert: risk introduced 4.1, `reverted_in: 4.1.2`, target 4.2 → disqualified.
- Supersession: 4.0 "alias=None required", 4.2 "alias removed" → single path; requirement from 4.2; history in ambiguities.
- Remediation chain: v1beta1 removed 1.26 → replacement v1beta2 (removed 1.29) rejected; v1beta3/v1 chosen for target 1.29.
- Deprecated-not-removed: deprecated 4.2, removed 5.0, target 4.2 → context fact.
- Start applicability: `applies_if_from: "<3.1"`, from 3.2 → dropped.
- Cross-project: Next 13 peer `react ^18.2.0` → `requires_upgrades` React 17→18.

### 13.4 Rubric (`tests/test_rubric.py`)
- Tier-2-only evidence never high.
- Inference never high.
- `uncertain` always low.
- Two tier-1 sources + json_path → high.

### 13.5 Validator, adversarial (`tests/test_validator_adversarial.py`)
Each must produce a specific error:
1. Drifted quote ("Python 3.9, 3.10, 3.11, and 3.12", 3.8 dropped).
2. Plausible invented quote.
3. Tier-2-only condition marked high.
4. Path without version condition.
5. `json_path` expected `>=16.14.0` against next@14.0.0 (actual `>=18.17.0`).
6. Dangling `requires_upgrades`.
7. Unknown `source_id`; rejected source used as evidence.
8. Invalid enum (`removed_configuration`).
9. Condition with no evidence and no ambiguity.
10. Duplicate IDs.

### 13.6 LLM layer (`tests/test_llm_client.py`)
- Cache hit returns stored response with no network (mock transport raises).
- Schema failure triggers one repair, then `extraction_failed`.
- Prompt version change changes the cache key.

### 13.7 End-to-end (`tests/test_e2e_offline.py`)
- With committed `cache/` and `llm_cache/`, `urx extract` for all five upgrades runs offline, passes the validator, and matches snapshot path IDs.

---

## 14. Milestones (build order with acceptance criteria)

| M | Deliverable | Acceptance |
|---|---|---|
| M0 | Repo skeleton, models, JSON Schema export, registry loader | `pytest tests/test_models.py` green; schema exported |
| M1 | Fetcher + caching + stub detection; all five registries fetched | Cache populated; inventory with hashes and pinned refs; v14 canary rejected |
| M2 | Adapters + normalizer + item splitter | 13.1 green; item counts logged per release |
| M3 | Planner + version facts | 13.2 green; Next Node/React facts resolved from package.json |
| M4 | Validator + rubric (before any LLM!) | 13.4, 13.5 green |
| M5 | LLM client + cache + triage | 13.6 green; triage labels for all items; recall sweep log |
| M6 | Extraction + per-release storage | All release risks pass the validator; extraction failures listed |
| M7 | Composition rules + linker | 13.3 green; five risk models produced |
| M8 | Judge + report + Mermaid + overrides | Reports with review checklists; overrides re-applied on rerun |
| M9 | Gold sets + eval + ablations | `eval/results.md` with metrics in 12.3 and ablations in 12.4 |
| M10 | README, design note, scan demo, e2e offline test | 13.7 green; fresh clone runs offline in under 2 minutes |
| M11 | API server + UI (section 17.3) | `urx serve` shows all 5 upgrades, path detail with evidence context, evals, live run log; review decisions persist to `review/overrides.yaml` |

Stretch: extra upgrade (e.g. Python 3.8→3.12) via registry only; discovery agent; local-model provider.

---

## 15. Design note answers (source for DESIGN_NOTE.md)

1. **Decomposition:** ingestion (fetch, parse, split) → per-release triage and extraction → linking → composition per path → rubric → validation and judging → report. Each stage has a narrow contract and its own artifact.
2. **LLM role:** triage, extraction with forced schema, rare cross-version reconciliation, entailment judging, bounded discovery. Never parsing, version math, confidence or validation.
3. **Deterministic parts:** fetching, pinning, parsing, normalization, item splitting, symbol extraction, planning, composition rules, rubric, validator, report.
4. **Hallucination prevention:** verbatim quotes with exact match against cached sources; JSON-path evidence for version facts; judge for entailment; unsupported → uncertain or dropped; confidence never self-reported.
5. **Risk vs context:** a risk needs a version-side change and a checkable app/deployment-side condition under which it matters; otherwise it is a context fact, with evidence and a reason.
6. **Conflicts and gaps:** trust tiers; metadata settles version facts; R1–R3 handle reverts, supersession, remediation chains; every disagreement recorded in ambiguities and `sources_with_disagreements`; undocumented areas listed as open questions.
7. **Scaling:** registry-as-config; per-release extraction (cost grows with releases, not pairs); release-triggered batch jobs; cached composition; LLM cache.
8. **Precision/recall:** gold sets, matching, metrics and ablations in section 12.
9. **More time:** mine full changelogs and issue trackers; ecosystem sources (type packages, extensions, drivers); larger judge calibration set; more format adapters; discovery agent for registry generation.
10. **Downstream use:** conditions carry operators, expected values and search queries; the engine evaluates app-side conditions against a repo or cluster, honors disqualifying conditions and `applies_to`, and reports firing paths (demonstrated by `urx scan`).

---

## 16. Assignment compliance checklist

- [ ] Outputs and source inventories for all 5 upgrades
- [ ] Intermediate artifacts (items, triage, release risks)
- [ ] README: run, setup, API keys or offline mode, assumptions, limitations, what we trusted, where it fails
- [ ] Source code, prompts, schemas, retrieval/processing logic
- [ ] Design note (1–2 pages) answering all 10 questions
- [ ] Validation: JSON Schema, evidence check, critic/judge, rubric, gold comparison, structural test
- [ ] Not a single prompt (ablation proves the difference)
- [ ] Constraints respected: public docs only, no issues filed, no real repos scanned, explicit "not a migration plan" disclaimer in every output
- [ ] Bonus: extra upgrade, review report, rubric, source ranking, dedup, judge, graph, gold set, search queries, multi-provider

---

## 17. Gap review (revision 1.1)

Every registry URL in section 5.2 was fetched on 2026-10-20 and returned HTTP 200. The gaps below were found by checking the design against those live files and against the assignment text. Each gap has a resolution that the implementation follows.

### 17.1 Gaps that would have produced wrong results

| # | Gap | Evidence | Resolution |
|---|---|---|---|
| G1 | Stub rule "body under 1,500 chars" rejects real pages. | The pinned `v14.2.0` Next 14 guide is a real 1.3k-char page; the 504-byte canary page is the actual stub. | Stub = frontmatter has `source:` **and** body is empty after removing comments, **or** normalized body under 200 chars. Test: v14.2.0 guide accepted, canary stub rejected. The canary stub stays in the registry as a deliberately rejected source. |
| G2 | The planner cannot enumerate releases (Django has no 3.3; PG has no 13.5 majors). | `walk_minors` from 3.2 has no way to know the next release is 4.0. | Registry gains `known_releases` (ordered list, including releases after the targets, so future removals can be placed). The planner selects from that list and never does version arithmetic. |
| G3 | Revert rule R1 needs patch notes, but the registry skips patch sections. | Django's related-manager cache revert lives only in `4.1.2.txt`. | New source kind `patch_notes` with `revert_scan: true`: patch notes for each release on the path are fetched, and only items matching `\brevert` become revert candidates. An LLM reconcile step links each candidate to at most one path, quoting the revert. |
| G4 | Non-per-release sources (K8s deprecation guide, Django deprecation timeline) span every release. | The guide holds v1.16–v1.32 removals; using it whole would emit 1.16/1.22/1.32 risks for a 1.23→1.29 upgrade. | Source field `release_from_heading: <regex>` assigns each item the release from its nearest matching heading. R4 drops releases off the path; releases after the target feed R6 (future removal context). |
| G5 | Section windows use raw-text anchors, which break line spans and heading parsing at slice edges. | — | Windows are applied to parsed blocks: `select: [{start: <heading regex>, end: <heading regex or null>}]`, optionally nested via `within`. `end: null` means "next heading of the same or higher level". The full document is always parsed, so quote verification uses the same text the LLM saw. |
| G6 | K8s extraction only mined Urgent Upgrade Notes, a recall gap the TDD itself lists. | The `### Deprecation` subsection is 0.8–5 kB per release. | K8s windows = Urgent Upgrade Notes **plus** Changes by Kind / Deprecation. API Change and Feature stay unmined (listed in open questions). |
| G7 | The DocBook xref map is wrong for the real files. | PG uses `app-pg-dumpall`, not `app-pgdumpall`. | Map: `guc-*` → underscore name; `app-*` → strip prefix, `-`→`_`; explicit `pgupgrade`→`pg_upgrade`, `app-pgdump`→`pg_dump`; unknown → linkend verbatim and logged. |
| G8 | Quote matching does not define Unicode handling, so it can drift. | Curly quotes and non-breaking spaces appear in MDX sources. | `normalize()` = NFKC, curly→straight quotes, NBSP→space, strip backticks/`**`, collapse whitespace. It must be idempotent (tested). The validator applies it to both the source and the quote. |
| G9 | Primary symbol (needed for R2 and the linker) is undefined. | — | The extractor emits `primary_symbol` (the most specific identifier, e.g. the full apiVersion). Key normalization: lowercase, strip `()`, last dotted component unless it contains `/`. R2 only merges paths with the same key **and** the same `risk_type`, so FlowSchema v1beta1 and v1beta2 stay distinct. |
| G10 | `version` conditions have no canonical form, so the downstream engine cannot evaluate them. | — | After extraction, the first version condition is normalized to `operator: in_range`, `expected_value: {"current_version": "< R", "target_version": ">= R"}` where R = `introduced_in`. If the LLM omits one, a rule-derived version condition is injected (`derived_by: rule`) that quotes the item's opening words. |

### 17.2 Gaps that were undefined

| # | Gap | Resolution |
|---|---|---|
| G11 | How `risk_level` is set. | The extractor proposes `risk_level` using a rubric written into the prompt (critical = upgrade fails or data is at risk for most users who meet the conditions; high = breaks code that meets the conditions; medium = behavior change or migration with workaround; low = edge case or cosmetic). Confidence remains rubric-only. |
| G12 | How `summary`, `evidence_summary`, `open_questions` and `overall_confidence` are produced. | All are deterministic. The summary is a template over counts by type and level plus critical path names. `overall_confidence`: high if ≥ 70% of paths are high and there are no extraction failures or rejected tier-1 sources (deliberately rejected transclusion stubs excluded); medium if ≥ 70% of paths are at least medium; otherwise low. Open questions = registry-declared coverage gaps + rejected sources + extraction failures + unresolved reconciles + uncertain conditions. |
| G13 | Version facts are only prompt inputs; changes in them never become risks. | Rule-derived paths: for each `version_facts` field whose value differs between the current and target metadata (Node engines, Python `requires_python`, React peer range), emit a `derived_by: rule` path with JSON-path evidence on both sides. These are merged with LLM paths about the same runtime. A prose version that contradicts metadata goes to `sources_with_disagreements` (L6). |
| G14 | Context items never reach the output. | Triage `context` items in risk-heavy sections (removed, deprecated, incompatible, urgent, requirements, changed) become `context_facts`. Quote = opening sentence (verbatim), `why_not_risk` = triage reason. Items in "new features" sections are counted only. |
| G15 | When does a validator error remove something, and when does it stop the run? | Pipeline mode repairs deterministically: evidence with a failed quote is dropped; a condition with no evidence left is dropped; a path missing its version or app-side condition is dropped. Every drop goes to `intermediate/rejected.jsonl` and is counted. Gate mode (`urx validate`) fails on any error. Final outputs must have zero errors. |
| G16 | Gold matching by "symbol overlap" cannot work with free-text gold symbols ("Python 3.6, 3.7"). | Gold items use `match`: a list of term groups (DNF); a path matches if every term of any group appears case-insensitively in its text blob, and `release` is equal, in a list, or `"*"`. An optional `risk_types` filter applies. Matching is deterministic; no LLM matcher. |
| G17 | Gold sets only cover 2 of 5 upgrades. | Small gold sets for React, PostgreSQL and Next.js, written from official docs **before** the first extraction run and committed separately. They are not exhaustive, so strict precision is a lower bound. |
| G18 | "Adjudicated valid" precision and calibration need human labels that do not exist. | Report strict precision (gold-matched / extracted) and estimated precision (gold-matched + paths that an LLM precision judge, `precision_judge.v1`, accepts as specific, checkable and supported). Judge-accepted paths are flagged for human review in the UI. Calibration uses the same validity label. |
| G19 | Judge calibration needs 50 human labels. | Synthetic adversarial set: verified quotes are turned into claims (identity → supported) and deterministic mutations (number changed, negation, swapped symbol → not supported). Report accuracy and Cohen's κ. A human label file, if added, is used too. |
| G20 | The condition-field accuracy sample needs human labels. | Replaced by automated field-consistency checks: version conditions carry a canonical range; `in_range/less_than/greater_than` must carry a parseable version; `present/absent` must name a symbol; app-side conditions with a literal symbol need search queries. Reported as a rate. |
| G21 | The stability metric needs two cold runs over 5 upgrades (cost). | Run cold on React (the smallest upgrade) only; report path-ID Jaccard and the matched-gold delta. |
| G22 | Linker requires Postgres tsvector and pgvector, which the stack never sets up. | An in-process BM25 index over change items (pure Python). Dense embeddings are out of scope (listed under "more time"). |
| G23 | No UI, no run tracking. | Section 17.3. |
| G24 | Cost control is undefined. | Thread pool (8 workers); triage batches of 20; the judge is batched per path; per-stage token and cost estimates go to `run_log.jsonl`; LLM cache in `llm_cache/`. |
| G25 | Some TDD features exceed the 4-hour assignment budget. | Cut and listed as future work: discovery agent (A6), Ollama provider, dense retrieval, tier-2 Trac/GitHub issue mining, gold export from overrides. Anthropic (default) and OpenAI providers are implemented. |
| G26 | `required` vs `role` mapping is unstated. | `required = (role == "required")`. `disqualifying` means "if this holds, the path does not apply"; `alternative` means at least one alternative must hold. |

### 17.3 User interface and run tracking (new)

A FastAPI server (`urx serve`, bound to `127.0.0.1`) exposes the outputs; a React + Vite + TypeScript app in `ui/` consumes them.

| View | Content |
|---|---|
| Overview | One card per upgrade: risk counts by level, overall confidence, validator errors/warnings, recall against gold, last run. |
| Upgrade | Risk paths with filters (level, type, surface, confidence, review status, text). Path detail shows conditions (role, operator, expected value, confidence, judge verdict), verbatim evidence with a "show in source" context view, actions, search queries, and a Mermaid graph. Tabs for sources (used/rejected, hash, pinned ref), evidence summary and open questions, context facts and disqualified candidates, and a pipeline funnel (items → triaged risk → extracted → linked → composed → final). |
| Review | Accept/reject/edit buttons write `review/overrides.yaml`, which is applied on the next run. |
| Evals | Every metric in 17.4 with its target and pass/fail, per-gold-item matched/missed lists, and ablation results. |
| Runs | Start a run (online or offline) and follow stage events live from `outputs/<slug>/run_log.jsonl`. |

### 17.4 Evaluation metrics (replaces 12.3)

| Metric | Definition | Target | Gate type |
|---|---|---|---|
| Grounding rate | verified quotes / quotes in final outputs, recomputed independently from `cache/` | 1.00 | hard (pytest) |
| Validator errors | errors across all 5 final models | 0 | hard (pytest) |
| Structural completeness | paths with ≥ 1 version and ≥ 1 app/deployment condition / paths | 1.00 | hard (pytest) |
| Risk recall | gold risks matched by a path / gold risks, per upgrade | ≥ 0.80 per upgrade, ≥ 0.85 overall | hard (pytest) |
| Strict precision | paths matching any gold risk / paths | report (lower bound) | report |
| Estimated precision | (gold-matched + precision-judge-valid) / paths | ≥ 0.85 | soft |
| Classification accuracy | gold items found in the right bucket (risk / context / disqualified) / gold items found | ≥ 0.85 | hard (pytest) |
| Level agreement | matched gold risks whose level is within one step of `min_level` | ≥ 0.80 | soft |
| Field consistency | conditions passing the G20 checks / conditions | ≥ 0.95 | hard (pytest) |
| Calibration | valid-rate(high) ≥ valid-rate(medium) ≥ valid-rate(low) | must hold | soft |
| Judge accuracy | accuracy and κ on the synthetic adversarial set (G19) | ≥ 0.90, κ ≥ 0.8 | soft |
| Drift false-accept | exact vs fuzzy (≥ 0.9 ratio) on injected-drift quotes | exact = 0.00 | hard (pytest) |
| Stability | path-ID Jaccard, React cold rerun | ≥ 0.80 | soft |
| Cost / latency | tokens, estimated USD, wall time per stage and upgrade | report | report |

"Hard" metrics are asserted in `tests/test_eval_gates.py` against the committed outputs; "soft" metrics are reported in `eval/results.md` and shown in the UI.

### 17.5 Registry additions

`known_releases: [..]`, `coverage_gaps: [..]` (text that becomes open questions), per-source `select`, `within`, `release`, `release_from_heading`, `revert_scan`, `patch_max`, `future_removal`, and `cross_project: {field: Project}` on `version_facts` (R7).

---

## Appendix A: Django 3.2→4.2 gold seed

| gold_id | release | symbols | kind | min_level |
|---|---|---|---|---|
| dj_python | 4.0/4.2 | Python 3.6, 3.7 | risk | critical |
| dj_pg12 | 4.2 | PostgreSQL 12 | risk | critical |
| dj_mysql8 | 4.2 | MySQL 8 | risk | critical |
| dj_mariadb104 | 4.2 | MariaDB 10.4 | risk | critical |
| dj_oracle19 | 4.0 | Oracle 19c | risk | high |
| dj_sqlite321 | 4.2 | SQLite 3.21.0 | risk | high |
| dj_psycopg2 | 4.0 | psycopg2 2.8.4 | risk | medium |
| dj_asgiref | 4.2 | asgiref 3.6.0 | risk | medium |
| dj_csrf_scheme | 4.0 | CSRF_TRUSTED_ORIGINS | risk | high |
| dj_csrf_origin | 4.0 | Origin, CSRF_COOKIE_DOMAIN | risk | high |
| dj_csrf_masked | 4.1 | CSRF_COOKIE_MASKED | risk | medium |
| dj_xss_header | 4.0 | SECURE_BROWSER_XSS_FILTER, X-XSS-Protection | risk | low |
| dj_sha1 | 4.0 | DEFAULT_HASHING_ALGORITHM | risk | high |
| dj_removed_text | 4.0 | force_text, smart_text | risk | high |
| dj_removed_ugettext | 4.0 | ugettext, ugettext_lazy, ungettext | risk | high |
| dj_removed_url | 4.0 | django.conf.urls.url | risk | high |
| dj_removed_is_ajax | 4.0 | is_ajax | risk | high |
| dj_removed_nullbool | 4.0 | NullBooleanField | risk | high |
| dj_removed_ifequal | 4.0 | ifequal, ifnotequal | risk | high |
| dj_removed_is_safe_url | 4.0 | is_safe_url | risk | medium |
| dj_removed_pg_jsonfield | 4.0 | django.contrib.postgres.fields.JSONField | risk | high |
| dj_removed_reset_days | 4.0 | PASSWORD_RESET_TIMEOUT_DAYS | risk | medium |
| dj_memcachedcache | 4.1 | MemcachedCache | risk | high |
| dj_default_app_config | 4.1 | default_app_config | risk | medium |
| dj_emailvalidator_whitelist | 4.1 | whitelist, domain_whitelist | risk | low |
| dj_requires_system_checks | 4.1 | requires_system_checks | risk | low |
| dj_zoneinfo | 4.0 | zoneinfo, pytz, USE_DEPRECATED_PYTZ | risk | medium |
| dj_use_l10n | 4.0 | USE_L10N | risk | medium |
| dj_deleteview | 4.0 | DeleteView, form_valid | risk | high |
| dj_update_fields | 4.2 | update_or_create, update_fields | risk | high |
| dj_reverse_fk | 4.1 | ValueError, related managers | risk | medium |
| dj_smtp_tls | 4.2 | EmailBackend, ssl_context | risk | medium |
| dj_group_by_alias | 4.0→4.2 | get_group_by_cols | risk | low |
| dj_admin_search | 4.1 | search_fields | risk | low |
| dj_mysql_rawsql | 4.2 | RawSQL | risk | medium |
| dj_usercreationform | 4.2 | UserCreationForm | risk | low |
| dj_ctx_storages | 4.2 | DEFAULT_FILE_STORAGE, STORAGES | context | – |
| dj_ctx_index_together | 4.2 | index_together | context | – |
| dj_ctx_psycopg3 | 4.2 | psycopg | context | – |
| dj_disq_manager_cache | 4.1 | related managers cached (reverted 4.1.2) | disqualified | – |

## Appendix B: Kubernetes 1.23→1.29 gold seed

| gold_id | release | symbols | kind | min_level |
|---|---|---|---|---|
| k8s_skew_cp | path | kube-apiserver one minor | risk | critical |
| k8s_skew_kubelet | path | kubelet < 1.25 two minors | risk | high |
| k8s_dockershim | 1.24 | dockershim | risk | critical |
| k8s_sa_tokens | 1.24 | LegacyServiceAccountTokenNoAutoGeneration | risk | high |
| k8s_topology_spread | 1.24 | topologySpreadConstraints | risk | medium |
| k8s_master_label | 1.24 | node-role.kubernetes.io/master | risk | medium |
| k8s_flag_capabilities | 1.24 | --experimental-check-node-capabilities-before-mount | risk | low |
| k8s_gate_rbd_rename | 1.24 | csiMigrationRBD | risk | low |
| k8s_cronjob | 1.25 | batch/v1beta1 CronJob | risk | critical |
| k8s_endpointslice | 1.25 | discovery.k8s.io/v1beta1 | risk | high |
| k8s_events | 1.25 | events.k8s.io/v1beta1 | risk | high |
| k8s_hpa_v2beta1 | 1.25 | autoscaling/v2beta1 | risk | high |
| k8s_pdb | 1.25 | policy/v1beta1 PodDisruptionBudget | risk | high |
| k8s_pdb_selector | 1.25 | spec.selector {} | risk | high |
| k8s_psp | 1.25 | PodSecurityPolicy | risk | critical |
| k8s_runtimeclass | 1.25 | node.k8s.io/v1beta1 | risk | medium |
| k8s_intree_vol_125 | 1.25 | flocker, quobyte, storageos | risk | high |
| k8s_registry | 1.25 | registry.k8s.io, k8s.gcr.io | risk | medium |
| k8s_flowcontrol_b1 | 1.26 | flowcontrol.apiserver.k8s.io/v1beta1 | risk | high |
| k8s_hpa_v2beta2 | 1.26 | autoscaling/v2beta2 | risk | high |
| k8s_openstack | 1.26 | OpenStack in-tree, cinder | risk | critical |
| k8s_glusterfs | 1.26 | GlusterFS | risk | critical |
| k8s_csistoragecap | 1.27 | storage.k8s.io/v1beta1 CSIStorageCapacity | risk | medium |
| k8s_aws_intree | 1.27 | AWS in-tree, EBS | risk | critical |
| k8s_ipv6_gate | 1.27 | IPv6DualStack | risk | low |
| k8s_restart_always | 1.27 | RestartPolicy=Always Succeeded | risk | medium |
| k8s_scheduler_plugin | 1.28 | EventsToRegister, ClusterEventWithHint | risk | high |
| k8s_flowcontrol_b2 | 1.29 | flowcontrol.apiserver.k8s.io/v1beta2 | risk | high |
| k8s_super_admin | 1.29 | super-admin.conf, kubeadm:cluster-admins | risk | medium |
| k8s_kubeadm_plan_config | 1.29 | kubeadm upgrade plan --config | risk | low |
| k8s_ctx_kms_gcm | 1.25 | AES-GCM | context | – |
| k8s_ctx_ginkgo | 1.25 | Ginkgo v2 | context | – |
| k8s_ctx_ceph | 1.28 | CephFS, RBD deprecated | context | – |

---

## Appendix C: Cursor rules (`.cursor/rules/urx.mdc`)

```
---
description: URX project rules
alwaysApply: true
---
- Read TDD.md sections 0-3 before changing code. Follow the milestone order in section 14.
- Never add, rename or remove fields/enums from the assignment schema (TDD 6.1). Only extensions from 6.2.
- Never hardcode source URLs in code; they live in registry/*.yaml.
- Never fabricate quotes, versions or URLs in code, fixtures, prompts or outputs.
- Every evidence quote must pass validate.py exact-match against cache/. No fuzzy matching.
- Confidence is computed by rubric.py only. LLM outputs never include confidence.
- Deterministic first: parsing, planning, composition, validation and rubric contain no LLM calls.
- Write the tests in TDD section 13 before implementing each component; every validator rule needs a negative test.
- LLM calls go through llm/client.py with caching; temperature 0; prompt files are versioned.
- The pipeline must run offline from cache/ and llm_cache/.
- Do not scan real repositories; scan.py runs only on fixtures/demo_app.
- Every output must include the disclaimer: "Documentation-derived risk conditions; not a migration plan."
```
