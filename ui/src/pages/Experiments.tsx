import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { api, type ExperimentRow, type Experiments as Exp } from '../api'
import { Badge, ErrorBox, Loading } from '../components/ui'

type MetricKey = 'f1' | 'recall' | 'estimated_precision' | 'strict_precision' | 'classification' | 'level_agreement' | 'stability' | 'judge_accuracy'

const METRICS: [MetricKey, string][] = [
  ['f1', 'F1 (recall × est. precision)'],
  ['recall', 'Gold recall'],
  ['estimated_precision', 'Estimated precision'],
  ['strict_precision', 'Strict precision (lower bound)'],
  ['classification', 'Classification accuracy'],
  ['level_agreement', 'Level agreement'],
  ['stability', 'Stability (cold rerun Jaccard)'],
  ['judge_accuracy', 'Judge accuracy'],
]

const COLORS: Record<string, string> = { haiku_haiku: '#2f9e44', haiku_sonnet: '#3b5bdb', sonnet_opus: '#c2255c' }
const pct = (x: number | null | undefined) => (x === null || x === undefined ? '–' : `${(100 * x).toFixed(1)}%`)
const frac = (r: [number, number] | null | undefined) => (r ? `${r[0]}/${r[1]}` : '–')

function Scatter({ rows, metric }: { rows: ExperimentRow[]; metric: MetricKey }) {
  const W = 640, H = 340, P = { l: 60, r: 30, t: 20, b: 50 }
  const pts = rows.filter((r) => r[metric] !== null && r.cost_usd > 0)
  if (!pts.length) return <div className="muted">No data for this metric.</div>
  const lx = (c: number) => Math.log10(c)
  const xs = pts.map((r) => lx(r.cost_usd))
  const xmin = Math.floor(Math.min(...xs) * 2) / 2 - 0.25, xmax = Math.ceil(Math.max(...xs) * 2) / 2 + 0.25
  const ys = pts.map((r) => r[metric] as number)
  const ymin = Math.max(0, Math.floor((Math.min(...ys) - 0.05) * 20) / 20), ymax = Math.min(1, Math.ceil((Math.max(...ys) + 0.02) * 20) / 20)
  const sx = (c: number) => P.l + ((lx(c) - xmin) / (xmax - xmin)) * (W - P.l - P.r)
  const sy = (v: number) => H - P.b - ((v - ymin) / Math.max(ymax - ymin, 0.01)) * (H - P.t - P.b)
  const ticksX: number[] = []
  for (let e = Math.ceil(xmin); e <= Math.floor(xmax); e++) for (const m of [1, 2, 5]) {
    const v = m * 10 ** e
    if (lx(v) >= xmin && lx(v) <= xmax) ticksX.push(v)
  }
  const ticksY: number[] = []
  for (let v = ymin; v <= ymax + 1e-9; v += (ymax - ymin) / 4) ticksY.push(v)
  const front = [...pts]
    .sort((a, b) => a.cost_usd - b.cost_usd)
    .reduce<ExperimentRow[]>((acc, r) => (acc.length && (r[metric] as number) <= (acc[acc.length - 1][metric] as number) ? acc : [...acc, r]), [])
  return (
    <svg viewBox={`0 0 ${W} ${H}`} className="scatter">
      {ticksY.map((v) => (
        <g key={v}>
          <line x1={P.l} x2={W - P.r} y1={sy(v)} y2={sy(v)} stroke="#eef0f3" />
          <text x={P.l - 8} y={sy(v) + 4} textAnchor="end" fontSize="11" fill="#6b7280">{(100 * v).toFixed(ymax - ymin < 0.2 ? 1 : 0)}%</text>
        </g>
      ))}
      {ticksX.map((v) => (
        <g key={v}>
          <line x1={sx(v)} x2={sx(v)} y1={P.t} y2={H - P.b} stroke="#f3f4f6" />
          <text x={sx(v)} y={H - P.b + 16} textAnchor="middle" fontSize="11" fill="#6b7280">${v >= 1 ? v : v.toFixed(2)}</text>
        </g>
      ))}
      <text x={(W + P.l) / 2} y={H - 10} textAnchor="middle" fontSize="12" fill="#374151">Cost to produce (USD, log scale)</text>
      <polyline
        fill="none" stroke="#9ca3af" strokeDasharray="5 4" strokeWidth="1.5"
        points={front.map((r) => `${sx(r.cost_usd)},${sy(r[metric] as number)}`).join(' ')}
      />
      {[...pts].sort((a, b) => a.cost_usd - b.cost_usd).map((r, i, all) => {
        const x = sx(r.cost_usd), y = sy(r[metric] as number)
        const last = i === all.length - 1
        const below = i % 2 === 1
        const tx = last ? x - 12 : x + 12
        const ty = below ? y + 22 : y - 22
        return (
          <g key={r.name}>
            <circle cx={x} cy={y} r="8" fill={COLORS[r.name] ?? '#495057'} opacity="0.85" />
            <text x={tx} y={ty} textAnchor={last ? 'end' : 'start'} fontSize="12" fontWeight="600" fill="#1a1d23">{r.label}</text>
            <text x={tx} y={ty + 14} textAnchor={last ? 'end' : 'start'} fontSize="11" fill="#6b7280">
              ${r.cost_usd.toFixed(2)} · {pct(r[metric] as number)}
            </text>
          </g>
        )
      })}
    </svg>
  )
}

