"""Version path planning (TDD C1, G2). No version arithmetic: releases come from the registry."""

from __future__ import annotations

from packaging.version import InvalidVersion, Version
from pydantic import BaseModel

from .registry import Registry


def vkey(v: str) -> Version:
    try:
        return Version(v)
    except InvalidVersion:
        return Version("0")


def vcmp_le(a: str, b: str) -> bool:
    return vkey(a) <= vkey(b)


class Plan(BaseModel):
    project: str
    current_version: str
    target_version: str
    mode: str
    releases: list[str]
    future_releases: list[str]
    hops: int


def plan(reg: Registry, current: str, target: str) -> Plan:
    known = sorted(reg.known_releases, key=vkey)
    if target not in known:
        raise ValueError(f"{reg.project}: target {target} not in known_releases {known}")
    if vkey(current) >= vkey(target):
        raise ValueError(f"{reg.project}: current {current} must be older than target {target}")
    if reg.traversal.mode == "single":
        releases = [target]
    else:
        releases = [r for r in known if vkey(current) < vkey(r) <= vkey(target)]
    after = [r for r in known if vkey(r) > vkey(target)]
    return Plan(
        project=reg.project, current_version=current, target_version=target, mode=reg.traversal.mode,
        releases=releases, future_releases=after[: reg.future_removal_horizon], hops=len(releases),
    )
