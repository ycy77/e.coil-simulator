"""Bi-directional mapping between internal entity IDs and natural names.

The simulator keeps one canonical :class:`Entity` per real-world molecule. The
LLM never sees opaque IDs like ``protein.P03023``. Instead it sees the public
name (``LacI repressor``), the KEGG common name, UniProt recommended name,
or any of the curated aliases.

:class:`NameResolver` provides:

* :meth:`to_public` — entity_id -> natural name plus a stable display hint
  such as ``"LacI repressor (protein.P03023)"`` so the LLM can echo the ID
  back when needed for downstream validation.
* :meth:`from_public` — public name or id-hint back to the canonical
  entity_id, with multi-level fuzzy matching.
* :meth:`to_public_batch` / :meth:`from_public_batch` — batch helpers used by
  prompt building and action interpretation.

Resolution order in :meth:`from_public` (highest to lowest confidence):

1. Embedded id hint such as ``(protein.P03023)``
2. Exact entity_id
3. Exact lowercase name
4. Exact lowercase alias
5. Exact lowercase external id
6. Whole-word substring match (with word boundary)
7. Token-level substring match (lowest confidence)
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

from ecoil_sim.models import Entity


_TOKEN_SPLIT = re.compile(r"[^A-Za-z0-9]+")
_GENERIC_DISPLAY_TOKENS = {
    "gene",
    "protein",
    "proteincomplex",
    "complex",
    "smallmolecule",
    "molecule",
    "rna",
    "reaction",
}


@dataclass
class ResolvedEntity:
    entity_id: str
    name: str
    confidence: float
    matched_via: str


class NameResolver:
    def __init__(self, entities: Iterable[Entity]) -> None:
        self._by_id: Dict[str, Entity] = {}
        self._by_exact_name: Dict[str, str] = {}
        self._by_alias: Dict[str, str] = {}
        self._by_external: Dict[str, str] = {}
        self._by_name_token: Dict[str, str] = {}
        for entity in entities:
            self._by_id[entity.entity_id] = entity
            self._register_entity(entity)

    def has_entity(self, entity_id: str) -> bool:
        return entity_id in self._by_id

    def to_public(self, entity_id: str) -> str:
        """Render the entity in the form ``"LacI repressor (protein.P03023)"``."""
        entity = self._by_id.get(entity_id)
        if not entity:
            return f"unknown entity ({entity_id})"
        display = self._display_name(entity)
        if display == entity.entity_id:
            return entity.entity_id
        return f"{display} ({entity.entity_id})"

    def to_public_short(self, entity_id: str) -> str:
        entity = self._by_id.get(entity_id)
        if not entity:
            return entity_id
        return self._display_name(entity)

    def to_public_batch(self, entity_ids: Sequence[str]) -> Dict[str, str]:
        return {entity_id: self.to_public(entity_id) for entity_id in entity_ids}

    def from_public(self, text: str) -> Optional[ResolvedEntity]:
        """Resolve a free-form LLM reference back to the canonical entity."""
        if not text:
            return None
        cleaned = text.strip()
        if not cleaned:
            return None

        extracted_id = self._extract_id_hint(cleaned)
        if extracted_id and extracted_id in self._by_id:
            entity = self._by_id[extracted_id]
            return ResolvedEntity(entity.entity_id, entity.name, 1.0, "id_hint")

        lowered = cleaned.lower()
        if lowered in self._by_id:
            entity = self._by_id[lowered]
            return ResolvedEntity(entity.entity_id, entity.name, 1.0, "id_exact")

        candidates: List[Tuple[float, str, str]] = []

        def add_candidate(score: float, entity_id: str, matched_via: str) -> None:
            if not entity_id or entity_id not in self._by_id:
                return
            length_penalty = -0.001 * len(self._by_id[entity_id].name)
            candidates.append((score + length_penalty, entity_id, matched_via))

        if lowered in self._by_exact_name:
            add_candidate(0.98, self._by_exact_name[lowered], "name")
        if lowered in self._by_alias:
            add_candidate(0.95, self._by_alias[lowered], "alias")
        if lowered in self._by_external:
            add_candidate(0.9, self._by_external[lowered], "external_id")

        for entity in self._by_id.values():
            for alias in entity.aliases:
                if alias and alias.lower() == lowered:
                    add_candidate(0.95, entity.entity_id, "alias_scan")
                    break
            for alias in entity.aliases:
                if alias and self._word_boundary_contains(lowered, alias.lower()):
                    add_candidate(0.6, entity.entity_id, "substring_alias")
                    break
            else:
                for token in self._tokenize(entity.name):
                    if len(token) >= 4 and self._word_boundary_contains(lowered, token):
                        add_candidate(0.5, entity.entity_id, "substring_token")
                        break

        for candidate_key in self._iter_candidate_keys(lowered):
            if candidate_key in self._by_exact_name:
                add_candidate(0.92, self._by_exact_name[candidate_key], "name_token")
            if candidate_key in self._by_alias:
                add_candidate(0.88, self._by_alias[candidate_key], "alias_token")
            if candidate_key in self._by_name_token:
                add_candidate(0.7, self._by_name_token[candidate_key], "name_token_substr")

        if not candidates:
            return None
        candidates.sort(key=lambda item: (-item[0], item[1]))
        score, entity_id, matched_via = candidates[0]
        return ResolvedEntity(entity_id, self._by_id[entity_id].name, round(score, 3), matched_via)

    def from_public_batch(self, texts: Sequence[str]) -> List[Optional[ResolvedEntity]]:
        return [self.from_public(text) for text in texts]

    def fuzzy_candidates(self, text: str, limit: int = 5) -> List[ResolvedEntity]:
        if not text:
            return []
        needle = text.lower()
        scored: List[Tuple[float, Entity, str]] = []
        for entity in self._by_id.values():
            haystack = " ".join(
                [entity.entity_id.lower(), entity.name.lower(), " ".join(entity.aliases).lower()]
            )
            if needle in haystack:
                score = 5.0 if needle == entity.name.lower() else 2.0
                score += 1.0 if needle in entity.entity_id.lower() else 0.0
                scored.append((score, entity, "substring"))
        scored.sort(key=lambda item: (-item[0], item[1].entity_id))
        return [
            ResolvedEntity(entity.entity_id, entity.name, min(1.0, score / 5.0), matched_via)
            for score, entity, matched_via in scored[:limit]
        ]

    def _register_entity(self, entity: Entity) -> None:
        if entity.name:
            self._by_exact_name[entity.name.lower()] = entity.entity_id
            for token in self._tokenize(entity.name):
                if len(token) >= 4 and token not in self._by_name_token:
                    self._by_name_token[token] = entity.entity_id
        for alias in entity.aliases:
            if not alias:
                continue
            key = alias.lower()
            self._by_alias[key] = entity.entity_id
        for ext in self._split_external(entity.external_ids):
            self._by_external[ext.lower()] = entity.entity_id

    def _iter_candidate_keys(self, text: str) -> Iterable[str]:
        lowered = text.lower().strip()
        yield from self._tokenize(lowered)

    def _tokenize(self, text: str) -> List[str]:
        if not text:
            return []
        return [token for token in _TOKEN_SPLIT.split(text.lower()) if token]

    def _split_external(self, external: str) -> List[str]:
        if not external:
            return []
        return [item for item in re.split(r"[|,;\s]+", external) if item]

    def _extract_id_hint(self, text: str) -> Optional[str]:
        match = re.search(r"\(([a-zA-Z]+(?:\.[A-Za-z0-9_.:-]+))\)", text)
        if match:
            return match.group(1)
        match = re.search(r"\b([a-zA-Z]+\.[A-Za-z0-9_.:-]{2,})\b", text)
        if match:
            return match.group(1)
        return None

    def _display_name(self, entity: Entity) -> str:
        if entity.name and entity.name.lower() not in _GENERIC_DISPLAY_TOKENS:
            return entity.name
        if entity.aliases:
            for alias in entity.aliases:
                if alias and alias.lower() not in _GENERIC_DISPLAY_TOKENS:
                    return alias
        if entity.annotation:
            head = entity.annotation.split(".")[0].strip()
            if head and head.lower() not in _GENERIC_DISPLAY_TOKENS:
                return head[:80]
        return entity.entity_id

    @staticmethod
    def _word_boundary_contains(haystack: str, needle: str) -> bool:
        if not needle:
            return False
        if needle not in haystack:
            return False
        if len(needle) == len(haystack):
            return True
        idx = haystack.find(needle)
        if idx > 0 and haystack[idx - 1].isalnum():
            return False
        end = idx + len(needle)
        if end < len(haystack) and haystack[end].isalnum():
            return False
        return True
