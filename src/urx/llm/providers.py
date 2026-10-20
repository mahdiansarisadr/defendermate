"""LLM providers. Each returns (parsed_json, usage). Structured output via JSON schema."""

from __future__ import annotations

import json
from typing import Any, Protocol


class Provider(Protocol):
    name: str

    def complete(self, model: str, system: str, user: str, schema: dict, max_tokens: int) -> tuple[Any, dict]: ...


def _parse_json(text: str) -> Any:
    text = text.strip()
    if text.startswith("```"):
        text = text.strip("`")
        text = text[text.find("\n") + 1:]
    return json.loads(text)


class AnthropicProvider:
    name = "anthropic"

    def __init__(self) -> None:
        import anthropic

        self.client = anthropic.Anthropic(max_retries=5, timeout=180)

    def complete(self, model: str, system: str, user: str, schema: dict, max_tokens: int) -> tuple[Any, dict]:
        resp = self.client.messages.create(
            model=model, max_tokens=max_tokens, system=system,
            messages=[{"role": "user", "content": user}],
            output_config={"format": {"type": "json_schema", "schema": schema}},
        )
        text = "".join(b.text for b in resp.content if b.type == "text")
        usage = {"input_tokens": resp.usage.input_tokens, "output_tokens": resp.usage.output_tokens,
                 "stop_reason": resp.stop_reason}
        return _parse_json(text), usage


class OpenAIProvider:
    name = "openai"

    def __init__(self) -> None:
        import openai

        self.client = openai.OpenAI(max_retries=5, timeout=180)

    def complete(self, model: str, system: str, user: str, schema: dict, max_tokens: int) -> tuple[Any, dict]:
        resp = self.client.chat.completions.create(
            model=model, max_completion_tokens=max_tokens,
            messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
            response_format={"type": "json_schema", "json_schema": {"name": "emit", "schema": schema, "strict": True}},
        )
        usage = {"input_tokens": resp.usage.prompt_tokens, "output_tokens": resp.usage.completion_tokens,
                 "stop_reason": resp.choices[0].finish_reason}
        return _parse_json(resp.choices[0].message.content or ""), usage


def get_provider(name: str) -> Provider:
    if name == "anthropic":
        return AnthropicProvider()
    if name == "openai":
        return OpenAIProvider()
    raise ValueError(f"unknown provider {name!r}")
