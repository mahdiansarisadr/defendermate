import { NavLink, Route, Routes } from 'react-router-dom'
import Overview from './pages/Overview'
import UpgradePage from './pages/Upgrade'
import Evals from './pages/Evals'
import Runs from './pages/Runs'

export default function App() {
  return (
    <div className="shell">
      <header className="topbar">
        <div className="brand">
          <span className="logo">URX</span>
          <span className="brand-sub">Upgrade Risk Extraction</span>
        </div>
        <nav>
          <NavLink to="/" end>Overview</NavLink>
          <NavLink to="/evals">Evals</NavLink>
          <NavLink to="/runs">Runs</NavLink>
        </nav>
      </header>
      <main>
        <Routes>
          <Route path="/" element={<Overview />} />
          <Route path="/upgrade/:slug" element={<UpgradePage />} />
          <Route path="/evals" element={<Evals />} />
          <Route path="/runs" element={<Runs />} />
        </Routes>
      </main>
      <footer className="foot">Documentation-derived risk conditions; not a migration plan.</footer>
    </div>
  )
}
