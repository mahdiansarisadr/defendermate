import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { api, type Run } from '../api'
import { Badge, ErrorBox, PageHeader } from '../components/ui'

const STAGES = ['plan', 'fetch', 'parse', 'triage', 'extract', 'link', 'compose', 'judge', 'rubric', 'assemble', 'validate']

export default function Runs() {
  const [reg, setReg] = useState<{ project: string; known_releases: string[] }[]>([])
  const [runs, setRuns] = useState<Run[]>([])
  const [active, setActive] = useState<Run | null>(null)
  const [form, setForm] = useState({ project: 'Django', current_version: '3.2', target_version: '4.2', offline: true })
  const [err, setErr] = useState<string | null>(null)

  useEffect(() => {
    api.registry().then(setReg)
    api.runs().then(setRuns)
  }, [])

  useEffect(() => {
    if (!active || active.status !== 'running') return
    const t = setInterval(async () => {
      const r = await api.run(active.run_id)
      setActive(r)
      if (r.status !== 'running') api.runs().then(setRuns)
    }, 1500)
    return () => clearInterval(t)
  }, [active])

  const start = async () => {
    setErr(null)
    try {
      const r = await api.startRun(form)
      setActive({ ...r, events: [] })
      api.runs().then(setRuns)
    } catch (e) {
      setErr(String(e))
    }
  }

  const releases = reg.find((r) => r.project.toLowerCase() === form.project.toLowerCase())?.known_releases ?? []
  const done = new Set((active?.events ?? []).filter((e) => e.event === 'stage_end').map((e) => e.stage))
  const current = [...(active?.events ?? [])].reverse().find((e) => e.event === 'stage_start')?.stage

  return (
    <div>
      <PageHeader
        title="Runs"
        subtitle="Offline replays the pinned source and LLM caches at no cost; online fetches and calls the model for anything not cached."
      />
      <div className="card run-form">
        <select value={form.project} onChange={(e) => setForm({ ...form, project: e.target.value })}>
          {reg.map((r) => (
            <option key={r.project}>{r.project}</option>
          ))}
        </select>
        <select value={form.current_version} onChange={(e) => setForm({ ...form, current_version: e.target.value })}>
          {releases.map((v) => (
            <option key={v}>{v}</option>
          ))}
        </select>
        <span>→</span>
        <select value={form.target_version} onChange={(e) => setForm({ ...form, target_version: e.target.value })}>
          {releases.map((v) => (
            <option key={v}>{v}</option>
          ))}
        </select>
        <label className="small">
          <input type="checkbox" checked={form.offline} onChange={(e) => setForm({ ...form, offline: e.target.checked })} /> offline
        </label>
        <button className="btn ok" onClick={start}>
          Start run
        </button>
      </div>
      {err && <ErrorBox error={err} />}
      {active && (
        <div className="card">
          <div className="card-head">
            <h3>
              {active.slug} <span className="muted small">run {active.run_id}</span>
            </h3>
            <Badge kind={active.status === 'ok' ? 'ok' : active.status === 'error' ? 'bad' : 'warn'}>{active.status}</Badge>
          </div>
          <div className="stages">
            {STAGES.map((s) => (
              <div key={s} className={`stage ${done.has(s) ? 'done' : s === current ? 'cur' : ''}`}>
                {s}
              </div>
            ))}
          </div>
          {active.error && <ErrorBox error={active.error} />}
          {active.status === 'ok' && <Link to={`/upgrade/${active.slug}`}>Open result →</Link>}
          <pre className="code log">
            {(active.events ?? [])
              .map((e) => `+${e.elapsed_s.toFixed(1)}s  ${e.event}${e.stage ? ' ' + e.stage : ''}${Object.entries(e)
                .filter(([k]) => !['ts', 'elapsed_s', 'event', 'stage', 'run_id', 'upgrade', 'usage'].includes(k))
                .map(([k, v]) => ` ${k}=${typeof v === 'object' ? JSON.stringify(v) : v}`)
                .join('')}`)
              .join('\n')}
          </pre>
        </div>
      )}
      <div className="card">
        <h3>Runs this session</h3>
        <table className="table compact">
          <thead>
            <tr>
              <th>Run</th>
              <th>Upgrade</th>
              <th>Mode</th>
              <th>Started</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {runs.map((r) => (
              <tr key={r.run_id} onClick={() => api.run(r.run_id).then(setActive)}>
                <td className="mono small">{r.run_id}</td>
                <td>{r.slug}</td>
                <td>{r.offline ? 'offline' : 'online'}</td>
                <td className="small">{r.started}</td>
                <td>
                  <Badge kind={r.status === 'ok' ? 'ok' : r.status === 'error' ? 'bad' : 'warn'}>{r.status}</Badge>
                </td>
              </tr>
            ))}
            {!runs.length && (
              <tr>
                <td colSpan={5} className="muted">
                  No runs started from the UI yet. CLI runs appear in each upgrade's Pipeline tab.
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  )
}
