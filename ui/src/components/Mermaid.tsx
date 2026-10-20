import { useEffect, useRef, useState } from 'react'
import mermaid from 'mermaid'

mermaid.initialize({ startOnLoad: false, theme: 'neutral', securityLevel: 'strict', flowchart: { htmlLabels: true } })

let counter = 0

export default function Mermaid({ code }: { code: string }) {
  const ref = useRef<HTMLDivElement>(null)
  const [err, setErr] = useState<string | null>(null)
  useEffect(() => {
    let alive = true
    const id = `mmd-${counter++}`
    mermaid
      .render(id, code)
      .then(({ svg }) => {
        if (alive && ref.current) ref.current.innerHTML = svg
      })
      .catch((e) => alive && setErr(String(e)))
    return () => {
      alive = false
    }
  }, [code])
  if (err) return <pre className="code">{code}</pre>
  return <div className="mermaid" ref={ref} />
}
