import { useCallback, useEffect, useMemo, useState } from 'react'
import { Link, useParams, useSearchParams } from 'react-router-dom'
import { api, type Override, type RiskModel, type RunEvent } from '../api'
import PathDetail from '../components/PathDetail'
import { Badge, ErrorBox, LEVELS, Loading, PageHeader, Tabs } from '../components/ui'

type Tab = 'paths' | 'sources' | 'evidence' | 'context' | 'pipeline' | 'report'

export default function UpgradePage() {
  const { slug = '' } = useParams()
  const [params, setParams] = useSearchParams()
  const [model, setModel] = useState<RiskModel | null>(null)
  const [overrides, setOverrides] = useState<Override[]>([])
  const [err, setErr] = useState<string | null>(null)
  const tab = (params.get('tab') as Tab) || 'paths'
  const selected = params.get('path')

  const load = useCallback(() => {
    api.model(slug).then(setModel).catch((e) => setErr(String(e)))
    api.overrides().then(setOverrides).catch(() => {})
  }, [slug])
  useEffect(load, [load])

  const set = (k: string, v: string | null) => {
    const p = new URLSearchParams(params)
    if (v === null) p.delete(k)
    else p.set(k, v)
    setParams(p, { replace: true })
  }

  if (err) return <ErrorBox error={err} />
  if (!model) return <Loading what="risk model" />
  const path = model.risk_paths.find((p) => p.path_id === selected)
  const ov = (id: string) => overrides.find((o) => o.id === id)

  const review = async (decision: 'accept' | 'reject' | null, note: string) => {
    if (!path) return
    const next = decision
      ? await api.saveOverride({ id: path.path_id, decision, note, reviewer: 'ui' })
      : await api.deleteOverride(path.path_id)
    setOverrides(next)
  }

  return (
    <div>
      <PageHeader
        title={
          <>
            {model.project} <span className="muted">{model.current_version} → {model.target_version}</span>
          </>
        }
        subtitle={
          <span className="meta">
            <Badge kind={model.overall_confidence}>{model.overall_confidence} confidence</Badge>
            <span>releases {model.plan.releases.join(', ')}</span>
            <span>
              {model.pipeline.validation.errors} errors · {model.pipeline.validation.warnings} warnings
            </span>
          </span>
        }
      />
      <details className="summary">
        <summary>Summary</summary>
        <p>{model.summary}</p>
        <p className="disclaimer">{model.disclaimer}</p>
      </details>
      {model.requires_upgrades.length > 0 && (
        <div className="callout">
          {model.requires_upgrades.map((r) => (
            <div key={r.model_ref}>
              Requires <b>{r.project} {r.current_version} → {r.target_version}</b>: {r.reason}{' '}
              <Link to={`/upgrade/${r.model_ref}`}>open that model</Link>
            </div>
          ))}
        </div>
      )}
      <Tabs<Tab>
        value={tab}
        onChange={(t) => set('tab', t)}
        tabs={[
          ['paths', 'Risk paths', model.risk_paths.length],
          ['evidence', 'Evidence', model.open_questions.length],
          ['context', 'Context', model.context_facts.length + model.disqualified_candidates.length],
          ['sources', 'Sources', model.source_inventory.length],
          ['pipeline', 'Pipeline'],
          ['report', 'Report'],
        ]}
      />
      {tab === 'paths' && <PathsTab model={model} overrides={overrides} selected={selected} onSelect={(id) => set('path', id)} />}
      {tab === 'sources' && <SourcesTab model={model} />}
      {tab === 'evidence' && <EvidenceTab model={model} onSelect={(id) => { set('tab', 'paths'); set('path', id) }} />}
      {tab === 'context' && <ContextTab model={model} />}
      {tab === 'pipeline' && <PipelineTab slug={slug} model={model} />}
      {tab === 'report' && <ReportTab slug={slug} />}
      {path && tab === 'paths' && (
        <PathDetail
          path={path}
          slug={slug}
          model={model}
          override={ov(path.path_id)}
          onReview={review}
          onClose={() => set('path', null)}
        />
      )}
    </div>
  )
}

