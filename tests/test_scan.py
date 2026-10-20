from __future__ import annotations

import shutil

import pytest

from urx import config
from urx.scan import scan

DJ = config.ROOT / "outputs" / "django_3.2_to_4.2" / "risk_model.json"
REACT = config.ROOT / "outputs" / "react_17_to_18" / "risk_model.json"
APP = config.ROOT / "fixtures" / "demo_app"
pytestmark = pytest.mark.skipif(shutil.which("rg") is None, reason="ripgrep not installed")


def test_refuses_paths_outside_fixtures(tmp_path):
    with pytest.raises(PermissionError):
        scan(DJ, tmp_path)
    with pytest.raises(PermissionError):
        scan(DJ, config.ROOT / "src")


@pytest.mark.skipif(not DJ.exists(), reason="no Django output")
def test_planted_usages_fire_and_control_does_not():
    res = scan(DJ, APP)
    fired = " | ".join(r["path_name"].lower() for r in res if r["fires"])
    for planted in ("ugettext", "is_ajax", "nullbooleanfield", "jsonfield", "force_text", "csrf_trusted_origins",
                    "default_hashing_algorithm", "index_together", "pytz"):
        assert planted in fired, planted
    assert not any(r["fires"] for r in res if "urlquote" in r["path_name"].lower())


@pytest.mark.skipif(not REACT.exists(), reason="no React output")
def test_other_project_model_does_not_fire_on_django_app():
    assert not any(r["fires"] for r in scan(REACT, APP))
