"""Fetcher with pinning, hashing, stub detection and an offline cache (TDD A1, G1)."""

from __future__ import annotations

import hashlib
import json
import os
import re
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import httpx
import yaml

from . import config
from .registry import ResolvedSource

EXT = {"rst": "txt", "markdown": "md", "mdx": "mdx", "docbook": "sgml", "json": "json"}


class OfflineCacheMiss(RuntimeError):
    pass


@dataclass
class Fetched:
    source: ResolvedSource
    path: Path | None
    meta: dict
    absent: bool = False      # optional probe that returned 404
    stub_reason: str | None = None

    @property
    def text(self) -> str:
        assert self.path is not None
        return self.path.read_text(encoding="utf-8")


def cache_paths(project: str, src: ResolvedSource) -> tuple[Path, Path]:
    base = config.CACHE_DIR / config.slugify(project) / src.registry_source
    name = re.sub(r"[^A-Za-z0-9._-]", "_", src.version_label or "doc")
    return base / f"{name}.{EXT[src.spec.format]}", base / f"{name}.meta.json"


def _git_ref(raw_url: str) -> tuple[str, str, str, str] | None:
    m = re.match(r"https://raw\.githubusercontent\.com/([^/]+)/([^/]+)/(.+)$", raw_url)
    if not m:
        return None
    owner, repo, rest = m.groups()
    segs = rest.split("/")
    n = 2 if segs[0] == "stable" else 1
    return owner, repo, "/".join(segs[:n]), "/".join(segs[n:])


def _resolve_commit(client: httpx.Client, raw_url: str) -> str | None:
    parts = _git_ref(raw_url)
    if not parts:
        return None
    owner, repo, ref, path = parts
    headers = {"Accept": "application/vnd.github+json"}
    if tok := os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {tok}"
    try:
        r = client.get(f"https://api.github.com/repos/{owner}/{repo}/commits",
                       params={"path": path, "sha": ref, "per_page": 1}, headers=headers)
        if r.status_code == 200 and r.json():
            return r.json()[0]["sha"]
    except httpx.HTTPError:
        pass
    return None


def pinned_ref(src: ResolvedSource, commit: str | None) -> str:
    parts = _git_ref(src.raw_url)
    if parts:
        ref = parts[2]
        return f"{ref}@{commit[:12]}" if commit else f"{src.spec.pin}:{ref}"
    if "pypi.org" in src.raw_url:
        return f"pypi:{src.version_label}"
    return src.spec.pin


_FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
_COMMENTS = re.compile(r"\{/\*.*?\*/\}|<!--.*?-->", re.S)


def detect_stub(raw: str, fmt: str) -> str | None:
    """G1: a stub is a transclusion pointer with no body, or an (almost) empty document."""
    if fmt == "json":
        return None
    body = raw
    fm = _FRONTMATTER.match(raw)
    if fm:
        body = raw[fm.end():]
        try:
            front = yaml.safe_load(fm.group(1)) or {}
        except yaml.YAMLError:
            front = {}
        if isinstance(front, dict) and front.get("source") and not _COMMENTS.sub("", body).strip():
            return "transclusion_stub"
    if len(re.sub(r"\s+", " ", _COMMENTS.sub("", body)).strip()) < 200:
        return "empty_document"
    return None


def _get(client: httpx.Client, url: str) -> httpx.Response:
    last: Exception | None = None
    for attempt in range(3):
        try:
            r = client.get(url)
            if r.status_code < 500:
                return r
        except httpx.HTTPError as e:
            last = e
        time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"fetch failed for {url}: {last}")


def fetch_all(project: str, sources: list[ResolvedSource], offline: bool, refresh: bool = False,
              log=lambda *a, **k: None) -> list[Fetched]:
    out: list[Fetched] = []
    stop_probe: set[tuple[str, str | None]] = set()
    client = None if offline else httpx.Client(timeout=30, follow_redirects=True,
                                               headers={"User-Agent": "urx/0.1 (research; public docs only)"})
    try:
        for src in sources:
            group = (src.registry_source, src.release)
            if src.optional and group in stop_probe:
                continue
            data_path, meta_path = cache_paths(project, src)
            if meta_path.exists() and not refresh:
                meta = json.loads(meta_path.read_text())
            elif offline:
                if src.optional:
                    stop_probe.add(group)
                    continue
                raise OfflineCacheMiss(f"{src.inventory_id}: not cached at {data_path}; run without --offline")
            else:
                assert client is not None
                r = _get(client, src.raw_url)
                retrieved = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                meta = {"inventory_id": src.inventory_id, "url": src.url, "raw_url": src.raw_url,
                        "status_code": r.status_code, "retrieved_at": retrieved}
                data_path.parent.mkdir(parents=True, exist_ok=True)
                if r.status_code == 200:
                    data_path.write_bytes(r.content)
                    commit = _resolve_commit(client, src.raw_url) if src.spec.pin == "commit" else None
                    meta.update(content_hash="sha256:" + hashlib.sha256(r.content).hexdigest(),
                                pinned_ref=pinned_ref(src, commit), bytes=len(r.content))
                elif not src.optional:
                    raise RuntimeError(f"{src.inventory_id}: HTTP {r.status_code} for {src.raw_url}")
                meta_path.write_text(json.dumps(meta, indent=2))
                log("fetched", source=src.inventory_id, status=r.status_code)
            if meta.get("status_code") != 200:
                stop_probe.add(group)
                continue
            f = Fetched(source=src, path=data_path, meta=meta)
            if not src.spec.revert_scan:
                f.stub_reason = detect_stub(f.text, src.spec.format)
            out.append(f)
    finally:
        if client:
            client.close()
    return out
