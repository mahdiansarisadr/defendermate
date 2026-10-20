"""B1 triage: cheap model over every item, plus a strong-model recall sweep over 'noise' (L8)."""

from __future__ import annotations

import json
import re
from concurrent.futures import ThreadPoolExecutor
from typing import Literal

from pydantic import BaseModel

from . import config
from .llm import LLMClient
from .models import ChangeItem, TriageLabel

BATCH = 20
SIGNAL = re.compile(r"\b(removed?|no longer|now raises|default|deprecat\w*|must|requires?|dropped|renamed|"
                    r"incompatib\w*|breaking|minimum|unsupported|not supported)\b", re.I)


class _Out(BaseModel):
    item_id: str
    label: Literal["risk", "context", "noise"]
    reason: str


class _Batch(BaseModel):
    labels: list[_Out]


def _run_batch(client: LLMClient, batch: list[ChangeItem], ctx: dict, tier: str) -> dict[str, _Out]:
    lines = "\n".join(json.dumps({"item_id": i.item_id, "section": " / ".join(i.heading_path[-3:]),
                                  "text": i.text[:1500]}, ensure_ascii=False) for i in batch)
    res = client.complete("triage.v1", {**ctx, "release": batch[0].release, "items_jsonl": lines}, _Batch,
                          model_tier=tier, max_tokens=6000, stage="triage" if tier == "cheap" else "triage_sweep")
    return {o.item_id: o for o in res.labels}


def triage(client: LLMClient, items: list[ChangeItem], ctx: dict, source_titles: dict[str, str],
           log=lambda *a, **k: None) -> tuple[list[TriageLabel], list[dict]]:
    groups: dict[tuple[str, str], list[ChangeItem]] = {}
    for it in items:
        groups.setdefault((it.source_id, it.release), []).append(it)
    batches = [(g[i:i + BATCH], src) for (src, _), g in groups.items() for i in range(0, len(g), BATCH)]

    results: dict[str, _Out] = {}

    def work(arg):
        batch, src = arg
        return _run_batch(client, batch, {**ctx, "source_title": source_titles.get(src, src)}, "cheap")

    with ThreadPoolExecutor(config.MAX_WORKERS) as ex:
        for out in ex.map(work, batches):
            results.update(out)
    log("triage_done", batches=len(batches))

    labels: dict[str, TriageLabel] = {}
    for it in items:
        o = results.get(it.item_id)
        if o is None:  # model skipped the item: fail open to "risk" (prompt rule: when unsure, risk)
            labels[it.item_id] = TriageLabel(item_id=it.item_id, label="risk", reason="missing triage label; defaulted to risk")
        else:
            labels[it.item_id] = TriageLabel(item_id=it.item_id, label=o.label, reason=o.reason)

    # Recall sweep: strong model re-checks 'noise' items that carry risk signal words.
    sweep = [it for it in items if labels[it.item_id].label == "noise" and SIGNAL.search(it.text)]
    disagreements: list[dict] = []
    if sweep:
        sweep_batches: dict[str, list[ChangeItem]] = {}
        for it in sweep:
            sweep_batches.setdefault(it.source_id, []).append(it)
        arg_list = [(g[i:i + BATCH], s) for s, g in sweep_batches.items() for i in range(0, len(g), BATCH)]

        def sweep_work(arg):
            batch, src = arg
            return _run_batch(client, batch, {**ctx, "source_title": source_titles.get(src, src)}, "strong")

        with ThreadPoolExecutor(config.MAX_WORKERS) as ex:
            for out in ex.map(sweep_work, arg_list):
                for iid, o in out.items():
                    if iid in labels and o.label != "noise":
                        disagreements.append({"item_id": iid, "cheap": "noise", "strong": o.label, "reason": o.reason})
                        labels[iid] = TriageLabel(item_id=iid, label=o.label, reason=o.reason, swept=True)
        log("sweep_done", swept=len(sweep), flipped=len(disagreements))
    return [labels[it.item_id] for it in items], disagreements
