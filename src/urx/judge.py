"""C5 LLM entailment judge, batched per path. Verdicts feed the rubric; not_supported -> uncertain."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

from pydantic import BaseModel

from . import config
from .llm import ExtractionFailed, LLMClient
from .models import JudgeResult, JudgeVerdict, RiskPath


class _Verdict(BaseModel):
    condition_id: str
    verdict: JudgeVerdict
    missing: str


class _Batch(BaseModel):
    verdicts: list[_Verdict]


def judge_claims(client: LLMClient, claims: list[dict], stage: str = "judge") -> dict[str, _Verdict]:
    res = client.complete("judge.v1", {"claims_json": claims}, _Batch, model_tier="strong", max_tokens=4000, stage=stage)
    return {v.condition_id: v for v in res.verdicts}


def judge_paths(client: LLMClient, paths: list[RiskPath], log=lambda *a, **k: None) -> dict:
    def work(p: RiskPath):
        claims = [{"condition_id": c.condition_id, "claim": c.statement,
                   "quotes": [e.quote for e in c.evidence if e.quote]}
                  for c in p.conditions if c.derived_by != "rule" and any(e.quote for e in c.evidence)]
        if not claims:
            return p, {}
        try:
            return p, judge_claims(client, claims)
        except ExtractionFailed:
            return p, None

    stats = {"supported": 0, "partially_supported": 0, "not_supported": 0, "failed": 0}
    with ThreadPoolExecutor(config.MAX_WORKERS) as ex:
        for p, verdicts in ex.map(work, paths):
            if verdicts is None:
                stats["failed"] += 1
                p.review_flags.append("judge_failed")
                continue
            for c in p.conditions:
                v = verdicts.get(c.condition_id)
                if not v:
                    continue
                c.judge = JudgeResult(verdict=v.verdict, missing=v.missing)
                stats[v.verdict] += 1
                if v.verdict == "not_supported":
                    c.role, c.required = "uncertain", False
                    c.ambiguities.append(f"Judge: evidence does not support this claim. {v.missing}".strip())
                    if "judge_not_supported" not in p.review_flags:
                        p.review_flags.append("judge_not_supported")
    log("judge_done", **stats)
    return stats
