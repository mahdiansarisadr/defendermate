"""Project registry: the scaling mechanism. Adding a project = one YAML file (TDD 5, 17.5)."""

from __future__ import annotations

import re
from functools import lru_cache
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field

from . import config
from .models import SourceType


class Window(BaseModel):
    model_config = ConfigDict(extra="forbid")
    start: str
    end: str | None = None


class RegistrySource(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    title: str
    type: SourceType
    tier: Literal[1, 2, 3]
    url_template: str
    raw_template: str
    format: Literal["rst", "markdown", "mdx", "docbook", "json"]
    per_release: bool = False
    release: str | None = None
    tags: dict[str, str] | None = None
    select: list[Window] | None = None
    within: Window | None = None
    release_from_heading: str | None = None
    revert_scan: bool = False
    patch_max: int = 0
    include_current: bool = False
    pin: Literal["tag", "branch", "commit"] = "branch"
    why_relevant: str = ""


class CrossProject(BaseModel):
    project: str
    current_version: str
    target_version: str


class VersionFactSpec(BaseModel):
    source_id: str
    fields: dict[str, str]
    labels: dict[str, str] = Field(default_factory=dict)
    cross_project: dict[str, CrossProject] = Field(default_factory=dict)


class Traversal(BaseModel):
    mode: Literal["walk_minors", "walk_majors", "jump_majors", "single"]


class Registry(BaseModel):
    model_config = ConfigDict(extra="forbid")
    project: str
    version_scheme: str
    traversal: Traversal
    known_releases: list[str]
    future_removal_horizon: int = 0
    coverage_gaps: list[str] = Field(default_factory=list)
    sources: list[RegistrySource]
    version_facts: list[VersionFactSpec] = Field(default_factory=list)


class ResolvedSource(BaseModel):
    """One fetchable document: a registry source instantiated for a release, patch or tag."""

    inventory_id: str
    registry_source: str
    release: str | None          # release that items belong to; None = assign from headings
    version_label: str           # the concrete version or tag the URL points at
    title: str
    url: str
    raw_url: str
    spec: RegistrySource
    optional: bool = False       # patch probes: 404 means "no such patch", not an error


@lru_cache(maxsize=None)
def load_registry(project: str) -> Registry:
    path = config.REGISTRY_DIR / f"{config.slugify(project)}.yaml"
    if not path.exists():
        raise FileNotFoundError(f"No registry for {project!r} at {path}")
    return Registry.model_validate(yaml.safe_load(path.read_text()))


def list_projects() -> list[str]:
    return [load_registry(p.stem).project for p in sorted(config.REGISTRY_DIR.glob("*.yaml"))]


def render(template: str, **values: str) -> str:
    def sub(m: re.Match) -> str:
        key = m.group(1)
        return values[key] if key in values else m.group(0)

    return re.sub(r"\{(\w+)\}", sub, template)


def template_values(release: str, current: str, target: str, tag: str = "") -> dict[str, str]:
    return {"release": release, "release_re": re.escape(release), "target": target, "current": current, "tag": tag}


def expand_sources(reg: Registry, releases: list[str], current: str, target: str) -> list[ResolvedSource]:
    out: list[ResolvedSource] = []
    for s in reg.sources:
        def make(release: str | None, label: str, tag: str = "", optional: bool = False) -> ResolvedSource:
            v = template_values(label, current, target, tag)
            suffix = tag or label
            inv = f"{s.id}@{suffix}" if suffix else s.id
            return ResolvedSource(
                inventory_id=inv, registry_source=s.id, release=release, version_label=tag or label,
                title=render(s.title, **v), url=render(s.url_template, **v), raw_url=render(s.raw_template, **v),
                spec=s, optional=optional,
            )

        if s.tags:
            for tag, rel in s.tags.items():
                if rel in releases or rel == current:
                    out.append(make(rel, rel, tag=tag))
        elif s.revert_scan:
            for rel in releases:
                for n in range(1, s.patch_max + 1):
                    out.append(make(rel, f"{rel}.{n}", optional=True))
        elif s.per_release:
            rels = list(releases) + ([current] if s.include_current else [])
            for rel in rels:
                out.append(make(rel, rel))
        elif s.release is not None:
            if s.release == "*" or s.release in releases:
                out.append(make(s.release, ""))
        else:
            out.append(make(None, ""))
    return out
