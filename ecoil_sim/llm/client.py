"""LLM client abstractions.

Three execution modes are supported:

* :class:`NullLLMClient` — does nothing, used for pure topology tests.
* :class:`RuleBasedMockLLM` — deterministic offline LLM that emits valid
  actions from the candidate rules in the prompt. Used for CI and
  debugging.
* :class:`AsyncVLLMClient` — production client against a vLLM OpenAI
  compatible endpoint.

All three expose the same ``batch_chat`` interface. The async client
runs prompts concurrently behind an ``asyncio.Semaphore`` and routes
model output through :func:`parse_llm_output` so a single bad agent can
never crash a round.
"""

from __future__ import annotations

import asyncio
import json
import re
from typing import Any, Dict, Iterable, List, Optional

from pathlib import Path

from ecoil_sim.llm.response_parser import parse_llm_output
from ecoil_sim.validation import ActionValidator


def load_guided_json(model_config: Dict[str, Any], project_root: Path) -> Optional[Dict[str, Any]]:
    """Return the JSON schema to constrain decoding, or None if disabled.

    Reads the ``structured_output`` block of the model config
    (configs/model.qwen35_9b.yaml). When ``require_json`` is set, loads
    ``schema_file`` (the action wrapper schema) so callers can pass it as
    ``guided_json`` to :class:`AsyncVLLMClient`.
    """
    structured = model_config.get("structured_output", {}) or {}
    if not structured.get("require_json"):
        return None
    schema_rel = structured.get("schema_file", "schemas/action.schema.json")
    schema_path = Path(project_root) / schema_rel
    if not schema_path.exists():
        return None
    return json.loads(schema_path.read_text(encoding="utf-8"))


class NullLLMClient:
    async def batch_chat(self, batches: Iterable[List[Dict[str, str]]]) -> List[Dict[str, Any]]:
        return [{"actions": []} for _ in batches]


