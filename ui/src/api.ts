export type Level = 'critical' | 'high' | 'medium' | 'low' | 'unknown'
export type Conf = 'high' | 'medium' | 'low'

export interface Evidence {
  source_id: string
  source_type: string
  quote_or_summary: string
  relevance: string
  quote: string | null
  verified: boolean
  json_path: string | null
  expected: string | null
}

export interface Condition {
  condition_id: string
  statement: string
  category: string
  required: boolean
  operator: string
  expected_value: unknown
  evidence: Evidence[]
  confidence: Conf
  ambiguities: string[]
  role: string
  derived_by: string
  search_queries: { tool: string; query: string }[]
  judge: { verdict: string; missing: string } | null
}

export interface RiskPath {
  path_id: string
  path_name: string
  risk_type: string
  risk_level: Level
  affected_surface: string
  description: string
  conditions: Condition[]
  suggested_actions: string[]
  confidence: Conf
  applies_to: { cluster_type: string | null; upgrade_method: string | null; from_versions: string | null } | null
  fires_at: string
  introduced_in: string
  primary_symbol: string
  symbols: string[]
  superseded_by: string | null
  reverted_in: string | null
  merged_from: string[]
  source_item_ids: string[]
  review_status: string
  review_flags: string[]
}

export interface SourceRecord {
  source_id: string
  title: string
  url: string
  source_type: string
  retrieved_at: string
  why_relevant: string
  authority_tier: number
  content_hash: string
  pinned_ref: string
  status: 'used' | 'rejected'
  rejection_reason: string | null
  release: string | null
}

export interface RiskModel {
  project: string
  current_version: string
  target_version: string
  disclaimer: string
  summary: string
  source_inventory: SourceRecord[]
  risk_paths: RiskPath[]
  open_questions: string[]
  overall_confidence: Conf
  evidence_summary: {
    high_confidence_risks: string[]
    medium_confidence_risks: string[]
    low_confidence_or_disputed_risks: string[]
    sources_with_disagreements: { topic: string; sources: string[]; detail: string; resolution: string }[]
    open_questions: string[]
  }
  context_facts: { fact_id: string; statement: string; introduced_in: string; evidence: Evidence[]; why_not_risk: string; fires_at: string | null }[]
  disqualified_candidates: { candidate_id: string; statement: string; reason: string; evidence: Evidence[] }[]
  requires_upgrades: { project: string; current_version: string; target_version: string; reason: string; model_ref: string }[]
  plan: { releases: string[]; future_releases: string[]; mode: string; hops: number }
  pipeline: {
    run_id: string
    generated_at: string
    models: Record<string, string>
    funnel: Record<string, number>
    judge: Record<string, number>
    usage: Record<
      string,
      { calls: number; cache_hits: number; input_tokens: number; output_tokens: number; usd_estimate: number; usd_full?: number }
    >
    timings_s: Record<string, number>
    validation: { errors: number; warnings: number; by_code: Record<string, number> }
  }
}

export interface UpgradeSummary {
  slug: string
  exists: boolean
  project?: string
  current_version?: string
  target_version?: string
  paths?: number
  by_level?: Record<string, number>
  by_confidence?: Record<string, number>
  by_type?: Record<string, number>
  overall_confidence?: Conf
  validation?: { errors: number; warnings: number }
  generated_at?: string
  funnel?: Record<string, number>
  usd_estimate?: number
  usd_full?: number
  context_facts?: number
  disqualified?: number
  open_questions?: number
  sources_used?: number
  sources_rejected?: number
  review_flags?: number
  recall?: [number, number]
  strict_precision?: [number, number]
  estimated_precision?: [number, number]
  grounding?: [number, number]
}

export interface Metric {
  name: string
  value: unknown
  display: string
  target: unknown
  pass: boolean | null
  gate: 'hard' | 'soft' | 'report'
}

export interface GoldItem {
  gold_id: string
  kind: string
  min_level: string | null
  hits: Record<string, string[]>
  found: boolean
  correct_bucket: boolean
  extracted_level: string | null
}

export interface EvalResults {
  metrics: Metric[]
  per_upgrade: Record<string, Record<string, unknown> & { gold_items?: GoldItem[]; project: string }>
  extra: Record<string, unknown>
}

export interface Override {
  id: string
  decision: 'accept' | 'reject' | 'edit'
  edits: Record<string, string>
  reviewer: string
  note: string
  at: string
}

export interface RunEvent {
  ts: string
  elapsed_s: number
  event: string
  stage?: string
  seconds?: number
  [k: string]: unknown
}

export interface Run {
  run_id: string
  slug: string
  status: 'running' | 'ok' | 'error'
  started: string
  ended?: string
  project: string
  current_version: string
  target_version: string
  offline: boolean
  error?: string
  events?: RunEvent[]
}

async function req<T>(url: string, init?: RequestInit): Promise<T> {
  const r = await fetch(url, init)
  if (!r.ok) throw new Error(`${r.status} ${await r.text()}`)
  const ct = r.headers.get('content-type') || ''
  return (ct.includes('json') ? r.json() : r.text()) as Promise<T>
}

const json = (body: unknown): RequestInit => ({
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(body),
})

export const api = {
  upgrades: () => req<UpgradeSummary[]>('/api/upgrades'),
  model: (slug: string) => req<RiskModel>(`/api/upgrades/${slug}`),
  graph: (slug: string, pathId: string) => req<string>(`/api/upgrades/${slug}/paths/${pathId}/graph`),
  evidence: (slug: string, sourceId: string, quote: string) =>
    req<{ found: boolean; before?: string; match?: string; after?: string; source: SourceRecord }>(
      `/api/upgrades/${slug}/evidence?source_id=${encodeURIComponent(sourceId)}&quote=${encodeURIComponent(quote)}`,
    ),
  intermediate: <T,>(slug: string, name: string) => req<T[]>(`/api/upgrades/${slug}/intermediate/${name}`),
  composeLog: (slug: string) => req<Record<string, unknown[]>>(`/api/upgrades/${slug}/compose_log`),
  runlog: (slug: string) => req<RunEvent[]>(`/api/upgrades/${slug}/runlog`),
  evalResults: () => req<EvalResults>('/api/eval'),
  runEval: () => req<EvalResults>('/api/eval/run', { method: 'POST' }),
  registry: () => req<{ project: string; known_releases: string[]; mode: string }[]>('/api/registry'),
  runs: () => req<Run[]>('/api/runs'),
  run: (id: string) => req<Run>(`/api/runs/${id}`),
  startRun: (body: { project: string; current_version: string; target_version: string; offline: boolean }) =>
    req<Run>('/api/runs', json(body)),
  overrides: () => req<Override[]>('/api/overrides'),
  saveOverride: (o: Partial<Override>) => req<Override[]>('/api/overrides', json(o)),
  deleteOverride: (id: string) => req<Override[]>(`/api/overrides/${encodeURIComponent(id)}`, { method: 'DELETE' }),
}