function PathsTab({
  model,
  overrides,
  selected,
  onSelect,
}: {
  model: RiskModel
  overrides: Override[]
  selected: string | null
  onSelect: (id: string) => void
}) {
  const [q, setQ] = useState('')
  const [levels, setLevels] = useState<Set<string>>(new Set())
  const [conf, setConf] = useState('')
  const [type, setType] = useState('')
  const [release, setRelease] = useState('')
  const [flagged, setFlagged] = useState(false)
  const [more, setMore] = useState(false)
  const types = useMemo(() => [...new Set(model.risk_paths.map((p) => p.risk_type))].sort(), [model])
  const releases = useMemo(() => [...new Set(model.risk_paths.map((p) => p.introduced_in))].sort(), [model])
  const rows = model.risk_paths
    .filter((p) => !levels.size || levels.has(p.risk_level))
    .filter((p) => !conf || p.confidence === conf)
    .filter((p) => !type || p.risk_type === type)
    .filter((p) => !release || p.introduced_in === release)
    .filter((p) => !flagged || p.review_flags.length > 0)
    .filter((p) => !q || JSON.stringify(p).toLowerCase().includes(q.toLowerCase()))
    .sort((a, b) => LEVELS.indexOf(a.risk_level) - LEVELS.indexOf(b.risk_level) || a.introduced_in.localeCompare(b.introduced_in))
  const toggle = (l: string) => {
    const s = new Set(levels)
    if (s.has(l)) s.delete(l)
    else s.add(l)
    setLevels(s)
  }
  return (
    <div>
      <div className="filters">
        <input placeholder="Search paths, symbols, quotes…" value={q} onChange={(e) => setQ(e.target.value)} />
        {LEVELS.map((l) => (
          <button key={l} className={`chip ${levels.has(l) ? `on lv-bg-${l}` : ''}`} onClick={() => toggle(l)}>
            {l}
          </button>
        ))}
        <button className={`chip ${more || conf || type || release || flagged ? 'chip-active' : ''}`} onClick={() => setMore(!more)}>
          More filters
        </button>
        <span className="muted small push">{rows.length} shown</span>
      </div>
      {more && (
      <div className="filters sub">
        <select value={conf} onChange={(e) => setConf(e.target.value)}>
          <option value="">any confidence</option>
          <option>high</option>
          <option>medium</option>
          <option>low</option>
        </select>
        <select value={type} onChange={(e) => setType(e.target.value)}>
          <option value="">any type</option>
          {types.map((t) => (
            <option key={t}>{t}</option>
          ))}
        </select>
        <select value={release} onChange={(e) => setRelease(e.target.value)}>
          <option value="">any release</option>
          {releases.map((t) => (
            <option key={t}>{t}</option>
          ))}
        </select>
        <label className="small">
          <input type="checkbox" checked={flagged} onChange={(e) => setFlagged(e.target.checked)} /> flagged only
        </label>
      </div>
      )}
      <div className="card flush">
      <table className="table plain">
        <thead>
          <tr>
            <th>Level</th>
            <th>Path</th>
            <th>Release</th>
            <th>Confidence</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {rows.map((p) => {
            const o = overrides.find((x) => x.id === p.path_id)
            return (
              <tr key={p.path_id} className={p.path_id === selected ? 'sel' : ''} onClick={() => onSelect(p.path_id)}>
                <td>
                  <Badge kind={p.risk_level}>{p.risk_level}</Badge>
                </td>
                <td>
                  <div className="pname">{p.path_name}</div>
                  <div className="muted small">
                    <code>{p.primary_symbol}</code> · {p.risk_type.replace(/_/g, ' ')}
                  </div>
                </td>
                <td>{p.introduced_in}</td>
                <td className="small">{p.confidence}</td>
                <td className="right">
                  {o ? <Badge kind={o.decision === 'accept' ? 'ok' : 'bad'}>{o.decision}</Badge> : null}
                  {p.review_flags.length > 0 && <Badge kind="flag" title={p.review_flags.join(', ')}>⚑ {p.review_flags.length}</Badge>}
                </td>
              </tr>
            )
          })}
        </tbody>
      </table>
      </div>
    </div>
  )
}

