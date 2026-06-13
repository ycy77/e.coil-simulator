from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Protocol

from ecoil_sim.config import load_yaml_like
from ecoil_sim.graph import StaticGraph
from ecoil_sim.models import Entity


@dataclass
class ParsedPerturbation:
    changes: List[Dict] = field(default_factory=list)
    unresolved: List[Dict] = field(default_factory=list)


class NaturalLanguagePerturbationParser:
    """Conservative deterministic parser for natural-language perturbations.

    It never invents drug targets. Unknown external perturbations are returned
    as unresolved candidates for a later LLM perturbation parser.
    """

    INTENTS = [
        (r"敲除|删除|knock\s*out|knockout|delete", "knockout"),
        (r"突变|mutat", "mutated"),
        (r"过表达|overexpress", "overexpressed"),
        (r"抑制|失活|inhibit|inhibited|inactive", "inhibited"),
        (r"激活|activate|activated|active", "active"),
        (r"升高|增加|加入|添加|提高|high|increase|add", "increase"),
        (r"降低|减少|移除|耗尽|low|decrease|remove|deplete", "decrease"),
    ]

    def __init__(
        self,
        graph: StaticGraph,
        search_limit: int = 12,
        knowledge_path: Path | None = None,
        name_resolver=None,
    ) -> None:
        self.graph = graph
        self.search_limit = search_limit
        # The graph's search_entities ranks by score; we must pull a
        # generous window so high-quality name matches are not crowded
        # out by id-substring hits. The actual filter happens in
        # ``_entities`` via ``_strong_name_match``.
        self._search_window = max(search_limit * 8, 200)
        self.knowledge = PerturbationKnowledgeBase(graph, knowledge_path) if knowledge_path else None
        self.name_resolver = name_resolver

    def parse(self, text: str) -> ParsedPerturbation:
        if self.knowledge:
            kb_match = self.knowledge.match(text)
            if kb_match.changes:
                return kb_match
        result = ParsedPerturbation()
        for clause in self._split_clauses(text):
            intent = self._intent(clause)
            if not intent:
                result.unresolved.append({"text": clause, "reason": "no recognized perturbation verb"})
                continue
            entities = self._entities(clause, intent)
            if not entities:
                result.unresolved.append({"text": clause, "intent": intent, "reason": "no native entity matched"})
                continue
            for entity in entities:
                change = self._change_for_entity(entity, intent, clause)
                if change:
                    result.changes.append(change)
                else:
                    result.unresolved.append({"text": clause, "entity_id": entity.entity_id, "intent": intent, "reason": "intent not compatible with entity states"})
        return result

    @staticmethod
    def _split_clauses(text: str) -> List[str]:
        parts = re.split(r"[;；。,.，\n]+|并且|然后|同时|和", text)
        return [part.strip() for part in parts if part.strip()]

    def _intent(self, clause: str) -> str:
        lowered = clause.lower()
        for pattern, intent in self.INTENTS:
            if re.search(pattern, lowered):
                return intent
        return ""

    def _entities(self, clause: str, intent: str) -> List[Entity]:
        explicit_ids = re.findall(r"\b(?:gene|protein|molecule|reaction|rna|complex)\.[A-Za-z0-9_.:-]+\b", clause)
        found: List[Entity] = []
        for entity_id in explicit_ids:
            entity = self.graph.get_entity(entity_id)
            if entity:
                found.append(entity)
        if found:
            return found

        tokens = self._candidate_tokens(clause)
        scored: Dict[str, Entity] = {}
        for token in tokens:
            hits = [
                entity for entity in self.graph.search_entities(token, limit=self._search_window)
                if self._strong_name_match(token, entity)
            ]
            native_hits = [entity for entity in hits if not self._is_ecocyc_fallback(entity)]
            for entity in native_hits or hits:
                scored[entity.entity_id] = entity
        return self._prefer_by_intent(list(scored.values()), intent)[: self.search_limit]

    @staticmethod
    def _candidate_tokens(clause: str) -> List[str]:
        cleaned = re.sub(r"敲除|删除|突变|过表达|抑制|失活|激活|升高|增加|加入|添加|提高|降低|减少|移除|耗尽", " ", clause)
        cleaned = re.sub(r"knock\s*out|knockout|delete|mutat\w*|overexpress\w*|inhibit\w*|inactive|activate\w*|increase|add|decrease|remove|deplete", " ", cleaned, flags=re.I)
        tokens = re.findall(r"[A-Za-z][A-Za-z0-9_-]{1,}|[\u4e00-\u9fff]{2,}", cleaned)
        stop = {"and", "with", "the", "gene", "protein", "molecule"}
        return [token for token in tokens if token.lower() not in stop]

    @staticmethod
    def _strong_name_match(token: str, entity: Entity) -> bool:
        token_l = token.lower()
        if token_l == entity.entity_id.lower() or token_l == entity.name.lower():
            return True
        return any(token_l == alias.lower() for alias in entity.aliases)

    @staticmethod
    def _is_ecocyc_fallback(entity: Entity) -> bool:
        return entity.source_database == "EcoCyc" and ".ecocyc." in entity.entity_id

    @staticmethod
    def _prefer_by_intent(entities: List[Entity], intent: str) -> List[Entity]:
        preference = {
            "knockout": {"gene", "rna"},
            "mutated": {"gene", "rna"},
            "overexpressed": {"gene"},
            "inhibited": {"protein", "complex"},
            "active": {"protein", "complex"},
            "increase": {"small_molecule", "gene", "protein"},
            "decrease": {"small_molecule", "gene", "protein"},
        }.get(intent, set())
        if not preference:
            return entities
        preferred = [entity for entity in entities if entity.entity_type in preference]
        return preferred or entities

    def _change_for_entity(self, entity: Entity, intent: str, clause: str) -> Dict | None:
        allowed = set(entity.allowed_states)
        state = ""
        abundance = ""
        if intent == "knockout":
            state = "knocked_out" if "knocked_out" in allowed else "degraded" if "degraded" in allowed else ""
        elif intent == "mutated":
            state = "mutated" if "mutated" in allowed else ""
        elif intent == "overexpressed":
            state = "overexpressed" if "overexpressed" in allowed else "active" if "active" in allowed else ""
        elif intent == "inhibited":
            state = "inhibited" if "inhibited" in allowed else "repressed" if "repressed" in allowed else ""
        elif intent == "active":
            state = "active" if "active" in allowed else "expressed" if "expressed" in allowed else ""
        elif intent == "increase":
            state, abundance = self._increase_state(entity)
        elif intent == "decrease":
            state, abundance = self._decrease_state(entity)
        if not state and not abundance:
            return None
        return {
            "entity_id": entity.entity_id,
            "state": state or entity.default_state,
            "abundance_label": abundance,
            "confidence": "medium",
            "source": "database",
            "raw_input": clause,
            "input_source": "natural_language",
            "perturbation_layer": "graph_search",
            "reason": f"natural language perturbation: {clause}",
        }

    @staticmethod
    def _increase_state(entity: Entity) -> tuple[str, str]:
        allowed = set(entity.allowed_states)
        if entity.entity_type == "small_molecule":
            return ("high" if "high" in allowed else entity.default_state, "high")
        if "overexpressed" in allowed:
            return "overexpressed", ""
        if "active" in allowed:
            return "active", ""
        return entity.default_state, ""

    @staticmethod
    def _decrease_state(entity: Entity) -> tuple[str, str]:
        allowed = set(entity.allowed_states)
        if entity.entity_type == "small_molecule":
            return ("low" if "low" in allowed else entity.default_state, "low")
        if "repressed" in allowed:
            return "repressed", ""
        if "inhibited" in allowed:
            return "inhibited", ""
        return entity.default_state, ""


