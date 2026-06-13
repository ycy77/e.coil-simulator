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
        # Robust to imperfect mentions: score the full phrase, AND each token
        # (for multi-word spans like "knock out recA" or "add ciprofloxacin").
        # Token matches are only accepted at the name/alias tier, so a verb or
        # stopword ("add", "knock") cannot surface via a weak annotation hit.
        m = mention.lower()
        # (query, is_full_phrase, token_only_strong)
        queries = [(m, True, False)]
        tokens = [t for t in re.split(r"\s+", m) if len(t) > 2]
        if len(tokens) > 1:
            queries.extend((t, False, True) for t in tokens)

        best: Dict[str, tuple] = {}  # entity_id -> (is_full, adjusted_score, via)
        for entity in self._entities.values():
            for query, is_full, token_only_strong in queries:
                score, via = self._score(entity, query)
                if score <= 0:
                    continue
                if token_only_strong and score < _SCORE_NAME_WORD:
                    continue
                adjusted = score - min(len(entity.name), 40) * 0.01
                key = (is_full, adjusted)
                if entity.entity_id not in best or key > best[entity.entity_id][:2]:
                    best[entity.entity_id] = (is_full, adjusted, via)

        scored = [
            Candidate(
                entity_id=eid,
                name=self._entities[eid].name,
                entity_type=self._entities[eid].entity_type,
                score=round(adj, 3),
                matched_via=via,
                is_exogenous=eid in self._exogenous,
                allowed_states=list(self._entities[eid].allowed_states),
                annotation_excerpt=(self._entities[eid].annotation or self._entities[eid].notes or "")[:240],
            )
            for eid, (is_full, adj, via) in best.items()
        ]
        # Full-phrase matches rank above token-only matches: a hit on the whole
        # mention ("DNA gyrase" -> gyrA via annotation) is more specific than a
        # generic token ("dna" -> the DNA metabolite).
        scored.sort(key=lambda c: (0 if best[c.entity_id][0] else 1, -c.score, c.entity_id))
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
