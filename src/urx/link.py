"""B3 linker: in-process BM25 over change items and duplicate-path merging (G22)."""

from __future__ import annotations

import math
import re
from collections import Counter

from .models import LEVEL_ORDER, RiskPath

_TOKEN = re.compile(r"[A-Za-z0-9_./-]+")


def tokenize(text: str) -> list[str]:
    return [t.lower().strip("./-") for t in _TOKEN.findall(text) if len(t) > 1]


class BM25:
    def __init__(self, docs: list[str], k1: float = 1.4, b: float = 0.75) -> None:
        self.tokens = [tokenize(d) for d in docs]
        self.k1, self.b = k1, b
        self.avg = sum(map(len, self.tokens)) / max(len(self.tokens), 1)
        df: Counter = Counter()
        for t in self.tokens:
            df.update(set(t))
        n = len(self.tokens)
        self.idf = {w: math.log(1 + (n - c + 0.5) / (c + 0.5)) for w, c in df.items()}
        self.tf = [Counter(t) for t in self.tokens]

    def search(self, query: str, k: int = 5) -> list[tuple[int, float]]:
        q = tokenize(query)
        scores = []
        for i, tf in enumerate(self.tf):
            dl = len(self.tokens[i])
            s = 0.0
            for w in q:
                if w in tf:
                    f = tf[w]
                    s += self.idf.get(w, 0) * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * dl / self.avg))
            if s > 0:
                scores.append((i, s))
        return sorted(scores, key=lambda x: -x[1])[:k]


def path_text(p: RiskPath) -> str:
    return " ".join([p.path_name, p.description, p.primary_symbol, " ".join(p.symbols)]
                    + [c.statement for c in p.conditions])


def full_symbol(s: str) -> str:
    s = s.strip().strip("`").replace("()", "").strip().lower()
    s = re.sub(r"[\s-]+", "", s)
    return s[:-3] if s.endswith(".js") else s


def symbols_equal(a: str, b: str) -> bool:
    """Exact match, or a bare name against a full module path (django.utils.encoding.force_text ~ force_text).

    Short dotted names (ReactDOM.render vs root.render) are NOT equal: the last component alone is ambiguous.
    """
    fa, fb = full_symbol(a), full_symbol(b)
    if not fa or not fb:
        return False
    if fa == fb:
        return True
    short, long_ = sorted((fa, fb), key=len)
    return "." not in short and long_.count(".") >= 2 and long_.endswith("." + short)


def _same_risk(a: RiskPath, b: RiskPath) -> bool:
    if a.introduced_in != b.introduced_in:
        return False
    if re.sub(r"\W+", " ", a.path_name.lower()).strip() == re.sub(r"\W+", " ", b.path_name.lower()).strip():
        return True
    return a.risk_type == b.risk_type and symbols_equal(a.primary_symbol, b.primary_symbol)


def merge_into(base: RiskPath, other: RiskPath) -> None:
    for oc in other.conditions:
        match = next((c for c in base.conditions if c.category == oc.category), None)
        if match is None:
            if oc.category != "version":
                base.conditions.append(oc)
            continue
        seen = {(e.source_id, e.quote) for e in match.evidence}
        for e in oc.evidence:
            if (e.source_id, e.quote) not in seen:
                match.evidence.append(e)
                seen.add((e.source_id, e.quote))
        match.ambiguities += [a for a in oc.ambiguities if a not in match.ambiguities]
        have = {q.query for q in match.search_queries}
        match.search_queries += [q for q in oc.search_queries if q.query not in have]
    base.suggested_actions += [a for a in other.suggested_actions if a not in base.suggested_actions]
    base.symbols += [s for s in other.symbols if s not in base.symbols]
    base.source_item_ids += [i for i in other.source_item_ids if i not in base.source_item_ids]
    base.merged_from += [other.path_id, *other.merged_from]
    if LEVEL_ORDER.index(other.risk_level) > LEVEL_ORDER.index(base.risk_level):
        base.risk_level = other.risk_level


def merge_duplicates(paths: list[RiskPath]) -> tuple[list[RiskPath], list[dict]]:
    parent = list(range(len(paths)))

    def find(i: int) -> int:
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for i in range(len(paths)):
        for j in range(i + 1, len(paths)):
            if _same_risk(paths[i], paths[j]):
                parent[find(j)] = find(i)
    groups: dict[int, list[RiskPath]] = {}
    for i, p in enumerate(paths):
        groups.setdefault(find(i), []).append(p)
    out, log = [], []
    for g in groups.values():
        g.sort(key=lambda p: (-sum(len(c.evidence) for c in p.conditions), p.path_id))
        base = g[0]
        for other in g[1:]:
            merge_into(base, other)
            log.append({"kept": base.path_id, "merged": other.path_id, "release": base.introduced_in,
                        "symbol": base.primary_symbol})
        out.append(base)
    return out, log