function SourcesTab({ model }: { model: RiskModel }) {
  return (
    <table className="table">
      <thead>
        <tr>
          <th>Source</th>
          <th>Type</th>
          <th>Tier</th>
          <th>Release</th>
          <th>Status</th>
          <th>Pinned ref</th>
          <th>Hash</th>
        </tr>
      </thead>
      <tbody>
        {model.source_inventory.map((s) => (
          <tr key={s.source_id} className={s.status === 'rejected' ? 'dim' : ''}>
            <td>
              <a href={s.url} target="_blank" rel="noreferrer">
                {s.title}
              </a>
              <div className="muted small">
                <code>{s.source_id}</code> · {s.why_relevant}
              </div>
            </td>
            <td className="small">{s.source_type}</td>
            <td>{s.authority_tier}</td>
            <td>{s.release ?? '–'}</td>
            <td>
              {s.status === 'used' ? <Badge kind="ok">used</Badge> : <Badge kind="bad" title={s.rejection_reason ?? ''}>rejected</Badge>}
              {s.rejection_reason && <div className="small muted">{s.rejection_reason}</div>}
            </td>
            <td className="small mono">{s.pinned_ref.slice(0, 14)}</td>
            <td className="small mono">{s.content_hash.slice(0, 18)}</td>
          </tr>
        ))}
      </tbody>
    </table>
  )
}

