from __future__ import annotations

from . import docbook, markdown, rst
from .base import Block, doc_text, window

PARSERS = {"rst": rst.parse, "markdown": markdown.parse, "mdx": markdown.parse, "docbook": docbook.parse}


def parse(raw: str, fmt: str) -> list[Block]:
    return PARSERS[fmt](raw)


__all__ = ["Block", "PARSERS", "parse", "doc_text", "window"]
