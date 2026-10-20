import { useEffect, useState } from 'react'
import { NavLink, Route, Routes } from 'react-router-dom'
import { api, type UpgradeSummary } from './api'
import { Icon } from './components/icons'
import Overview from './pages/Overview'
import UpgradePage from './pages/Upgrade'
import Evals from './pages/Evals'
import Experiments from './pages/Experiments'
import Runs from './pages/Runs'

function Sidebar() {
  const [upgrades, setUpgrades] = useState<UpgradeSummary[]>([])
  useEffect(() => {
    api.upgrades().then(setUpgrades).catch(() => {})
  }, [])
  return (
    <aside className="sidebar">
      <div className="brand">
        <span className="logo">URX</span>
        <span className="brand-sub">Upgrade Risk Extraction</span>
      </div>
      <nav>
        <NavLink to="/" end className="nav-item">
          <Icon name="overview" /> Overview
        </NavLink>
        <div className="nav-section">Upgrades</div>
        {upgrades.map((u) => (
          <NavLink key={u.slug} to={`/upgrade/${u.slug}`} className={`nav-item nav-sub ${u.exists ? '' : 'disabled'}`}>
            <span className="nav-label">
              {u.project ?? u.slug} <span className="nav-ver">{u.current_version} → {u.target_version}</span>
            </span>
            {u.exists && <span className="nav-count">{u.paths}</span>}
          </NavLink>
        ))}
        <div className="nav-section">Quality</div>
        <NavLink to="/evals" className="nav-item">
          <Icon name="evals" /> Evals
        </NavLink>
        <NavLink to="/experiments" className="nav-item">
          <Icon name="experiments" /> Experiments
        </NavLink>
        <div className="nav-section">Operations</div>
        <NavLink to="/runs" className="nav-item">
          <Icon name="runs" /> Runs
        </NavLink>
      </nav>
      <div className="sidebar-foot">Documentation-derived risk conditions; not a migration plan.</div>
    </aside>
  )
}

export default function App() {
  return (
    <div className="shell">
      <Sidebar />
      <main>
        <Routes>
          <Route path="/" element={<Overview />} />
          <Route path="/upgrade/:slug" element={<UpgradePage />} />
          <Route path="/evals" element={<Evals />} />
          <Route path="/experiments" element={<Experiments />} />
          <Route path="/runs" element={<Runs />} />
        </Routes>
      </main>
    </div>
  )
}
