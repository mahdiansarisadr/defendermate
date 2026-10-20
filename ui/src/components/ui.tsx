import type { ReactNode } from 'react'

export const LEVELS = ['critical', 'high', 'medium', 'low', 'unknown'] as const

export function Badge({ kind, children, title }: { kind: string; children: ReactNode; title?: string }) {
  return (
    <span className={`badge b-${kind.replace(/[^a-z_]/gi, '_')}`} title={title}>
      {children}
    </span>
  )
}

export function Stat({ label, value, hint }: { label: string; value: ReactNode; hint?: string }) {
  return (
    <div className="stat" title={hint}>
      <div className="stat-v">{value}</div>
      <div className="stat-l">{label}</div>
    </div>
  )
}

export function LevelBar({ counts }: { counts: Record<string, number> }) {
  const total = Object.values(counts).reduce((a, b) => a + b, 0) || 1
  return (
    <div className="levelbar" title={LEVELS.map((l) => `${l}: ${counts[l] || 0}`).join(', ')}>
      {LEVELS.map((l) =>
        counts[l] ? <div key={l} className={`seg s-${l}`} style={{ width: `${(100 * counts[l]) / total}%` }} /> : null,
      )}
    </div>
  )
}

export function ratio(r?: [number, number]) {
  if (!r || !r[1]) return '–'
  return `${((100 * r[0]) / r[1]).toFixed(0)}%`
}

export function Loading({ what }: { what: string }) {
  return <div className="muted pad">Loading {what}…</div>
}

export function ErrorBox({ error }: { error: string }) {
  return <div className="error-box">{error}</div>
}

export function Tabs<T extends string>({ tabs, value, onChange }: { tabs: [T, string][]; value: T; onChange: (t: T) => void }) {
  return (
    <div className="tabs">
      {tabs.map(([k, label]) => (
        <button key={k} className={k === value ? 'tab active' : 'tab'} onClick={() => onChange(k)}>
          {label}
        </button>
      ))}
    </div>
  )
}