function Takeaways({ rows }: { rows: ExperimentRow[] }) {
  if (rows.length < 2) return null
  const base = rows[0]
  return (
    <ul className="takeaways">
      {rows.slice(1).map((r) => {
        const df1 = r.f1 !== null && base.f1 !== null ? r.f1 - base.f1 : null
        const dcost = r.cost_usd - base.cost_usd
        return (
          <li key={r.name}>
            <b>{r.label}</b> costs <b>{r.cost_multiple}×</b> {base.label} (+${dcost.toFixed(2)}) for{' '}
            <b>{df1 === null ? '–' : `${df1 >= 0 ? '+' : ''}${(100 * df1).toFixed(1)} F1 points`}</b>
            {df1 !== null && df1 > 0 ? ` (≈ $${(dcost / (100 * df1)).toFixed(2)} per F1 point)` : ''}; recall {frac(r.recall_hits)} vs{' '}
            {frac(base.recall_hits)}, est. precision {pct(r.estimated_precision)} vs {pct(base.estimated_precision)}.
            {!r.pareto && <span className="bad-t"> Dominated: another config is cheaper and at least as good.</span>}
          </li>
        )
      })}
    </ul>
  )
}

export default function Experiments() {
  const [data, setData] = useState<Exp | null>(null)
  const [err, setErr] = useState<string | null>(null)
  const [metric, setMetric] = useState<MetricKey>('f1')
  useEffect(() => {
    api.experiments().then(setData).catch((e) => setErr(String(e)))
  }, [])
  if (err) return <ErrorBox error={err} />
  if (!data) return <Loading what="experiments" />
  const rows = data.rows
  return (
    <div>
      <section className="hero compact">
        <div>
          <h1>Model configuration experiment</h1>
          <p className="muted">
            The same pipeline run under different cheap / strong model pairs on {data.subset.join(', ') || '–'}. The cheap tier
            triages every item; the strong tier extracts paths, re-checks noise, reconciles reverts and judges grounding. Every
            config is scored against the same gold sets with the same Sonnet 5.5 precision judge.
          </p>
        </div>
      </section>
      {data.pending.length > 0 && (
        <div className="callout">
          Not run yet: {data.pending.map((p) => p.label).join(', ')}. Run <code>urx experiment --config &lt;name&gt;</code>.
        </div>
      )}
      <div className="cols">
        <div className="card">
          <div className="card-head">
            <h3>Quality vs cost</h3>
            <select value={metric} onChange={(e) => setMetric(e.target.value as MetricKey)}>
              {METRICS.map(([k, l]) => (
                <option key={k} value={k}>{l}</option>
              ))}
            </select>
          </div>
          <Scatter rows={rows} metric={metric} />
          <div className="small muted">Dashed line: cost-efficient frontier for the selected metric.</div>
        </div>
        <div className="card">
          <h3>Trade-off</h3>
          <Takeaways rows={rows} />
          <h3>Cost breakdown</h3>
          {rows.map((r) => (
            <div key={r.name} className="costbar-row">
              <span className="small">{r.label}</span>
              <div className="costbar" style={{ width: `${Math.max(2, (100 * r.cost_usd) / Math.max(...rows.map((x) => x.cost_usd)))}%`, background: COLORS[r.name] }} />
              <b>${r.cost_usd.toFixed(2)}</b>
            </div>
          ))}
          <div className="small muted">
            List-price estimates from recorded token counts. Tokens: {rows.map((r) => `${r.label} ${(r.input_tokens / 1e6).toFixed(2)}M in / ${(r.output_tokens / 1e6).toFixed(2)}M out`).join(' · ')}
          </div>
        </div>
      </div>
      <table className="table">
        <thead>
          <tr>
            <th>Config</th>
            <th>Models</th>
            <th>Cost</th>
            <th>Paths</th>
            <th>Recall</th>
            <th>Est. prec.</th>
            <th>F1</th>
            <th>Strict prec.</th>
            <th>Classif.</th>
            <th>Level</th>
            <th>Judge acc / κ</th>
            <th>Stability</th>
            <th>$ / gold risk</th>
            <th>Hard gates</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((r) => (
            <tr key={r.name}>
              <td>
                <b>{r.label}</b> {r.pareto ? <Badge kind="ok">frontier</Badge> : <Badge kind="bad">dominated</Badge>}
              </td>
              <td className="small mono">{r.models.cheap} / {r.models.strong}</td>
              <td>${r.cost_usd.toFixed(2)} <span className="muted small">({r.cost_multiple}×)</span></td>
              <td>{r.paths}</td>
              <td>{frac(r.recall_hits)}</td>
              <td>{pct(r.estimated_precision)}</td>
              <td><b>{r.f1?.toFixed(3) ?? '–'}</b></td>
              <td>{pct(r.strict_precision)}</td>
              <td>{pct(r.classification)}</td>
              <td>{pct(r.level_agreement)}</td>
              <td>{r.judge_accuracy?.toFixed(2) ?? '–'} / {r.judge_kappa?.toFixed(2) ?? '–'}</td>
              <td>{r.stability?.toFixed(2) ?? '–'}{r.stability_reused ? <span className="muted small"> (reused)</span> : null}</td>
              <td>{r.usd_per_gold_risk_found !== null ? `$${r.usd_per_gold_risk_found.toFixed(3)}` : '–'}</td>
              <td>
                {r.validator_errors === 0 && r.grounding === 1 ? <Badge kind="ok">pass</Badge> : <Badge kind="bad">{r.validator_errors} err, {pct(r.grounding)} grounded</Badge>}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <h2>Per upgrade</h2>
      <div className="grid">
        {data.subset.map((slug) => (
          <div className="card" key={slug}>
            <h3><Link to={`/upgrade/${slug}`}>{slug}</Link></h3>
            <table className="table compact">
              <thead>
                <tr><th>Config</th><th>Paths</th><th>Recall</th><th>Est. prec.</th><th>Cost</th><th>Missed gold</th></tr>
              </thead>
              <tbody>
                {rows.map((r) => {
                  const u = r.per_upgrade[slug]
                  return u ? (
                    <tr key={r.name}>
                      <td>{r.label}</td>
                      <td>{u.paths}</td>
                      <td>{frac(u.recall)}</td>
                      <td>{frac(u.estimated_precision)}</td>
                      <td>${u.cost_usd.toFixed(2)}</td>
                      <td className="small mono">{u.missed.join(', ') || '–'}</td>
                    </tr>
                  ) : null
                })}
              </tbody>
            </table>
          </div>
        ))}
      </div>
    </div>
  )
}
