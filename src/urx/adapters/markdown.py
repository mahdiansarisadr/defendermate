"""Markdown / MDX adapter (Kubernetes, React, Next.js)."""

from __future__ import annotations

import re

from .base import Block, assign_heading_paths

_FRONT = re.compile(r"\A---\n.*?\n---\n", re.S)
_JSX_COMMENT = re.compile(r"\{/\*.*?\*/\}", re.S)
_HTML_COMMENT = re.compile(r"<!--.*?-->", re.S)
_HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
_ANCHOR = re.compile(r"\s*\{#[^}]*\}\s*$")
_BULLET = re.compile(r"^(\s*)([*\-+]|\d+[.)])\s+(.*)$")
_PR_REFS = re.compile(r"\s*\(\[#\d+\]\([^)]*\)(?:\s*,\s*\[[#@][^\]]+\]\([^)]*\))*\)")
_SIG = re.compile(r"\s*\[SIG [^\]]*\]")
_IMG = re.compile(r"!\[[^\]]*\]\([^)]*\)")
_LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)")
_REFLINK = re.compile(r"\[([^\]]+)\]\[[^\]]*\]")
_TAG = re.compile(r"</?[A-Za-z][\w.]*(?:\s[^<>]*)?/?>")


def _outside_code(text: str, fn) -> str:
    parts = re.split(r"(`[^`]*`)", text)
    return "".join(p if p.startswith("`") and p.endswith("`") and len(p) > 1 else fn(p) for p in parts)


def convert_inline(text: str) -> str:
    text = _PR_REFS.sub("", text)
    text = _SIG.sub("", text)
    text = _IMG.sub("", text)
    text = _LINK.sub(r"\1", text)
    text = _REFLINK.sub(r"\1", text)
    text = _outside_code(text, lambda s: _TAG.sub("", s))
    return text.strip()


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def parse(raw: str) -> list[Block]:
    # Remove frontmatter/comments but keep line numbering stable.
    def blank(m: re.Match) -> str:
        return "\n" * m.group(0).count("\n")

    raw = _FRONT.sub(blank, raw)
    raw = _JSX_COMMENT.sub(blank, raw)
    raw = _HTML_COMMENT.sub(blank, raw)
    lines = raw.splitlines()
    blocks: list[Block] = []
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        s = line.strip()
        if not s:
            i += 1
            continue
        if s.startswith("```") or s.startswith("~~~"):
            fence = s[:3]
            start = i
            i += 1
            body = []
            while i < n and not lines[i].strip().startswith(fence):
                body.append(lines[i])
                i += 1
            i += 1
            code = "\n".join(body).strip()
            if code:
                blocks.append(Block("code", code, 0, start + 1, i))
            continue
        hm = _HEADING.match(s) if _indent(line) < 4 else None
        if hm:
            title = convert_inline(_ANCHOR.sub("", hm.group(2)))
            blocks.append(Block("heading", title, len(hm.group(1)), i + 1, i + 1))
            i += 1
            continue
        if s.startswith("|"):
            if not re.match(r"^\|?\s*:?-{2,}", s):
                cells = [convert_inline(c.strip()) for c in s.strip("|").split("|")]
                blocks.append(Block("table_row", " | ".join(c for c in cells if c), 0, i + 1, i + 1))
            i += 1
            continue
        bm = _BULLET.match(line)
        if bm:
            base = len(bm.group(1))
            start = i
            parts = [bm.group(3)]
            i += 1
            while i < n:
                nxt = lines[i]
                if not nxt.strip():
                    if i + 1 < n and lines[i + 1].strip() and _indent(lines[i + 1]) > base \
                            and not lines[i + 1].strip().startswith("```"):
                        i += 1
                        continue
                    break
                if _indent(nxt) <= base and (_BULLET.match(nxt) or _HEADING.match(nxt.strip())):
                    break
                if nxt.strip().startswith("```"):
                    break
                parts.append(nxt.strip())
                i += 1
            blocks.append(Block("list_item", convert_inline(" ".join(parts)), 0, start + 1, i))
            continue
        start = i
        parts = []
        while i < n and lines[i].strip():
            t = lines[i].strip()
            if parts and (_BULLET.match(lines[i]) or _HEADING.match(t) or t.startswith("```") or t.startswith("|")):
                break
            parts.append(t.lstrip("> ").strip() if t.startswith(">") else t)
            i += 1
        text = convert_inline(" ".join(parts))
        if text:
            blocks.append(Block("para", text, 0, start + 1, i))
    return assign_heading_paths(blocks)
