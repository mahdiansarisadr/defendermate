"""Paths and runtime settings. Model names come from env, never from call sites."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[2]
load_dotenv(ROOT / ".env")

REGISTRY_DIR = ROOT / "registry"
PROMPTS_DIR = ROOT / "prompts"
SCHEMAS_DIR = ROOT / "schemas"
CACHE_DIR = Path(os.environ.get("URX_CACHE_DIR", ROOT / "cache"))
LLM_CACHE_DIR = Path(os.environ.get("URX_LLM_CACHE_DIR", ROOT / "llm_cache"))
OUTPUTS_DIR = Path(os.environ.get("URX_OUTPUTS_DIR", ROOT / "outputs"))
GOLD_DIR = ROOT / "gold"
REVIEW_FILE = ROOT / "review" / "overrides.yaml"
EVAL_DIR = ROOT / "eval"
UI_DIST = ROOT / "ui" / "dist"

PROVIDER = os.environ.get("URX_PROVIDER", "anthropic")
MODELS = {
    "anthropic": {
        "cheap": os.environ.get("URX_CHEAP_MODEL", "claude-haiku-5-5"),
        "strong": os.environ.get("URX_STRONG_MODEL", "claude-sonnet-5-5"),
    },
    "openai": {
        "cheap": os.environ.get("URX_OPENAI_CHEAP_MODEL", "gpt-5-mini"),
        "strong": os.environ.get("URX_OPENAI_STRONG_MODEL", "gpt-5"),
    },
}
# USD per million tokens (input, output); estimates for the cost report only.
PRICES = {
    "claude-haiku-5-5": (1.0, 5.0),
    "claude-sonnet-5-5": (3.0, 15.0),
}
MAX_WORKERS = int(os.environ.get("URX_MAX_WORKERS", "8"))

DISCLAIMER = "Documentation-derived risk conditions; not a migration plan."

DEFAULT_UPGRADES = [
    ("Django", "3.2", "4.2"),
    ("React", "17", "18"),
    ("Kubernetes", "1.23", "1.29"),
    ("PostgreSQL", "13", "16"),
    ("Next.js", "12", "14"),
]


def slugify(project: str) -> str:
    return project.lower().replace(".", "").replace(" ", "")


def upgrade_slug(project: str, current: str, target: str) -> str:
    return f"{slugify(project)}_{current}_to_{target}"
