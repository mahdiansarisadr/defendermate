from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from urx import config
from urx.server import app

SLUG = "react_17_to_18"
pytestmark = pytest.mark.skipif(not (config.OUTPUTS_DIR / SLUG / "risk_model.json").exists(), reason="no output")
client = TestClient(app)


def test_upgrades_and_model():
    rows = {r["slug"]: r for r in client.get("/api/upgrades").json()}
    assert rows[SLUG]["exists"] and rows[SLUG]["paths"] > 0
    m = client.get(f"/api/upgrades/{SLUG}").json()
    assert m["disclaimer"] == config.DISCLAIMER


def test_evidence_context_finds_every_quote():
    m = client.get(f"/api/upgrades/{SLUG}").json()
    evs = [e for p in m["risk_paths"] for c in p["conditions"] for e in c["evidence"] if e["quote"]]
    for e in evs[:30]:
        r = client.get(f"/api/upgrades/{SLUG}/evidence", params={"source_id": e["source_id"], "quote": e["quote"]})
        assert r.json()["found"], e["quote"]


def test_graph_and_intermediate():
    m = client.get(f"/api/upgrades/{SLUG}").json()
    g = client.get(f"/api/upgrades/{SLUG}/paths/{m['risk_paths'][0]['path_id']}/graph")
    assert g.status_code == 200 and g.text.startswith("graph")
    assert client.get(f"/api/upgrades/{SLUG}/intermediate/triage").json()
    assert client.get(f"/api/upgrades/{SLUG}/intermediate/secrets").status_code == 400


def test_override_roundtrip(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "REVIEW_FILE", tmp_path / "overrides.yaml")
    r = client.post("/api/overrides", json={"id": "react_x", "decision": "reject", "note": "test"})
    assert any(o["id"] == "react_x" for o in r.json())
    r = client.delete("/api/overrides/react_x")
    assert not any(o["id"] == "react_x" for o in r.json())
