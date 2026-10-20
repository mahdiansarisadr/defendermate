"""Shared DocTree representation (TDD A2) and block-level windowing (G5)."""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from ..normalize import normalize


@dataclass
class Block:
    kind: str                 # heading | para | list_item | code | table_row
    text: str                 # adapter output; may contain `code` spans (stripped by normalize)
    level: int = 0            # heading level; 0 for non-headings
    line_start: int = 0
    line_end: int = 0
    heading_path: list[str] = field(default_factory=list)

    @property
    def norm(self) -> str:
        return normalize(self.text)


def assign_heading_paths(blocks: list[Block]) -> list[Block]:
    stack: list[tuple[int, str]] = []
    for b in blocks:
        if b.kind == "heading":
            while stack and stack[-1][0] >= b.level:
                stack.pop()
            stack.append((b.level, b.norm))
            b.heading_path = [t for _, t in stack]
        else:
            b.heading_path = [t for _, t in stack]
    return blocks


def doc_text(blocks: list[Block]) -> str:
    """Normalized full-document text; the corpus quotes are verified against."""
    return normalize(" ".join(b.text for b in blocks))


def window(blocks: list[Block], start: str, end: str | None) -> list[Block]:
    """Blocks from the heading matching `start` up to the heading matching `end`.

    `end=None` stops at the next heading of the same or higher level. Anchors are
    regexes over heading text, never heading depth (L9).
    """
    rs = re.compile(start)
    re_end = re.compile(end) if end else None
    out: list[Block] = []
    start_level = None
    for b in blocks:
        if start_level is None:
            if b.kind == "heading" and rs.search(b.norm):
                start_level = b.level
                out.append(b)
            continue
        if b.kind == "heading":
            if re_end is not None and re_end.search(b.norm):
                break
            if re_end is None and b.level <= start_level:
                break
        out.append(b)
    return out
