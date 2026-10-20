"""DocTree -> ChangeItems: windowing, release assignment, atomic splitting, symbols, dedup (TDD A4, G4, G5)."""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field

from .adapters import Block, doc_text, parse, window
from .fetch import Fetched
from .models import ChangeItem, SectionType
from .normalize import normalize
from .registry import render

MAX_PARA_ITEM = 1200
MAX_CODE = 600
MAX_SECTION = 2500

_SYMBOL_PATTERNS = [
    re.compile(r"`([^`]{2,80})`"),
    re.compile(r"\b((?:[a-z0-9-]+\.)+k8s\.io/v\d+(?:(?:alpha|beta)\d+)?)\b"),
    re.compile(r"\b((?:batch|policy|autoscaling|apps|extensions|networking|storage|rbac|discovery|events|node|flowcontrol)/v\d+(?:(?:alpha|beta)\d+)?)\b"),
    re.compile(r"\b([A-Z][A-Z0-9]*_[A-Z0-9_]{2,})\b"),
    re.compile(r"(?<![\w-])(--[a-z][a-z0-9-]{2,})"),
]
_REVERT = re.compile(r"\brevert", re.I)


def section_type(heading_path: list[str]) -> SectionType:
    h = " / ".join(heading_path).lower()
    rules: list[tuple[str, SectionType]] = [
        (r"urgent upgrade", "urgent"),
        (r"features removed|removed apis|\bremoved\b|no longer served", "removed"),
        (r"backwards incompatible|breaking changes|migration to version|incompatib|upgrading from", "incompatible"),
        (r"deprecat", "deprecated"),
        (r"python compatibility|dropped support|requirements|minimum|version skew|supported version", "requirements"),
        (r"what's new|new features|minor features|new apis", "new"),
        (r"notable changes|changes|summary|updates to|automatic batching|strict mode|testing", "changed"),
    ]
    for pat, kind in rules:
        if re.search(pat, h):
            return kind
    return "other"


def extract_symbols(text: str) -> list[str]:
    out: list[str] = []
    for pat in _SYMBOL_PATTERNS:
        for m in pat.finditer(text):
            s = m.group(1).strip().strip(".,;:")
            if s and s not in out and not s.isdigit():
                out.append(s)
    return out[:20]


def _sha(*parts: str, n: int = 12) -> str:
    return hashlib.sha1("|".join(parts).encode()).hexdigest()[:n]


@dataclass
class ParsedSource:
    fetched: Fetched
    blocks: list[Block]
    corpus: str
    windows_found: bool
    items: list[ChangeItem] = field(default_factory=list)
    section_texts: dict[str, str] = field(default_factory=dict)


def _release_from_heading(heading_path: list[str], pattern: str) -> str | None:
    rx = re.compile(pattern)
    for h in reversed(heading_path):
        m = rx.search(h)
        if m:
            return m.group(1)
    return None


def _select_blocks(f: Fetched, blocks: list[Block]) -> tuple[list[Block], bool]:
    spec = f.source.spec
    label = f.source.version_label if spec.per_release or spec.tags else (f.source.release or "")
    values = {"release": label, "release_re": re.escape(label)}
    scope = blocks
    if spec.within:
        scope = window(blocks, render(spec.within.start, **values),
                       render(spec.within.end, **values) if spec.within.end else None)
        if not scope:
            return [], False
    if not spec.select:
        return scope, True
    out: list[Block] = []
    for w in spec.select:
        out.extend(window(scope, render(w.start, **values), render(w.end, **values) if w.end else None))
    return out, bool(out)


def build_items(project: str, f: Fetched) -> ParsedSource:
    spec = f.source.spec
    blocks = parse(f.text, spec.format)
    corpus = doc_text(blocks)
    selected, found = _select_blocks(f, blocks)
    ps = ParsedSource(fetched=f, blocks=blocks, corpus=corpus, windows_found=found)
    if not found:
        return ps

    sections: dict[str, list[Block]] = {}
    for b in selected:
        if b.kind != "heading":
            sections.setdefault(" / ".join(b.heading_path), []).append(b)

    def release_for(b: Block) -> str | None:
        if spec.release_from_heading:
            return _release_from_heading(b.heading_path, spec.release_from_heading)
        return f.source.release

    pending: list[Block] = []

    def flush() -> None:
        if not pending:
            return
        rel = release_for(pending[0])
        if rel is None:
            pending.clear()
            return
        text = normalize(" ".join(b.text for b in pending if b.kind != "code"))
        code = " ".join(b.text for b in pending if b.kind == "code")
        if code:
            text = normalize(text + " " + code[:MAX_CODE])
        raw_text = " ".join(b.text for b in pending)
        hp = pending[0].heading_path
        is_revert = spec.revert_scan
        if is_revert and not _REVERT.search(text):
            pending.clear()
            return
        sec_key = " / ".join(hp)
        ps.items.append(ChangeItem(
            item_id=_sha(project, rel, f.source.inventory_id, text),
            project=project, release=rel, source_id=f.source.inventory_id, registry_source=spec.id,
            heading_path=hp, section_type=section_type(hp), text=text,
            raw_span=(pending[0].line_start, pending[-1].line_end),
            symbols=extract_symbols(raw_text),
            parent_id=_sha(f.source.inventory_id, sec_key) if len(sections.get(sec_key, [])) > 1 else None,
            revert_candidate=is_revert,
        ))
        pending.clear()

    prev: Block | None = None
    for b in selected:
        if b.kind == "heading":
            flush()
        elif b.kind == "code":
            if pending and pending[-1].heading_path == b.heading_path:
                pending.append(b)
        elif b.kind in ("list_item", "table_row"):
            flush()
            pending.append(b)
            flush()
        else:  # para: merge short consecutive paragraphs under one heading
            size = sum(len(x.text) for x in pending)
            if pending and (pending[-1].heading_path != b.heading_path or size + len(b.text) > MAX_PARA_ITEM
                            or pending[-1].kind != "para"):
                flush()
            pending.append(b)
        prev = b
    flush()
    ps.section_texts = {
        _sha(f.source.inventory_id, k): normalize(k + ": " + " ".join(b.text for b in v))[:MAX_SECTION]
        for k, v in sections.items()
    }
    return ps


def dedup(items: list[ChangeItem]) -> list[ChangeItem]:
    """Exact-duplicate removal across sources; provenance is kept in also_in (A4)."""
    seen: dict[tuple[str, str], ChangeItem] = {}
    out: list[ChangeItem] = []
    for it in items:
        key = (it.release, hashlib.sha1(it.text.encode()).hexdigest())
        if key in seen:
            if it.source_id not in seen[key].also_in:
                seen[key].also_in.append(it.source_id)
            continue
        seen[key] = it
        out.append(it)
    return out
