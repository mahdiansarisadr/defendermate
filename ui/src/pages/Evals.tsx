import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { api, type EvalResults } from '../api'
import { Badge, ErrorBox, Loading, ratio } from '../components/ui'

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
  return (
    <div>
      <section className="hero compact">
        <div>
          <h1>Evaluation</h1>
          <p className="muted">
            Metrics from TDD §17.4. Hard gates must pass (asserted in <code>tests/test_eval_gates.py</code>); soft gates are
            targets reported here. Gold sets were committed before the first extraction.
          </p>
        </div>
        <button className="btn" onClick={rerun} disabled={busy} title="Deterministic metrics only (no LLM calls)">
          {busy ? 'Recomputing…' : 'Recompute deterministic metrics'}
        </button>
      </section>
      <table className="table">
        <thead>
          <tr>
            <th>Metric</th>
            <th>Result</th>
            <th>Target</th>
            <th>Gate</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {res.metrics.map((m) => (
            <tr key={m.name}>
              <td>
                <b>{m.name}</b>
                <div className="small muted">{DESCRIPTIONS[m.name] ?? ''}</div>
              </td>
              <td className="small">{m.display}</td>
              <td className="small">{m.target === null || m.target === undefined ? '–' : String(m.target)}</td>
              <td>
                <Badge kind={m.gate === 'hard' ? 'bad' : m.gate === 'soft' ? 'warn' : 'info'}>{m.gate}</Badge>
              </td>
              <td>{m.pass === true ? <Badge kind="ok">pass</Badge> : m.pass === false ? <Badge kind="bad">fail</Badge> : '–'}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <h2>Per upgrade</h2>
      <div className="grid">
        {per.map(([slug, r]) => {
          const items = r.gold_items ?? []
          return (
            <div className="card" key={slug}>
              <div className="card-head">
                <h3>
                  <Link to={`/upgrade/${slug}`}>{slug}</Link>
                </h3>
              </div>
              <div className="mini-stats">
                <div><b>{ratio(r.recall as [number, number])}</b><small>recall</small></div>
                <div><b>{ratio(r.strict_precision as [number, number])}</b><small>strict prec.</small></div>
                <div><b>{ratio(r.estimated_precision as [number, number])}</b><small>est. prec.</small></div>
                <div><b>{ratio(r.classification as [number, number])}</b><small>classification</small></div>
                <div><b>{ratio(r.grounding as [number, number])}</b><small>grounding</small></div>
                <div><b>{String(r.validator_errors)}</b><small>errors</small></div>
              </div>
              <table className="table compact">
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
          )
        })}
      </div>
      {res.extra?.ablations ? (
        <>
          <h2>Ablations</h2>
          <pre className="code">{JSON.stringify(res.extra.ablations, null, 1)}</pre>
        </>
      ) : null}
    </div>
  )
}
