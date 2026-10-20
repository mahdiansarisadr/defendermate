"""reStructuredText adapter (Django docs)."""

from __future__ import annotations

import re

from .base import Block, assign_heading_paths

_UNDER = re.compile(r"^([=\-~^\"'`#*+<>_.:])\1{2,}\s*$")
_CODE_ROLES = {
    "setting", "class", "meth", "func", "attr", "mod", "data", "exc", "option", "envvar", "djadmin",
    "lookup", "ttag", "tfilter", "fieldlookup", "obj", "py:class", "py:meth", "py:func", "py:attr",
    "py:mod", "py:data", "py:exc", "py:obj", "djadminopt", "templatetag", "rfc", "pep",
}
_ROLE = re.compile(r":([\w:]+):`([^`]+)`")
_LINK = re.compile(r"`([^`<]+?)\s*<[^>]+>`__?")
_REF = re.compile(r"`([^`]+)`_")
_BULLET = re.compile(r"^(\s*)([*\-+]|#\.|\d+\.)\s+(.*)$")


def convert_inline(text: str) -> str:
    def role(m: re.Match) -> str:
        name, body = m.group(1), m.group(2).strip()
        lab = re.match(r"(.*?)\s*<(.+)>$", body, re.S)
        if lab and lab.group(1):
            shown = lab.group(1)
        else:
            target = lab.group(2) if lab else body
            shown = target
            if shown.startswith("~"):
                shown = shown[1:].split(".")[-1]
            shown = shown.lstrip(".!")
        if name == "ticket":
            return f"#{shown}"
        if name in _CODE_ROLES:
            return f"`{shown}`"
        return shown

    text = _ROLE.sub(role, text)
    text = _LINK.sub(r"\1", text)
    text = _REF.sub(r"\1", text)
    text = text.replace("``", "`")
    text = re.sub(r"(?<=\S)::(\s|$)", r":\1", text)
    return text


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def parse(raw: str) -> list[Block]:
    lines = raw.splitlines()
    blocks: list[Block] = []
    styles: list[tuple[str, bool]] = []
    i, n = 0, len(lines)
    expect_code = False

    def heading_level(ch: str, over: bool) -> int:
        key = (ch, over)
        if key not in styles:
            styles.append(key)
        return styles.index(key) + 1

    while i < n:
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1
            continue
        # overline + title + underline
        if _UNDER.match(line) and i + 2 < n and lines[i + 1].strip() and _UNDER.match(lines[i + 2]) \
                and lines[i + 2].strip()[0] == stripped[0]:
            blocks.append(Block("heading", convert_inline(lines[i + 1].strip()), heading_level(stripped[0], True), i + 1, i + 3))
            i += 3
            continue
        # title + underline
        if i + 1 < n and _UNDER.match(lines[i + 1]) and _indent(line) == 0 \
                and len(lines[i + 1].strip()) >= len(stripped) and not _UNDER.match(line):
            blocks.append(Block("heading", convert_inline(stripped), heading_level(lines[i + 1].strip()[0], False), i + 1, i + 2))
            i += 2
            continue
        if expect_code and _indent(line) == 0:
            expect_code = False
        # literal / directive code blocks: indented body
        if expect_code or re.match(r"^\.\.\s+(code-block|code|console|sourcecode)::", stripped):
            base = _indent(line)
            start = i
            if not expect_code:
                i += 1
                while i < n and (not lines[i].strip() or lines[i].strip().startswith(":")) and i - start < 3:
                    i += 1
            body = []
            while i < n and (not lines[i].strip() or _indent(lines[i]) > (base if not expect_code else base - 1)):
                body.append(lines[i])
                i += 1
            expect_code = False
            code = "\n".join(l.strip() for l in body if l.strip())
            if code:
                blocks.append(Block("code", code, 0, start + 1, i))
            continue
        # comments, targets, other directives: skip the directive line and keep its indented content
        if stripped.startswith(".."):
            m = re.match(r"^\.\.\s+([\w-]+)::\s*(.*)$", stripped)
            base = _indent(line)
            i += 1
            if not m:
                while i < n and (not lines[i].strip() or _indent(lines[i]) > base):
                    i += 1
            elif m.group(1) in {"toctree", "highlight", "currentmodule", "module", "contents", "include"}:
                while i < n and (not lines[i].strip() or _indent(lines[i]) > base):
                    i += 1
            elif m.group(2).strip():
                blocks.append(Block("para", convert_inline(f"{m.group(1).replace('-', ' ').capitalize()}: {m.group(2)}"), 0, i, i))
            continue
        # bullet items (one top-level bullet = one block, nested content included)
        bm = _BULLET.match(line)
        if bm:
            base = len(bm.group(1))
            start = i
            parts = [bm.group(3)]
            i += 1
            while i < n:
                nxt = lines[i]
                if not nxt.strip():
                    if i + 1 < n and lines[i + 1].strip() and _indent(lines[i + 1]) > base:
                        i += 1
                        continue
                    break
                if _indent(nxt) <= base:
                    break
                parts.append(nxt.strip())
                i += 1
            text = " ".join(parts)
            blocks.append(Block("list_item", convert_inline(text), 0, start + 1, i))
            if text.rstrip().endswith("::"):
                expect_code = True
            continue
        # paragraph
        start = i
        parts = []
        while i < n and lines[i].strip():
            if _BULLET.match(lines[i]) and parts:
                break
            if i + 1 < n and _UNDER.match(lines[i + 1]) and not _UNDER.match(lines[i]) and _indent(lines[i]) == 0 and parts:
                break
            parts.append(lines[i].strip())
            i += 1
        text = " ".join(parts)
        if text.endswith("::"):
            expect_code = True
        blocks.append(Block("para", convert_inline(text), 0, start + 1, i))
    return assign_heading_paths(blocks)
