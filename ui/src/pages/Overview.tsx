import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { api, type EvalResults, type UpgradeSummary } from '../api'
import { Badge, ErrorBox, LevelBar, Loading, Stat, ratio } from '../components/ui'

export default function Overview() {
  const [rows, setRows] = useState<UpgradeSummary[] | null>(null)
  const [ev, setEv] = useState<EvalResults | null>(null)
  const [err, setErr] = useState<string | null>(null)
  useEffect(() => {
    api.upgrades().then(setRows).catch((e) => setErr(String(e)))
    api.evalResults().then(setEv).catch(() => {})
  }, [])
  if (err) return <ErrorBox error={err} />
  if (!rows) return <Loading what="upgrades" />
  const hard = ev?.metrics?.filter((m) => m.gate === 'hard') ?? []
  const hardPass = hard.filter((m) => m.pass).length
  const totals = rows.reduce(
    (a, r) => ({
      paths: a.paths + (r.paths || 0),
      usd: a.usd + (r.usd_full || 0),
      errs: a.errs + (r.validation?.errors || 0),
    }),
    { paths: 0, usd: 0, errs: 0 },
  )
  return (
    <div>
      <section className="hero">
        <div>
          <h1>Upgrade risk models</h1>
          <p className="muted">
            Evidence-grounded risk paths extracted from official release notes, migration guides, changelogs and package
            metadata. Every condition carries a verbatim quote that is re-verified against the cached source.
          </p>
        </div>
        <div className="stats">
          <Stat label="risk paths" value={totals.paths} />
          <Stat label="validator errors" value={totals.errs} />
          <Stat label="hard eval gates" value={ev ? `${hardPass}/${hard.length}` : '–'} hint="See Evals" />
          <Stat
            label="LLM cost to produce"
            value={`$${totals.usd.toFixed(2)}`}
            hint="Estimated cost of every LLM call behind these models, cached or not. Replays from cache cost nothing."
          />
        </div>
      </section>
      <div className="grid">
        {rows.map((r) =>
          r.exists ? (
            <Link to={`/upgrade/${r.slug}`} className="card upgrade-card" key={r.slug}>
              <div className="card-head">
                <h2>
                  {r.project} <span className="muted">{r.current_version} → {r.target_version}</span>
                </h2>
                <Badge kind={r.overall_confidence || 'low'} title="overall confidence">
                  {r.overall_confidence}
                </Badge>
              </div>
              <LevelBar counts={r.by_level || {}} />
              <div className="kv">
                <span>{r.paths} paths</span>
                {(['critical', 'high', 'medium', 'low'] as const).map((l) => (
                  <span key={l} className={`lv-${l}`}>
                    {r.by_level?.[l] || 0} {l}
                  </span>
                ))}
              </div>
              <div className="mini-stats">
                <div><b>{ratio(r.recall)}</b><small>gold recall</small></div>
                <div><b>{ratio(r.estimated_precision)}</b><small>est. precision</small></div>
                <div><b>{ratio(r.grounding)}</b><small>grounded</small></div>
                <div><b>{r.validation?.errors ?? '–'}</b><small>errors</small></div>
                <div><b>{r.sources_used}</b><small>sources{r.sources_rejected ? ` (+${r.sources_rejected} rej.)` : ''}</small></div>
                <div><b>{r.review_flags}</b><small>flagged</small></div>
              </div>
              <div className="muted small">
                {r.context_facts} context facts · {r.disqualified} disqualified · {r.open_questions} open questions ·
                generated {r.generated_at?.replace('T', ' ').replace('Z', ' UTC')}
              </div>
            </Link>
          ) : (
            <div className="card upgrade-card missing" key={r.slug}>
              <h2>{r.slug}</h2>
              <p className="muted">No output yet. Start a run from the Runs page.</p>
            </div>
          ),
        )}
      </div>
    </div>
  )
}
