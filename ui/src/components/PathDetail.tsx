import { useEffect, useState } from 'react'
import { api, type Condition, type Evidence, type Override, type RiskModel, type RiskPath } from '../api'
import Mermaid from './Mermaid'
import { Badge } from './ui'

function EvidenceRow({ slug, ev, model }: { slug: string; ev: Evidence; model: RiskModel }) {
  const [ctx, setCtx] = useState<{ before?: string; match?: string; after?: string; found: boolean } | null>(null)
  const src = model.source_inventory.find((s) => s.source_id === ev.source_id)
  const show = () => {
    if (ctx) return setCtx(null)
    if (ev.quote) api.evidence(slug, ev.source_id, ev.quote).then(setCtx)
  }
  return (
    <div className="evidence">
      <div className="ev-head">
        <a href={src?.url} target="_blank" rel="noreferrer" title={src?.title}>
          {ev.source_id}
        </a>
        <Badge kind={`tier${src?.authority_tier ?? 3}`}>tier {src?.authority_tier ?? '?'}</Badge>
        {ev.verified ? <Badge kind="ok">verified</Badge> : <Badge kind="bad">unverified</Badge>}
        {ev.json_path && <Badge kind="info">json: {ev.json_path}</Badge>}
        {ev.quote && (
          <button className="link" onClick={show}>
            {ctx ? 'hide source' : 'show in source'}
          </button>
        )}
      </div>
      <blockquote>{ev.quote ?? ev.quote_or_summary}</blockquote>
      {ev.expected && <div className="small muted">expected value: <code>{ev.expected}</code></div>}
      <div className="small muted">{ev.relevance}</div>
      {ctx &&
        (ctx.found ? (
          <pre className="source-ctx">
            …{ctx.before}
            <mark>{ctx.match}</mark>
            {ctx.after}…
          </pre>
        ) : (
          <div className="error-box">Quote not found in cached source.</div>
        ))}
    </div>
  )
}

function ConditionCard({ c, slug, model }: { c: Condition; slug: string; model: RiskModel }) {
  return (
    <div className={`cond role-${c.role}`}>
      <div className="cond-head">
        <code className="cid">{c.condition_id}</code>
        <Badge kind="cat">{c.category}</Badge>
        <Badge kind={`role_${c.role}`}>{c.role}</Badge>
        <Badge kind={c.confidence}>{c.confidence}</Badge>
        <Badge kind="derive">{c.derived_by}</Badge>
        {c.judge && (
          <Badge kind={`judge_${c.judge.verdict}`} title={c.judge.missing}>
            judge: {c.judge.verdict}
          </Badge>
        )}
      </div>
      <div className="cond-stmt">{c.statement}</div>
      <div className="small">
        <code>{c.operator}</code> <code>{JSON.stringify(c.expected_value)}</code>
      </div>
      {c.ambiguities.length > 0 && (
        <ul className="ambig">
          {c.ambiguities.map((a, i) => (
            <li key={i}>{a}</li>
          ))}
        </ul>
      )}
      {c.search_queries.length > 0 && (
        <div className="queries">
          {c.search_queries.map((q, i) => (
            <div key={i}>
              <span className="muted small">{q.tool}</span> <code>{q.query}</code>
            </div>
          ))}
        </div>
      )}
      {c.evidence.map((e, i) => (
        <EvidenceRow key={i} ev={e} slug={slug} model={model} />
      ))}
    </div>
  )
}

export default function PathDetail({
  path,
  slug,
  model,
  override,
  onReview,
  onClose,
}: {
  path: RiskPath
  slug: string
  model: RiskModel
  override?: Override
  onReview: (decision: 'accept' | 'reject' | null, note: string) => void
  onClose: () => void
}) {
  const [graph, setGraph] = useState<string | null>(null)
  const [note, setNote] = useState(override?.note ?? '')
  useEffect(() => {
    setGraph(null)
    api.graph(slug, path.path_id).then(setGraph).catch(() => {})
    setNote(override?.note ?? '')
  }, [slug, path.path_id, override?.note])
  const groups: [string, Condition[]][] = [
    ['Required', path.conditions.filter((c) => c.role === 'required')],
    ['Alternatives (any one)', path.conditions.filter((c) => c.role === 'alternative')],
    ['Uncertain', path.conditions.filter((c) => c.role === 'uncertain')],
    ['Context', path.conditions.filter((c) => c.role === 'context')],
  ]
  return (
    <aside className="drawer">
      <div className="drawer-head">
        <div>
          <div className="muted small">
            <code>{path.path_id}</code>
          </div>
          <h2>{path.path_name}</h2>
          <div className="badges">
            <Badge kind={path.risk_level}>{path.risk_level}</Badge>
            <Badge kind={path.confidence}>confidence {path.confidence}</Badge>
            <Badge kind="cat">{path.risk_type}</Badge>
            <Badge kind="info">introduced {path.introduced_in}</Badge>
            <Badge kind="info">fires {path.fires_at}</Badge>
            {path.superseded_by && <Badge kind="warn">superseded by {path.superseded_by}</Badge>}
            {path.reverted_in && <Badge kind="warn">reverted in {path.reverted_in}</Badge>}
            {path.applies_to?.from_versions && <Badge kind="warn">applies from {path.applies_to.from_versions}</Badge>}
            {path.review_flags.map((f) => (
              <Badge key={f} kind="flag">{f}</Badge>
            ))}
          </div>
        </div>
        <button className="close" onClick={onClose} aria-label="close">
          ×
        </button>
      </div>
      <p>{path.description}</p>
      <div className="small muted">Affected surface: {path.affected_surface}</div>
      {path.merged_from.length > 0 && <div className="small muted">Merged from: {path.merged_from.join(', ')}</div>}

      <div className="review">
        <b>Review</b>
        <span className="muted small">current: {override?.decision ?? path.review_status}</span>
        <input placeholder="note" value={note} onChange={(e) => setNote(e.target.value)} />
        <button className="btn ok" onClick={() => onReview('accept', note)}>Accept</button>
        <button className="btn bad" onClick={() => onReview('reject', note)}>Reject</button>
        {override && <button className="btn" onClick={() => onReview(null, '')}>Clear</button>}
        <div className="small muted">Saved to review/overrides.yaml; applied on the next run.</div>
      </div>

      {graph && (
        <>
          <h3>Condition graph</h3>
          <Mermaid code={graph} />
        </>
      )}

      {groups.map(([title, cs]) =>
        cs.length ? (
          <section key={title}>
            <h3>{title}</h3>
            {cs.map((c) => (
              <ConditionCard key={c.condition_id} c={c} slug={slug} model={model} />
            ))}
          </section>
        ) : null,
      )}

      <h3>Suggested actions</h3>
      <ul>
        {path.suggested_actions.map((a, i) => (
          <li key={i}>{a}</li>
        ))}
      </ul>
    </aside>
  )
}