class RuleBasedMockLLM:
    """Offline deterministic client for testing iterative propagation.

    It reads the prompt payload and emits schema-compatible actions using only
    candidate rules already retrieved from the registry.
    """

    async def batch_chat(self, batches: Iterable[List[Dict[str, str]]]) -> List[Dict[str, Any]]:
        validator = ActionValidator()
        return [validator.validate(self._respond(messages)) for messages in batches]

    def _respond(self, messages: List[Dict[str, str]]) -> Dict[str, Any]:
        payload = self._payload(messages)
        if not payload:
            return {"actions": []}
        you_block = payload.get("you", {}) or {}
        current_id = you_block.get("public_id_hint", "")
        current_type = you_block.get("entity_type", "")
        changed_neighbors = payload.get("changed_neighbors", {})
        rules = payload.get("candidate_rules", [])
        edges = payload.get("retrieved_edges", [])
        actions: List[Dict[str, Any]] = []
        neighbor_index = self._build_neighbor_index(changed_neighbors)

        # For gene agents, the mock may emit BOTH a state action (from
        # ``represses``) and an efficiency action (from ``activates``)
        # in a single round. We collect them separately so the
        # interpreter can compose them.
        for edge in edges:
            relation = edge.get("relation_type", "")
            source = edge.get("source_id", "") or edge.get("source_entity_id", "")
            target = edge.get("target_id", "") or edge.get("target_entity_id", "")
            neighbor_id = source if target == current_id else target if source == current_id else ""
            if not neighbor_id or neighbor_id not in neighbor_index:
                continue
            rule_id = self._matching_rule_id(rules, source, target, relation)
            if not rule_id:
                continue
            neighbor_state = neighbor_index[neighbor_id].get("state", "")
            action = self._action_for_relation(
                current_id=current_id,
                current_type=current_type,
                relation=relation,
                is_current_target=(target == current_id),
                neighbor_state=neighbor_state,
                rule_id=rule_id,
            )
            if not action:
                continue
            if current_type == "gene":
                # For gene agents we may stack multiple actions across
                # the two regulation layers (state + efficiency). The
                # interpreter composes them, so dedupe is by rule_id.
                if not any(a.get("rule_id") == action.get("rule_id") for a in actions):
                    actions.append(action)
                continue
            # Non-gene entities: first valid action wins.
            actions.append(action)
            break
        return {"actions": actions}

    @staticmethod
    def _build_neighbor_index(changed_neighbors: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
        """Resolve the prompt's public-name keyed neighbour map to entity_id keys.

        The prompt builder keys ``changed_neighbors`` by public display
        name (e.g. ``"LacI repressor (protein.P03023)"``) for LLM
        readability, but the mock has to make decisions on canonical
        entity ids. The public map also carries the entity_id inside
        each value, which we use as the lookup key.
        """
        index: Dict[str, Dict[str, Any]] = {}
        for _public_name, info in changed_neighbors.items():
            if not isinstance(info, dict):
                continue
            entity_id = info.get("entity_id")
            if entity_id:
                index[entity_id] = info
        return index

    @staticmethod
    def _payload(messages: List[Dict[str, str]]) -> Dict[str, Any]:
        if not messages:
            return {}
        try:
            return json.loads(messages[-1].get("content", "{}"))
        except json.JSONDecodeError:
            return {}

    @staticmethod
    def _matching_rule_id(rules: List[Dict[str, Any]], source: str, target: str, relation: str) -> str:
        for rule in rules:
            # New prompt schema exposes source_id / target_id directly on the rule.
            if (
                rule.get("source_id") == source
                and rule.get("target_id") == target
                and rule.get("relation_type") == relation
            ):
                return rule.get("rule_id", "")
            # Older schema stored them under a nested ``participants`` key.
            participants = rule.get("participants", {})
            if (
                participants.get("source_id") == source
                and participants.get("target_id") == target
                and participants.get("relation_type") == relation
            ):
                return rule.get("rule_id", "")
        return ""

    @staticmethod
    def _action_for_relation(
        current_id: str,
        current_type: str,
        relation: str,
        is_current_target: bool,
        neighbor_state: str,
        rule_id: str,
    ) -> Dict[str, Any] | None:
        inactive = neighbor_state in {"inhibited", "degraded", "sequestered", "knocked_out", "mutated", "repressed"}
        active = neighbor_state in {"active", "expressed", "overexpressed", "high", "medium"}
        if relation == "represses" and is_current_target:
            return {
                "action_type": "change_activity",
                "rule_id": rule_id,
                "targets": [current_id],
                "direction": "up" if inactive else "down",
                "strength": 1,
                "reason": "mock: repressor state changed through a candidate represses rule",
            }
        if relation == "activates" and is_current_target:
            # For genes, ``activates`` drives the efficiency axis (Layer 2
            # of the dual-layer regulation model). For other entity types
            # it remains a functional activity change.
            if current_type == "gene":
                return {
                    "action_type": "change_efficiency",
                    "rule_id": rule_id,
                    "targets": [current_id],
                    "direction": "up" if active else "down",
                    "strength": 1,
                    "reason": "mock: activator state changed through a candidate activates rule on the efficiency axis",
                }
            return {
                "action_type": "change_activity",
                "rule_id": rule_id,
                "targets": [current_id],
                "direction": "down" if inactive else "up",
                "strength": 1,
                "reason": "mock: activator state changed through a candidate activates rule",
            }
        if relation == "encodes" and is_current_target:
            # encodes affects protein / RNA abundance, not activity. This
            # matches the fallback policy and the new dual-axis model.
            return {
                "action_type": "change_abundance",
                "rule_id": rule_id,
                "targets": [current_id],
                "direction": "down" if inactive else "up",
                "strength": 1,
                "reason": "mock: coding gene state changed through a candidate encodes rule",
            }
        if relation in {"is_product_of", "produce"} and current_type == "small_molecule":
            return {
                "action_type": "produce",
                "rule_id": rule_id,
                "targets": [current_id],
                "direction": "up" if active else "down",
                "strength": 1,
                "reason": "mock: producer state changed through a candidate production rule",
            }
        if relation in {"is_substrate_of", "consume"} and current_type == "small_molecule":
            return {
                "action_type": "consume",
                "rule_id": rule_id,
                "targets": [current_id],
                "direction": "down" if active else "up",
                "strength": 1,
                "reason": "mock: consumer state changed through a candidate substrate rule",
            }
        return None


class AsyncVLLMClient:
    def __init__(
        self,
        base_url: str,
        model: str,
        api_key: str = "EMPTY",
        max_concurrency: int = 32,
        timeout_seconds: float = 120.0,
        max_retries: int = 2,
        temperature: float = 0.2,
        top_p: float = 0.8,
        max_tokens: int = 256,
        validator: ActionValidator | None = None,
        raw_content_log_limit: int = 4000,
        thinking_kw: str = "think",
        guided_json: Optional[Dict[str, Any]] = None,
        guided_decoding_backend: str = "",
        enable_thinking: bool = False,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.api_key = api_key
        self.max_concurrency = max_concurrency
        self.timeout_seconds = timeout_seconds
        self.max_retries = max_retries
        self.temperature = temperature
        self.top_p = top_p
        self.max_tokens = max_tokens
        self.validator = validator or ActionValidator()
        self.raw_content_log_limit = raw_content_log_limit
        self.thinking_kw = thinking_kw
        # When set, the request constrains generation to this JSON schema so the
        # model cannot emit malformed/ambiguous actions (vLLM `guided_json`).
        self.guided_json = guided_json
        self.guided_decoding_backend = guided_decoding_backend
        self.enable_thinking = enable_thinking

    def _build_payload(self, messages: List[Dict[str, str]]) -> Dict[str, Any]:
        """Build the chat-completions request body.

        Schema-constrained decoding uses OpenAI-style ``response_format`` with a
        ``json_schema``. On the deployed vLLM this is what actually works AND it
        suppresses the model's ``<think>`` block — verified directly: top-level
        ``guided_json`` was silently IGNORED (output kept a <think> block and did
        not match the schema), which wasted the token budget on reasoning and
        truncated the action. ``response_format`` returns pure schema-valid JSON.
        """
        payload: Dict[str, Any] = {
            "model": self.model,
            "messages": messages,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
            "top_p": self.top_p,
            "chat_template_kwargs": {"enable_thinking": self.enable_thinking},
        }
        if self.guided_json:
            payload["response_format"] = {
                "type": "json_schema",
                "json_schema": {"name": "ecoil_action", "schema": self.guided_json},
            }
        return payload

    async def batch_chat(self, batches: Iterable[List[Dict[str, str]]]) -> List[Dict[str, Any]]:
        prompts = list(batches)
        semaphore = asyncio.Semaphore(self.max_concurrency)
        async with self._client() as client:
            tasks = [self._one(client, semaphore, messages) for messages in prompts]
            return await asyncio.gather(*tasks)

    def _client(self):
        import httpx

        return httpx.AsyncClient(timeout=self.timeout_seconds)

    async def _one(self, client, semaphore: asyncio.Semaphore, messages: List[Dict[str, str]]) -> Dict[str, Any]:
        async with semaphore:
            payload = self._build_payload(messages)
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            }
            last_error: Optional[Exception] = None
            for attempt in range(self.max_retries + 1):
                try:
                    response = await client.post(f"{self.base_url}/chat/completions", json=payload, headers=headers)
                    response.raise_for_status()
                    content = response.json().get("choices", [{}])[0].get("message", {}).get("content") or ""
                    parsed, diagnostics = parse_llm_output(content)
                    validated = self.validator.validate(parsed)
                    if self.raw_content_log_limit > 0:
                        validated["_raw_content"] = content[: self.raw_content_log_limit]
                    validated["_parsed_payload"] = parsed
                    validated["_parse_diagnostics"] = diagnostics.to_dict()
                    validated["_attempt"] = attempt
                    return validated
                except Exception as exc:  # keep one bad agent from killing the round
                    last_error = exc
                    await asyncio.sleep(0.2 * (attempt + 1))
            return {
                "actions": [],
                "_error": str(last_error) if last_error else "unknown",
                "_parse_diagnostics": {"final_method": "client_exception"},
            }
