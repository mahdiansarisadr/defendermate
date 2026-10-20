import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { api, type EvalResults, type UpgradeSummary } from '../api'
import { Badge, ErrorBox, LevelBar, Loading, PageHeader, Stat, ratio } from '../components/ui'

export default function Overview() {
  const [rows, setRows] = useState<UpgradeSummary[] | null>(null)
  const [ev, setEv] = useState<EvalResults | null>(null)
  const [err, setErr] = useState<string | null>(null)
  const nav = useNavigate()
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
      <PageHeader
        title="Overview"
        subtitle="Evidence-grounded risk paths from official release notes, migration guides and changelogs. Every quote is re-verified against the cached source."
      />
      <div className="stats">
        <Stat label="Risk paths" value={totals.paths} />
        <Stat label="Hard eval gates" value={ev ? `${hardPass}/${hard.length}` : '–'} />
        <Stat label="Validator errors" value={totals.errs} />
        <Stat
          label="LLM cost to produce"
          value={`$${totals.usd.toFixed(2)}`}
          hint="Estimated cost of every LLM call behind these models, cached or not."
        />
      </div>
      <div className="card flush">
        <table className="table plain">
          <thead>
            <tr>
              <th>Upgrade</th>
              <th style={{ width: '28%' }}>Risk mix</th>
              <th className="num">Paths</th>
              <th className="num">Gold recall</th>
              <th className="num">Est. precision</th>
              <th>Confidence</th>
            </tr>
          </thead>
          <tbody>
            {rows.map((r) =>
              r.exists ? (
                <tr key={r.slug} onClick={() => nav(`/upgrade/${r.slug}`)}>
                  <td>
                    <div className="pname">{r.project}</div>
                    <div className="muted small">
                      {r.current_version} → {r.target_version}
                    </div>
                  </td>
                  <td>
                    <LevelBar counts={r.by_level || {}} />
                    <div className="muted small">
                      {(r.by_level?.critical || 0) + (r.by_level?.high || 0)} critical or high
                    </div>
                  </td>
                  <td className="num">{r.paths}</td>
                  <td className="num">{ratio(r.recall)}</td>
                  <td className="num">{ratio(r.estimated_precision)}</td>
                  <td>
                    <Badge kind={r.overall_confidence || 'low'}>{r.overall_confidence}</Badge>
                  </td>
                </tr>
              ) : (
                <tr key={r.slug} className="dim">
                  <td colSpan={6}>
                    {r.slug} <span className="muted small">· no output yet, start one from Runs</span>
                  </td>
                </tr>
              ),
            )}
          </tbody>
        </table>
      </div>
      <ul className="legend">
        {LEVEL_DEFS.map(([l, d]) => (
          <li key={l}>
            <span className={`seg s-${l}`} />
            <b className={`lv-${l}`}>{l}</b> {d}
          </li>
        ))}
      </ul>
    </div>
  )
}

const LEVEL_DEFS: [string, string][] = [
  ['critical', 'The upgrade fails or data is at risk for most users who meet the conditions (e.g. unsupported runtime or database version, an API version that stops being served).'],
  ['high', 'Code or config that meets the conditions breaks at upgrade time.'],
  ['medium', 'Behavior change or migration with a clear workaround.'],
  ['low', 'Edge case, cosmetic, or warning-only.'],
]
