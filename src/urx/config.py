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
# USD per million tokens (input, output), from docs.anthropic.com/en/docs/about-claude/pricing (2026-10-20).
# Estimates for the cost report only; prompt caching discounts are not modeled.
PRICES = {
    "claude-haiku-5-5": (0.10, 0.50),
    "claude-sonnet-5-5": (2.0, 10.0),
    "claude-opus-5-5": (4.0, 20.0),
}
# Haiku 5.5 bills prompts over 100k input tokens at a higher rate.
LONG_PROMPT_PRICES = {"claude-haiku-5-5": (100_000, 0.50, 2.50)}


def price_usd(model: str, input_tokens: int, output_tokens: int) -> float:
    pin, pout = PRICES.get(model, (0.0, 0.0))
    if model in LONG_PROMPT_PRICES and input_tokens > LONG_PROMPT_PRICES[model][0]:
        _, pin, pout = LONG_PROMPT_PRICES[model]
    return (input_tokens * pin + output_tokens * pout) / 1e6
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
