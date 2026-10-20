"""Canonical text used by both the item builder and the validator (TDD A3, G8).

Quotes only verify if the LLM saw exactly what the validator checks, so this is
the single place where text is canonicalized. It must be idempotent.
"""

from __future__ import annotations

import re
import unicodedata

_QUOTES = str.maketrans({"\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"', "\u00a0": " ", "\u2009": " "})
_WS = re.compile(r"\s+")


def normalize(text: str) -> str:
    s = unicodedata.normalize("NFKC", text).translate(_QUOTES)
    s = s.replace("\\n", " ")
    s = s.replace("**", "").replace("__", "").replace("`", "")
    return _WS.sub(" ", s).strip()


def words(text: str) -> list[str]:
    return text.split()


def opening_quote(text: str, max_words: int = 30) -> str:
    """First sentence (or first max_words words) of normalized text, verbatim."""
    t = normalize(text)
    m = re.search(r"(?<=[a-z0-9)\]])[.!?](?=\s)", t)
    sent = t[: m.end()] if m else t
    w = sent.split()
    return " ".join(w[:max_words])
