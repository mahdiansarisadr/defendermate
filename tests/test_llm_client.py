"""TDD 13.6: cache hits need no network, schema failure -> one repair -> ExtractionFailed, prompt version keys."""

import pytest
from pydantic import BaseModel

from urx.llm.client import CacheMiss, ExtractionFailed, LLMClient, strict_schema


class Out(BaseModel):
    label: str
    n: int


class FakeProvider:
    name = "anthropic"

    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = 0

    def complete(self, model, system, user, schema, max_tokens):
        self.calls += 1
        return self.responses.pop(0), {"input_tokens": 10, "output_tokens": 5}


class Exploding:
    name = "anthropic"

    def complete(self, *a, **k):
        raise AssertionError("network must not be used on cache hit")


def test_cache_hit_uses_no_network(tmp_path):
    c = LLMClient(cache_dir=tmp_path, provider_impl=FakeProvider([{"label": "risk", "n": 1}]))
    assert c.complete("triage.v1", {"items_jsonl": "x"}, Out).label == "risk"
    c2 = LLMClient(cache_dir=tmp_path, provider_impl=Exploding())
    assert c2.complete("triage.v1", {"items_jsonl": "x"}, Out).n == 1


def test_offline_cache_miss_raises(tmp_path):
    with pytest.raises(CacheMiss):
        LLMClient(cache_dir=tmp_path, offline=True, provider_impl=Exploding()).complete("triage.v1", {"items_jsonl": "y"}, Out)


def test_schema_failure_repairs_once_then_fails(tmp_path):
    fp = FakeProvider([{"label": "risk"}, {"label": "risk", "n": 2}])
    assert LLMClient(cache_dir=tmp_path, provider_impl=fp).complete("triage.v1", {"items_jsonl": "a"}, Out).n == 2
    assert fp.calls == 2
    fp2 = FakeProvider([{"label": "risk"}, {"nope": 1}])
    with pytest.raises(ExtractionFailed):
        LLMClient(cache_dir=tmp_path, provider_impl=fp2).complete("triage.v1", {"items_jsonl": "b"}, Out)
    assert fp2.calls == 2


def test_prompt_version_changes_cache_key(tmp_path):
    c = LLMClient(cache_dir=tmp_path, provider_impl=Exploding())
    s = strict_schema(Out)
    assert c.cache_key("extract.v1", "m", "sys", "u", s) != c.cache_key("extract.v2", "m", "sys", "u", s)


def test_strict_schema_keeps_fields_named_description():
    class P(BaseModel):
        description: str
        title: str
    s = strict_schema(P)
    assert s["required"] == ["description", "title"] and s["additionalProperties"] is False
