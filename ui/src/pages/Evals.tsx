import { Fragment, useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { api, type EvalResults } from '../api'
import { Badge, ErrorBox, Loading, PageHeader, Stat, Tabs, ratio } from '../components/ui'

const DESCRIPTIONS: Record<string, string> = {
  grounding_rate: 'Share of quotes in final outputs found verbatim (after normalization) in the pinned cached source.',
  validator_errors: 'Deterministic validator errors across all five outputs (schema, refs, quotes, structure).',
  structural_completeness: 'Paths with at least one version condition and one app-side condition.',
  'recall_per_upgrade (min)': 'Gold risks found as risk paths, worst upgrade.',
  recall_overall: 'Gold risks found as risk paths, pooled across upgrades.',
  'strict_precision (lower bound)': 'Paths that match a gold item. A lower bound: gold sets are not exhaustive.',
  estimated_precision: 'LLM precision judge on paths not matched by gold, plus gold-matched paths counted valid.',
  classification_accuracy: 'Found gold items placed in the correct bucket (risk / context / disqualified).',
  level_agreement: 'Matched gold risks whose extracted level is within one level of the gold minimum.',
  field_consistency: 'Structured fields agree with quotes (version values match release, json_path values match metadata).',
  judge_accuracy: 'Grounding judge accuracy on synthetic supported vs mutated claims.',
  judge_kappa: "Cohen's kappa for the same judge check.",
  drift_false_accept_exact: 'Drifted (mutated) quotes accepted by the exact-match verifier. Fuzzy 0.9 shown for comparison.',
  stability_jaccard: 'Path-id overlap between a cached run and a cold rerun (React).',
}

export default function Evals() {
  const [res, setRes] = useState<EvalResults | null>(null)
  const [err, setErr] = useState<string | null>(null)
  const [busy, setBusy] = useState(false)
  const [slug, setSlug] = useState('')
  useEffect(() => {
    api.evalResults().then(setRes).catch((e) => setErr(String(e)))
  }, [])
  const rerun = async () => {
    setBusy(true)
    try {
      setRes(await api.runEval())
    } catch (e) {
      setErr(String(e))
    } finally {
      setBusy(false)
    }
  }
  if (err) return <ErrorBox error={err} />
  if (!res) return <Loading what="eval results" />
  if (!res.metrics) return <div className="card">No eval results yet. Run <code>urx eval</code>.</div>
  const per = Object.entries(res.per_upgrade)
  const gate = (g: string) => res.metrics.filter((m) => m.gate === g)
  const passed = (g: string) => gate(g).filter((m) => m.pass).length
  const groups: [string, string][] = [
    ['hard', 'Hard gates'],
    ['soft', 'Soft targets'],
    ['info', 'Informational'],
  ]
  const sel = per.find(([s]) => s === slug) ?? per[0]
  return (
    <div>
      <PageHeader
        title="Evals"
        subtitle={
          <span className="meta">
            <Badge kind={passed('hard') === gate('hard').length ? 'ok' : 'bad'}>
              {passed('hard')}/{gate('hard').length} hard gates pass
            </Badge>
            <span>
              {passed('soft')}/{gate('soft').length} soft targets met
            </span>
            <span>Gold sets committed before the first extraction</span>
          </span>
        }
        actions={
          <button className="btn" onClick={rerun} disabled={busy} title="Deterministic metrics only (no LLM calls)">
            {busy ? 'Recomputing…' : 'Recompute'}
          </button>
        }
      />
      <div className="card flush">
        <table className="table plain">
          <tbody>
            {groups.map(([g, label]) =>
              gate(g).length ? (
                <Fragment key={g}>
                  <tr className="group">
                    <td colSpan={3}>{label}</td>
                  </tr>
                  {gate(g).map((m) => (
                    <tr key={m.name} className="static">
                      <td>
                        <span className={`dot ${m.pass === true ? 'dot-ok' : m.pass === false ? 'dot-bad' : 'dot-info'}`} />
                        <b>{m.name.replace(/_/g, ' ')}</b>
                        <div className="small muted indent">{DESCRIPTIONS[m.name] ?? ''}</div>
                      </td>
                      <td className="small">{m.display}</td>
                      <td className="small muted right">
                        {m.target === null || m.target === undefined ? '' : `target ${String(m.target)}`}
                      </td>
                    </tr>
                  ))}
                </Fragment>
              ) : null,
            )}
          </tbody>
        </table>
      </div>

      <h2>Gold items by upgrade</h2>
      <Tabs<string> value={sel?.[0] ?? ''} onChange={setSlug} tabs={per.map(([s]) => [s, s.replace(/_/g, ' ')] as [string, string])} />
      {sel && [sel].map(([slug, r]) => {
          const items = r.gold_items ?? []
          return (
            <div key={slug}>
              <div className="stats">
                <Stat label="Recall" value={ratio(r.recall as [number, number])} />
                <Stat label="Est. precision" value={ratio(r.estimated_precision as [number, number])} />
                <Stat label="Classification" value={ratio(r.classification as [number, number])} />
                <Stat label="Grounding" value={ratio(r.grounding as [number, number])} />
              </div>
              <div className="card flush">
              <table className="table plain">
                <thead>
                  <tr>
                    <th>Gold item</th>
                    <th>Expected</th>
                    <th>Found as</th>
                    <th>Level</th>
                  </tr>
                </thead>
                <tbody>
                  {items.map((g) => {
                    const where = Object.entries(g.hits).filter(([, v]) => v.length).map(([k]) => k)
                    return (
                      <tr key={g.gold_id} className={g.correct_bucket ? '' : 'miss'}>
                        <td className="small mono">{g.gold_id}</td>
                        <td className="small">{g.kind}</td>
                        <td className="small">
                          {where.length ? where.join(', ') : <span className="bad-t">not found</span>}
                          {g.hits.risk?.length > 0 && (
                            <div>
                              {g.hits.risk.slice(0, 3).map((pid) => (
                                <Link key={pid} className="small" to={`/upgrade/${slug}?path=${pid}`}>
                                  {pid}{' '}
                                </Link>
                              ))}
                            </div>
                          )}
                        </td>
                        <td className="small">
                          {g.extracted_level ?? '–'}
                          {g.min_level ? <span className="muted"> (min {g.min_level})</span> : null}
                        </td>
                      </tr>
                    )
                  })}
                </tbody>
              </table>
              </div>
              <Link to={`/upgrade/${slug}`} className="small">Open {slug} →</Link>
            </div>
          )
        })}
      {res.extra?.ablations ? (
        <details className="more">
          <summary>Ablations</summary>
          <pre className="code">{JSON.stringify(res.extra.ablations, null, 1)}</pre>
        </details>
      ) : null}
    </div>
  )
}
