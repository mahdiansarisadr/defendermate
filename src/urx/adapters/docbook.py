"""DocBook SGML adapter (PostgreSQL release notes). Resolves xrefs instead of dropping them (L10, G7)."""

from __future__ import annotations

import bisect
import html
import logging
import re

from .base import Block, assign_heading_paths

log = logging.getLogger(__name__)

XREF_MAP = {"pgupgrade": "pg_upgrade", "app-pgdump": "pg_dump", "app-pg-dumpall": "pg_dumpall",
            "app-pgdumpall": "pg_dumpall", "app-pgrestore": "pg_restore", "app-psql": "psql"}
_CODE_TAGS = {"literal", "varname", "function", "command", "option", "type", "structname", "structfield",
              "filename", "application", "replaceable", "envar", "parameter", "systemitem", "classname",
              "programlisting", "returnvalue", "symbol", "token", "sqlstate", "property"}
_SECT = re.compile(r"^sect(\d)$|^(appendix|chapter)$")
unknown_linkends: set[str] = set()


def resolve_linkend(linkend: str) -> str:
    if linkend in XREF_MAP:
        return XREF_MAP[linkend]
    if linkend.startswith("guc-"):
        return linkend[4:].replace("-", "_")
    if linkend.startswith("app-"):
        return linkend[4:].replace("-", "_")
    if linkend.startswith("sql-"):
        return linkend[4:].replace("-", " ").upper()
    unknown_linkends.add(linkend)
    return linkend


def _inline(fragment: str) -> str:
    s = re.sub(r"<!--.*?-->", "", fragment, flags=re.S)
    s = re.sub(r"<ulink\b[^>]*>\s*&sect;\s*</ulink>", "", s)
    s = re.sub(r'<xref\s+linkend="([^"]+)"\s*/?>', lambda m: f"`{resolve_linkend(m.group(1))}`", s)
    for tag in _CODE_TAGS:
        s = re.sub(rf"<{tag}\b[^>]*>(.*?)</{tag}>", r"`\1`", s, flags=re.S)
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("&sect;", "").replace("&commit_baseurl;", "")
    s = re.sub(r"&(\w+);", lambda m: html.unescape(m.group(0)) if m.group(1) in {"lt", "gt", "amp", "quot", "apos", "nbsp", "mdash", "ndash", "hellip"} else m.group(1), s)
    s = s.replace("``", "")
    return re.sub(r"\s+", " ", s).strip()


def parse(raw: str) -> list[Block]:
    # Comments contain author/commit noise; blank them while keeping offsets.
    raw = re.sub(r"<!--.*?-->", lambda m: " " * len(m.group(0)), raw, flags=re.S)
    # <formalpara><title> is an inline label (e.g. "Release date:"), not a section heading.
    raw = re.sub(r"<formalpara>\s*<title>(.*?)</title>",
                 lambda m: "<formalpara><para>" + m.group(1) + "</para>", raw, flags=re.S)
    line_starts = [0] + [m.end() for m in re.finditer(r"\n", raw)]

    def line_of(pos: int) -> int:
        return bisect.bisect_right(line_starts, pos)

    blocks: list[Block] = []
    depth = 0
    # Tokenize the structural elements; inline markup is handled by _inline.
    pat = re.compile(r"<(/?)(sect\d|appendix|chapter|title|listitem|para|simpara|programlisting)\b[^>]*>", re.S)
    pos = 0
    stack: list[tuple[str, int]] = []
    in_listitem = 0
    li_start = 0
    while True:
        m = pat.search(raw, pos)
        if not m:
            break
        closing, tag = m.group(1) == "/", m.group(2)
        pos = m.end()
        if _SECT.match(tag):
            depth += -1 if closing else 1
            continue
        if not closing:
            if tag == "listitem":
                in_listitem += 1
                if in_listitem == 1:
                    li_start = m.end()
                continue
            if tag in ("title", "para", "simpara", "programlisting") and not (in_listitem and tag != "title"):
                end = raw.find(f"</{tag}>", m.end())
                if end < 0:
                    continue
                text = _inline(raw[m.end():end])
                if text:
                    if tag == "title":
                        blocks.append(Block("heading", text, depth, line_of(m.start()), line_of(end)))
                    elif tag == "programlisting":
                        blocks.append(Block("code", text, 0, line_of(m.start()), line_of(end)))
                    else:
                        blocks.append(Block("para", text, 0, line_of(m.start()), line_of(end)))
                pos = end
        else:
            if tag == "listitem":
                in_listitem -= 1
                if in_listitem == 0:
                    body = raw[li_start:m.start()]
                    paras = re.findall(r"<(?:para|simpara)\b[^>]*>(.*?)</(?:para|simpara)>", body, flags=re.S)
                    text = " ".join(t for t in (_inline(p) for p in paras) if t) or _inline(body)
                    if text:
                        blocks.append(Block("list_item", text, 0, line_of(li_start), line_of(m.start())))
    for u in sorted(unknown_linkends):
        log.debug("unknown linkend %s", u)
    return assign_heading_paths(blocks)
