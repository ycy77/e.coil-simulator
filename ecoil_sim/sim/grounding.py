"""Entity grounding: resolve a free-text mention to canonical graph entry points.

This is the retrieval half of the LLM perturbation intake. Given a user mention
("recA", "DNA gyrase", "penicillin-binding protein"), it returns ranked
candidate entities so the LLM can pick the right canonical id and (for an
exogenous drug) the right endogenous target -- grounded in real entity
annotations rather than a hand-written drug->target table.

Deterministic and offline-testable: no LLM, no network. The biology ("which
drug hits which target") is the LLM's job; this only finds entities whose
name/alias/annotation matches a string.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional

from ecoil_sim.models import Entity

# Scoring tiers. Name/alias/id matches must rank ABOVE annotation mentions, so
# "recA" grounds to the recA entity, not to recB/recC whose annotations cite it.
_SCORE_ID_EXACT = 100.0
_SCORE_NAME_EXACT = 95.0
_SCORE_ALIAS_EXACT = 85.0
_SCORE_NAME_WORD = 70.0
_SCORE_ALIAS_WORD = 60.0
_SCORE_NAME_SUBSTR = 45.0
_SCORE_ANNOT_WORD = 25.0
_SCORE_ANNOT_SUBSTR = 12.0


@dataclass
class Candidate:
    entity_id: str
    name: str
    entity_type: str
    score: float
    matched_via: str
    is_exogenous: bool
    allowed_states: List[str]
    annotation_excerpt: str

    def to_dict(self) -> Dict:
        return {
            "entity_id": self.entity_id,
            "name": self.name,
            "entity_type": self.entity_type,
            "matched_via": self.matched_via,
            "is_exogenous": self.is_exogenous,
            "allowed_states": self.allowed_states,
            "annotation_excerpt": self.annotation_excerpt,
        }


def _word_present(needle: str, haystack: str) -> bool:
    if not needle or not haystack:
        return False
    return re.search(r"(?<![a-z0-9])" + re.escape(needle) + r"(?![a-z0-9])", haystack) is not None


class EntityGrounder:
    """Rank graph entities by how well they match a free-text mention.

    Searches the endogenous graph plus an optional perturbagen catalog (so a
    drug name can resolve to its own perturbagen record while its molecular
    target resolves in the endogenous graph). Exogenous candidates are tagged
    so the LLM and the human reviewer can tell them apart.
    """

    def __init__(self, entities: Iterable[Entity], perturbagens: Iterable[Entity] = ()) -> None:
        self._entities: Dict[str, Entity] = {}
        self._exogenous: set = set()
        for entity in entities:
            self._entities[entity.entity_id] = entity
        for entity in perturbagens:
            if entity.entity_id not in self._entities:
                self._entities[entity.entity_id] = entity
            self._exogenous.add(entity.entity_id)

    def candidates(self, mention: str, limit: int = 8) -> List[Candidate]:
        mention = (mention or "").strip()
        if not mention:
            return []
        m = mention.lower()
        scored: List[Candidate] = []
        for entity in self._entities.values():
            score, via = self._score(entity, m)
            if score <= 0:
                continue
            # Prefer shorter, more specific names on ties.
            score -= min(len(entity.name), 40) * 0.01
            scored.append(
                Candidate(
                    entity_id=entity.entity_id,
                    name=entity.name,
                    entity_type=entity.entity_type,
                    score=round(score, 3),
                    matched_via=via,
                    is_exogenous=entity.entity_id in self._exogenous,
                    allowed_states=list(entity.allowed_states),
                    annotation_excerpt=(entity.annotation or entity.notes or "")[:240],
                )
            )
        scored.sort(key=lambda c: (-c.score, c.entity_id))
        return scored[:limit]

    def best(self, mention: str) -> Optional[Candidate]:
        found = self.candidates(mention, limit=1)
        return found[0] if found else None

    def _score(self, entity: Entity, m: str) -> tuple:
        name = entity.name.lower()
        aliases = [a.lower() for a in entity.aliases]
        if entity.entity_id.lower() == m:
            return _SCORE_ID_EXACT, "id_exact"
        if name == m:
            return _SCORE_NAME_EXACT, "name_exact"
        if m in aliases:
            return _SCORE_ALIAS_EXACT, "alias_exact"
        if _word_present(m, name):
            return _SCORE_NAME_WORD, "name_word"
        if any(_word_present(m, a) for a in aliases):
            return _SCORE_ALIAS_WORD, "alias_word"
        if m in name:
            return _SCORE_NAME_SUBSTR, "name_substr"
        annotation = (entity.annotation or "").lower()
        notes = (entity.notes or "").lower()
        if _word_present(m, annotation) or _word_present(m, notes):
            return _SCORE_ANNOT_WORD, "annotation_word"
        if m in annotation or m in notes:
            return _SCORE_ANNOT_SUBSTR, "annotation_substr"
        return 0.0, ""