class PerturbationKnowledgeBase:
    def __init__(self, graph: StaticGraph, path: Path | None) -> None:
        self.graph = graph
        self.entries = load_yaml_like(path) if path and path.exists() else {}

    def match(self, text: str) -> ParsedPerturbation:
        result = ParsedPerturbation()
        lowered = text.lower()
        for entry_id, entry in self.entries.items():
            keywords = entry.get("keywords", []) if isinstance(entry, dict) else []
            if not any(str(keyword).lower() in lowered for keyword in keywords):
                continue
            effect = entry.get("effect", "")
            source = entry.get("source", "database")
            confidence = entry.get("confidence", "medium")
            reason = entry.get("reason", f"matched perturbation knowledge entry {entry_id}")
            for entity_id in entry.get("targets", []):
                entity = self.graph.get_entity(entity_id)
                if not entity:
                    result.unresolved.append(
                        {
                            "text": text,
                            "entry_id": entry_id,
                            "entity_id": entity_id,
                            "reason": "knowledge target not found in graph",
                        }
                    )
                    continue
                state, abundance = self._effect_for_entity(entity, effect)
                if not state and not abundance:
                    result.unresolved.append(
                        {
                            "text": text,
                            "entry_id": entry_id,
                            "entity_id": entity_id,
                            "reason": f"effect {effect} incompatible with allowed states",
                        }
                    )
                    continue
                result.changes.append(
                    {
                        "entity_id": entity.entity_id,
                        "state": state or entity.default_state,
                        "abundance_label": abundance,
                        "confidence": confidence,
                        "source": source,
                        "raw_input": text,
                        "input_source": "natural_language",
                        "perturbation_layer": "knowledge_base",
                        "reason": reason,
                    }
                )
        return result

    @staticmethod
    def _effect_for_entity(entity: Entity, effect: str) -> tuple[str, str]:
        allowed = set(entity.allowed_states)
        if effect in allowed:
            return effect, ""
        if effect == "overexpressed" and "active" in allowed:
            return "active", ""
        if effect == "inhibited" and "repressed" in allowed:
            return "repressed", ""
        if effect == "high" and entity.entity_type == "small_molecule":
            return ("high" if "high" in allowed else entity.default_state, "high")
        if effect == "low" and entity.entity_type == "small_molecule":
            return ("low" if "low" in allowed else entity.default_state, "low")
        return "", ""