function EvidenceTab({ model, onSelect }: { model: RiskModel; onSelect: (id: string) => void }) {
  const es = model.evidence_summary
  const name = (id: string) => model.risk_paths.find((p) => p.path_id === id)?.path_name ?? id
  const list = (ids: string[]) => (
    <ul>
      {ids.map((id) => (
        <li key={id}>
          <button className="link" onClick={() => onSelect(id)}>
            {name(id)}
          </button>
        </li>
      ))}
    </ul>
  )
  return (
    <div className="cols">
      <div className="card">
        <h3>High confidence ({es.high_confidence_risks.length})</h3>
        {list(es.high_confidence_risks)}
        <h3>Medium confidence ({es.medium_confidence_risks.length})</h3>
        {list(es.medium_confidence_risks)}
        <h3>Low confidence or disputed ({es.low_confidence_or_disputed_risks.length})</h3>
        {list(es.low_confidence_or_disputed_risks)}
      </div>
      <div>
        <div className="card">
          <h3>Sources with disagreements ({es.sources_with_disagreements.length})</h3>
          {es.sources_with_disagreements.map((d, i) => (
            <div key={i} className="disagree">
              <b>{d.topic}</b>
              <div className="small muted">{d.sources.join(' vs ')}</div>
              <p>{d.detail}</p>
              <p className="small">
                <b>Resolution:</b> {d.resolution}
              </p>
            </div>
          ))}
          {!es.sources_with_disagreements.length && <p className="muted">None detected.</p>}
        </div>
        <div className="card">
          <h3>Open questions ({model.open_questions.length})</h3>
          <ul>
            {model.open_questions.map((q, i) => (
              <li key={i}>{q}</li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  )
}

function ContextTab({ model }: { model: RiskModel }) {
  return (
    <div className="cols">
      <div className="card">
        <h3>Context facts ({model.context_facts.length})</h3>
        <p className="muted small">True statements about the upgrade that are not standalone risks (deprecations that still work, future removals, background).</p>
        {model.context_facts.map((f) => (
          <div key={f.fact_id} className="fact">
            <div>
              <Badge kind="info">{f.introduced_in}</Badge> {f.statement}
            </div>
            <div className="small muted">{f.why_not_risk}</div>
          </div>
        ))}
      </div>
      <div className="card">
        <h3>Disqualified candidates ({model.disqualified_candidates.length})</h3>
        <p className="muted small">Changes that look risky but are reverted, superseded, or outside the walked release range.</p>
        {model.disqualified_candidates.map((d) => (
          <div key={d.candidate_id} className="fact">
            <div>{d.statement}</div>
            <div className="small warn-t">{d.reason}</div>
            {d.evidence.map((e, i) => (
              <blockquote key={i} className="small">
                {e.source_id}: {e.quote ?? e.quote_or_summary}
              </blockquote>
            ))}
          </div>
        ))}
      </div>
    </div>
  )
}

function PipelineTab({ slug, model }: { slug: string; model: RiskModel }) {
  const [log, setLog] = useState<RunEvent[]>([])
  const [rejected, setRejected] = useState<Record<string, unknown>[]>([])
  useEffect(() => {
    api.runlog(slug).then(setLog)
    api.intermediate<Record<string, unknown>>(slug, 'rejected').then(setRejected)
  }, [slug])
  const f = model.pipeline.funnel
  const max = Math.max(...Object.values(f).map(Number), 1)
  const usage = Object.entries(model.pipeline.usage)
  const lastRun = log.filter((e) => e.run_id === model.pipeline.run_id)
  return (
    <div>
      <div className="cols">
        <div className="card">
          <h3>Funnel</h3>
          {Object.entries(f).map(([k, v]) => (
            <div key={k} className="funnel-row">
              <span className="small">{k.replace(/_/g, ' ')}</span>
              <div className="funnel-bar" style={{ width: `${Math.max(2, (100 * Number(v)) / max)}%` }} />
              <b>{v}</b>
            </div>
          ))}
          <h3>Judge</h3>
          <div className="kv">
            {Object.entries(model.pipeline.judge || {}).map(([k, v]) => (
              <span key={k}>
                {k}: <b>{v}</b>
              </span>
            ))}
          </div>
          <h3>Models</h3>
          <div className="kv">
            {Object.entries(model.pipeline.models).map(([k, v]) => (
              <span key={k}>
                {k}: <code>{v}</code>
              </span>
            ))}
          </div>
        </div>
        <div className="card">
          <h3>LLM usage by stage</h3>
          <table className="table compact">
            <thead>
              <tr>
                <th>Stage</th>
                <th>Calls</th>
                <th>Cache hits</th>
                <th>In tok</th>
                <th>Out tok</th>
                <th>$ this run</th>
                <th>$ to produce</th>
              </tr>
            </thead>
            <tbody>
              {usage.map(([k, u]) => (
                <tr key={k}>
                  <td>{k}</td>
                  <td>{u.calls}</td>
                  <td>{u.cache_hits}</td>
                  <td>{u.input_tokens.toLocaleString()}</td>
                  <td>{u.output_tokens.toLocaleString()}</td>
                  <td>{u.usd_estimate.toFixed(3)}</td>
                  <td>{(u.usd_full ?? 0).toFixed(3)}</td>
                </tr>
              ))}
            </tbody>
          </table>
          <h3>Stage timings (s)</h3>
          <div className="kv">
            {Object.entries(model.pipeline.timings_s).map(([k, v]) => (
              <span key={k}>
                {k}: <b>{v.toFixed(1)}</b>
              </span>
            ))}
          </div>
          <h3>Validation</h3>
          <div className="kv">
            {Object.entries(model.pipeline.validation.by_code || {}).map(([k, v]) => (
              <span key={k}>
                <code>{k}</code>: {v}
              </span>
            ))}
            {!Object.keys(model.pipeline.validation.by_code || {}).length && <span className="muted">clean</span>}
          </div>
        </div>
      </div>
      <div className="card">
        <h3>Rejected extractions ({rejected.length})</h3>
        <p className="muted small">Drafts dropped by deterministic checks (no app-side condition, unverifiable quotes, repair drops).</p>
        <table className="table compact">
          <tbody>
            {rejected.slice(0, 200).map((r, i) => (
              <tr key={i}>
                <td className="small mono">{String(r.item_id ?? r.path_id ?? '')}</td>
                <td className="small">{String(r.kind ?? '')}</td>
                <td className="small">{String(r.path_name ?? r.statement ?? r.quote ?? '')}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <div className="card">
        <h3>Run log (run {model.pipeline.run_id})</h3>
        <pre className="code log">
          {lastRun.map((e) => `${e.ts}  +${e.elapsed_s.toFixed(1)}s  ${e.event}${e.stage ? ' ' + e.stage : ''}${e.seconds !== undefined ? ` (${Number(e.seconds).toFixed(1)}s)` : ''}`).join('\n')}
        </pre>
      </div>
    </div>
  )
}

function ReportTab({ slug }: { slug: string }) {
  const [md, setMd] = useState<string | null>(null)
  useEffect(() => {
    fetch(`/api/upgrades/${slug}/report`).then((r) => r.text()).then(setMd)
  }, [slug])
  if (md === null) return <Loading what="report" />
  return <pre className="code report">{md}</pre>
}
