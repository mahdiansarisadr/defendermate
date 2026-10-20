"""LLM client: versioned prompts, content-addressed cache, schema validation + one repair (TDD C10)."""

from __future__ import annotations

import hashlib
import json
import re
import threading
from pathlib import Path
from typing import Any, TypeVar

from pydantic import BaseModel, ValidationError

from .. import config
from .providers import Provider, get_provider

T = TypeVar("T", bound=BaseModel)


class CacheMiss(RuntimeError):
    pass


class ExtractionFailed(RuntimeError):
    pass


def load_prompt(prompt_id: str) -> tuple[str, str]:
    """Prompt files: system text, a line `===USER===`, then the user template."""
    text = (config.PROMPTS_DIR / f"{prompt_id}.md").read_text()
    system, _, user = text.partition("\n===USER===\n")
    return system.strip(), user.strip()


def render_prompt(template: str, variables: dict[str, Any]) -> str:
    def sub(m: re.Match) -> str:
        k = m.group(1)
        if k not in variables:
            return m.group(0)
        v = variables[k]
        return v if isinstance(v, str) else json.dumps(v, ensure_ascii=False, indent=1)

    return re.sub(r"\{(\w+)\}", sub, template)


def strict_schema(model: type[BaseModel]) -> dict:
    """Pydantic JSON schema -> provider structured-output schema (all props required, no extras)."""
    schema = model.model_json_schema()
    defs = schema.pop("$defs", {})

    def fix(node: Any) -> Any:
        if isinstance(node, dict):
            if "$ref" in node:
                return fix(defs[node["$ref"].split("/")[-1]])
            node = {k: (({pk: fix(pv) for pk, pv in v.items()}) if k == "properties" else fix(v))
                    for k, v in node.items() if k not in ("title", "default", "description")}
            if node.get("type") == "object" and "properties" in node:
                node["required"] = list(node["properties"].keys())
                node["additionalProperties"] = False
            return node
        if isinstance(node, list):
            return [fix(x) for x in node]
        return node

    return fix(schema)


class Usage:
    def __init__(self) -> None:
        self.lock = threading.Lock()
        self.by_stage: dict[str, dict[str, float]] = {}

    def add(self, stage: str, model: str, usage: dict, cached: bool) -> None:
        tin, tout = usage.get("input_tokens", 0), usage.get("output_tokens", 0)
        usd = config.price_usd(model, tin, tout)
        with self.lock:
            s = self.by_stage.setdefault(stage, {"calls": 0, "cache_hits": 0, "input_tokens": 0,
                                                 "output_tokens": 0, "usd_estimate": 0.0, "usd_full": 0.0,
                                                 "model": model})
            s["calls"] += 1
            s["cache_hits"] += int(cached)
            s["input_tokens"] += tin
            s["output_tokens"] += tout
            s["usd_full"] += usd
            if not cached:
                s["usd_estimate"] += usd


class LLMClient:
    def __init__(self, provider: str | None = None, offline: bool = False, cache_dir: Path | None = None,
                 provider_impl: Provider | None = None, models: dict[str, str] | None = None) -> None:
        self.provider_name = provider or config.PROVIDER
        self.offline = offline
        self.cache_dir = cache_dir or config.LLM_CACHE_DIR
        self._provider = provider_impl
        self.models = models
        self.usage = Usage()

    @property
    def provider(self) -> Provider:
        if self._provider is None:
            self._provider = get_provider(self.provider_name)
        return self._provider

    def model_for(self, tier: str) -> str:
        return (self.models or config.MODELS[self.provider_name])[tier]

    def model_map(self) -> dict[str, str]:
        return {t: self.model_for(t) for t in ("cheap", "strong")}

    def cache_key(self, prompt_id: str, model: str, system: str, user: str, schema: dict) -> str:
        h = hashlib.sha256()
        for part in (self.provider_name, model, prompt_id, system, user, json.dumps(schema, sort_keys=True)):
            h.update(part.encode())
            h.update(b"\x00")
        return h.hexdigest()

    def _call(self, prompt_id: str, model: str, system: str, user: str, schema: dict, max_tokens: int,
              stage: str) -> Any:
        key = self.cache_key(prompt_id, model, system, user, schema)
        path = self.cache_dir / prompt_id / f"{key[:2]}" / f"{key}.json"
        if path.exists():
            rec = json.loads(path.read_text())
            self.usage.add(stage, model, rec.get("usage", {}), cached=True)
            return rec["response"]
        if self.offline:
            raise CacheMiss(f"{prompt_id}: no cached response (key {key[:12]}); rerun without --offline")
        data, usage = self.provider.complete(model, system, user, schema, max_tokens)
        self.usage.add(stage, model, usage, cached=False)
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".tmp")
        tmp.write_text(json.dumps({"prompt_id": prompt_id, "provider": self.provider_name, "model": model,
                                   "user": user, "response": data, "usage": usage}, ensure_ascii=False, indent=1))
        tmp.replace(path)
        return data

    def complete(self, prompt_id: str, variables: dict[str, Any], schema: type[T], model_tier: str = "cheap",
                 max_tokens: int = 8000, stage: str | None = None, repair_note: str = "") -> T:
        system, template = load_prompt(prompt_id)
        user = render_prompt(template, variables) + (f"\n\n{repair_note}" if repair_note else "")
        model = self.model_for(model_tier)
        js = strict_schema(schema)
        stage = stage or prompt_id.split(".")[0]
        data = self._call(prompt_id, model, system, user, js, max_tokens, stage)
        try:
            return schema.model_validate(data)
        except ValidationError as e:
            fix = (f"{user}\n\nYour previous answer failed schema validation:\n{str(e)[:1500]}\n"
                   "Return a corrected answer.")
            data = self._call(prompt_id, model, system, fix, js, max_tokens, stage)
            try:
                return schema.model_validate(data)
            except ValidationError as e2:
                raise ExtractionFailed(f"{prompt_id}: schema validation failed after repair: {e2}") from e2