class PerturbationLLMClient(Protocol):
    async def complete_json(self, messages: List[Dict[str, str]]) -> Dict[str, Any]:
        ...


class LLMPerturbationParser:
    """LLM-assisted perturbation parser interface.

    It is not used by default while GPUs are unavailable. The deterministic
    parser above remains the offline fallback. This class defines the stable
    interface for later target/effect extraction with Qwen.
    """

    def __init__(self, graph: StaticGraph, llm_client: PerturbationLLMClient, candidate_limit: int = 30) -> None:
        self.graph = graph
        self.llm_client = llm_client
        self.candidate_limit = candidate_limit

    async def parse(self, text: str) -> ParsedPerturbation:
        candidates = self._candidate_entities(text)
        if not candidates:
            return ParsedPerturbation(unresolved=[{"text": text, "reason": "no entity candidates found"}])
        messages = [
            {
                "role": "system",
                "content": (
                    "Extract native E. coli perturbation targets. Do not invent drug targets. "
                    "Return JSON with changes: [{entity_id,state,abundance_label,confidence,reason}] "
                    "and unresolved: []. Confidence must be high, medium, or low. "
                    "These changes are temporary llm_inference results for this simulation only."
                ),
            },
            {
                "role": "user",
                "content": json.dumps({
                    "text": text,
                    "candidates": [
                        {
                            "entity_id": entity.entity_id,
                            "entity_type": entity.entity_type,
                            "name": entity.name,
                            "aliases": entity.aliases[:8],
                            "allowed_states": entity.allowed_states,
                            "annotation": entity.annotation[:800],
                        }
                        for entity in candidates
                    ],
                }, ensure_ascii=False),
            },
        ]
        payload = await self.llm_client.complete_json(messages)
        return self._normalize_payload(text, payload)

    def _candidate_entities(self, text: str) -> List[Entity]:
        tokens = NaturalLanguagePerturbationParser._candidate_tokens(text)
        found: Dict[str, Entity] = {}
        for token in tokens:
            for entity in self.graph.search_entities(token, limit=self.candidate_limit):
                found[entity.entity_id] = entity
        return list(found.values())[: self.candidate_limit]

    @staticmethod
    def _normalize_payload(text: str, payload: Dict[str, Any]) -> ParsedPerturbation:
        result = ParsedPerturbation()
        for item in payload.get("changes", []) if isinstance(payload, dict) else []:
            if not isinstance(item, dict) or not item.get("entity_id"):
                continue
            confidence = item.get("confidence", "medium")
            if confidence not in {"high", "medium", "low"}:
                confidence = "medium"
            result.changes.append(
                {
                    "entity_id": item["entity_id"],
                    "state": item.get("state", ""),
                    "abundance_label": item.get("abundance_label", ""),
                    "confidence": confidence,
                    "source": "llm_inference",
                    "raw_input": text,
                    "input_source": "natural_language",
                    "perturbation_layer": "llm_inference",
                    "reason": item.get("reason", f"LLM perturbation parser: {text}"),
                }
            )
        unresolved = payload.get("unresolved", []) if isinstance(payload, dict) else []
        for item in unresolved:
            result.unresolved.append(item if isinstance(item, dict) else {"text": str(item)})
        if not result.changes and not result.unresolved:
            result.unresolved.append({"text": text, "reason": "LLM parser returned no changes"})
        return result
