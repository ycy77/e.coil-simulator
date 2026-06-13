"""Construct per-agent LLM prompts.

The LLM never sees internal entity IDs as opaque strings. Every entity is
presented as ``"LacI repressor (protein.P03023)"`` so the LLM can:

* reason in natural language,
* echo a stable hint back when it needs to reference an entity by id.

Rules are surfaced as ``R#1``, ``R#2``, ... and the canonical rule_id is
hidden. The mapping from hint to canonical rule_id is returned in
:attr:`PromptBuildResult.rule_hint_map` so the validator can translate
back without the LLM ever seeing the long technical rule identifier.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, Dict, List

from ecoil_sim.graph import StaticGraph
from ecoil_sim.llm import NameResolver
from ecoil_sim.models import Rule
from ecoil_sim.retrieval import RetrievedContext
from ecoil_sim.state import TemporalState

# ``EnrichedService`` lives under :mod:`ecoil_sim.sim`, which in turn
# imports the prompt builder. We keep the import local so this
# module does not become a circular-import entry point.
if TYPE_CHECKING:
    from ecoil_sim.sim.enriched_service import EnrichedService


def _activates_action_type(entity_type: str) -> str:
    """For an ``activates`` edge, pick the right action axis.

    Genes get ``change_efficiency`` (transcription efficiency) while
    other entity types get ``change_activity`` (functional state).
    This is the second-layer regulation split the LLM needs to reason
    about a gene's dual axes: ``state`` (permissibility) versus
    ``efficiency`` (rate).
    """
    if entity_type == "gene":
        return "change_efficiency"
    return "change_activity"


@dataclass
class PromptBuildResult:
    messages: List[Dict[str, str]]
    rule_hint_map: Dict[str, str] = field(default_factory=dict)
    public_name_map: Dict[str, str] = field(default_factory=dict)


class PromptBuilder:
    def __init__(
        self,
        system_prompt_path: Path,
        name_resolver: NameResolver | None = None,
        enriched_service: EnrichedService | None = None,
    ) -> None:
        self.system_prompt = system_prompt_path.read_text(encoding="utf-8")
        self._name_resolver = name_resolver
        self._enriched_service = enriched_service

    def attach_resolver(self, name_resolver: NameResolver) -> None:
        self._name_resolver = name_resolver

    def attach_enriched(self, enriched_service: EnrichedService) -> None:
        """Inject the enriched-data service so the prompt can use
        the LLM-baked summary when the quality gate passes."""
        self._enriched_service = enriched_service

    def _get_enriched(self, entity_id: str):
        if self._enriched_service is None:
            return None
        return self._enriched_service.get(entity_id)

    def build(
        self,
        graph: StaticGraph,
        state: TemporalState,
        context: RetrievedContext,
    ) -> PromptBuildResult:
        if self._name_resolver is None:
            self._name_resolver = NameResolver(graph.entities.values())
        resolver = self._name_resolver

        entity = graph.entities[context.entity_id]
        current = state.states[context.entity_id]
        public_name = resolver.to_public(context.entity_id)

        public_neighbors: Dict[str, Dict] = {}
        for neighbor_id in sorted(set(context.changed_neighbors)):
            neighbor = state.states.get(neighbor_id)
            if not neighbor:
                continue
            display = resolver.to_public(neighbor_id)
            public_neighbors[display] = {
                "entity_id": neighbor_id,
                "state": neighbor.state,
                "abundance_label": neighbor.abundance_label,
                # ``efficiency`` is the gene's transcription-rate axis.
                # Without it the LLM cannot see that a gene is ``expressed``
                # but starved of activator, and overestimates the encoded
                # protein's abundance.
                "efficiency": neighbor.efficiency,
            }

        deduped_rules = self._dedupe_rules(context.rules)[:12]
        rule_hint_map: Dict[str, str] = {}
        public_rules: List[Dict] = []
        for index, rule in enumerate(deduped_rules, start=1):
            hint = f"R#{index}"
            rule_hint_map[hint] = rule.rule_id
            participants = rule.participants or {}
            source_public = resolver.to_public(participants.get("source_id", ""))
            target_public = resolver.to_public(participants.get("target_id", ""))
            public_rules.append(
                {
                    "hint": hint,
                    "rule_id": rule.rule_id,
                    "relation_type": participants.get("relation_type", ""),
                    "source": source_public,
                    "target": target_public,
                    "source_id": participants.get("source_id", ""),
                    "target_id": participants.get("target_id", ""),
                    "summary": self._summarize_rule(rule, source_public, target_public),
                }
            )

        public_edges: List[Dict] = []
        for edge in context.edges[:12]:
            participants_public = {
                "source": resolver.to_public(edge.source_id),
                "target": resolver.to_public(edge.target_id),
            }
            public_edges.append(
                {
                    "relation_type": edge.relation_type,
                    "source": participants_public["source"],
                    "target": participants_public["target"],
                    "source_id": edge.source_id,
                    "target_id": edge.target_id,
                    "evidence": edge.evidence,
                    "source_database": edge.source_database,
                }
            )

        payload = {
            "round": state.current_round,
            "you": {
                "name": public_name,
                "public_id_hint": context.entity_id,
                "entity_type": entity.entity_type,
                "annotation": self._select_annotation_for_llm(entity),
                "annotation_source": self._annotation_source(entity),
                "pathways": entity.pathways,
                "subcellular_location": entity.subcellular_location,
                "allowed_states": entity.allowed_states,
                "complex_type": entity.complex_type,
                "is_virtual": entity.is_virtual,
                "components": [resolver.to_public(c) for c in entity.components],
                "critical_components": [resolver.to_public(c) for c in entity.critical_components],
                "assembly_condition": entity.assembly_condition,
                "linked_entities": self._linked_entities_for_prompt(entity, resolver),
            },
            "your_state": {
                "state": current.state,
                "abundance_label": current.abundance_label,
                "efficiency": current.efficiency,
            },
            "retrieval": {
                "score": round(context.score, 4),
                "score_details": context.score_details,
            },
            "decision_policy": {
                "represses": {
                    "when_source_active": {"action_type": "change_activity", "direction": "down", "strength": 1},
                    "when_source_inhibited": {"action_type": "change_activity", "direction": "up", "strength": 1},
                },
                "activates": {
                    "when_source_active": {
                        "action_type": _activates_action_type(entity.entity_type),
                        "direction": "up",
                        "strength": 1,
                    },
                    "when_source_inhibited": {
                        "action_type": _activates_action_type(entity.entity_type),
                        "direction": "down",
                        "strength": 1,
                    },
                },
                "encodes": {
                    "when_source_high": {"action_type": "change_abundance", "direction": "up", "strength": 1},
                    "when_source_low": {"action_type": "change_abundance", "direction": "down", "strength": 1},
                },
                "is_product_of": {
                    "when_producer_active": {"action_type": "produce", "direction": "up", "strength": 1},
                },
                "is_substrate_of": {
                    "when_consumer_active": {"action_type": "consume", "direction": "down", "strength": 1},
                },
                # simulation-baseline relation vocabulary
                "produces": {
                    "when_producer_active": {"action_type": "produce", "direction": "up", "strength": 1},
                    "when_producer_inactive": {"action_type": "produce", "direction": "down", "strength": 1},
                },
                "consumes": {
                    "when_consumer_active": {"action_type": "consume", "direction": "down", "strength": 1},
                    "when_consumer_inactive": {"action_type": "consume", "direction": "up", "strength": 1},
                },
                "transcribed_as": {
                    "when_source_active": {"action_type": "change_abundance", "direction": "up", "strength": 1},
                    "when_source_inhibited": {"action_type": "change_abundance", "direction": "down", "strength": 1},
                },
                "interacts": {
                    "note": (
                        "Physical/functional protein-protein interaction (STRING). It has NO "
                        "fixed direction: a partner's change may activate, inhibit, sequester or "
                        "not affect you. Decide from your annotation and the partner's state. If "
                        "the interaction is not functionally relevant to you, return no action."
                    ),
                },
            },
            "changed_neighbors": public_neighbors,
            "candidate_rules": public_rules,
            "retrieved_edges": public_edges,
            "conflict_signals": self._format_conflict_signals(context, resolver),
            "echo_hint_instructions": (
                "Use the rule hint (R#1, R#2, ...) exactly as printed in candidate_rules. "
                "Use the public name in the targets list. You may also echo back the public_id_hint "
                "in parentheses if you need a stable handle."
            ),
        }
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": json.dumps(payload, ensure_ascii=False, indent=2)},
        ]
        return PromptBuildResult(
            messages=messages,
            rule_hint_map=rule_hint_map,
            public_name_map={context.entity_id: public_name, **{hint: public_name for hint in rule_hint_map}},
        )

    @staticmethod
    def _dedupe_rules(rules: List[Rule]) -> List[Rule]:
        seen = set()
        result = []
        for rule in rules:
            if rule.rule_id in seen:
                continue
            seen.add(rule.rule_id)
            result.append(rule)
        return result

    # ------------------------------------------------------------------
    # Enriched-annotation selection
    # ------------------------------------------------------------------
    #
    # The ``data/enriched/entities_enriched.jsonl`` cards were built
    # by an LLM and may contain hallucinations. We never let the
    # LLM in the simulation loop read those cards blindly. Instead
    # we apply a quality gate: the enriched card is used only when
    # the quality label is ``informative`` AND the summary is
    # non-empty AND its length crosses a minimum threshold. In
    # every other case we fall back to the raw UniProt /
    # EcoCyc / NCBI annotation that was loaded from the original
    # flatfiles.

    _ENRICHED_MIN_LENGTH = 40
    _ENRICHED_MAX_LENGTH = 1800

    def _select_annotation_for_llm(self, entity) -> str:
        """Choose what text the LLM will read as this agent's description.

        Looks up the enriched card from the :class:`EnrichedService`
        (a lightweight, read-through cache that reads the offline
        ``entities_enriched.jsonl``). The card is used only when its
        quality label is ``informative`` AND the summary is long
        enough to be useful. In every other case we fall back to
        the raw UniProt / EcoCyc / NCBI annotation that was loaded
        from the original flatfiles.
        """
        enriched = self._get_enriched(entity.entity_id)
        if enriched is not None and enriched.summary:
            if (
                enriched.quality_label == "informative"
                and len(enriched.summary) >= self._ENRICHED_MIN_LENGTH
            ):
                return enriched.summary[: self._ENRICHED_MAX_LENGTH]
        return entity.annotation[: self._ENRICHED_MAX_LENGTH]

    def _annotation_source(self, entity) -> str:
        """Tag the source so the LLM (and the reviewer) can tell which was used."""
        enriched = self._get_enriched(entity.entity_id)
        if enriched is not None and enriched.summary:
            if (
                enriched.quality_label == "informative"
                and len(enriched.summary) >= self._ENRICHED_MIN_LENGTH
            ):
                return "enriched.summary"
        return "raw.annotation"

    # ------------------------------------------------------------------
    # linked_entities truncation
    # ------------------------------------------------------------------
    #
    # Different entity types have different semantic roles. We limit
    # the per-bucket size so a single LLM call cannot be overwhelmed
    # by a metabolic-network entity whose linked list of reactions
    # runs into the hundreds. The caps follow the user's
    # specification:

    _LINKED_CAPS = {
        "gene": 5,
        "protein": 5,
        "small_molecule": 5,
        "complex": 100,        # complexes: never truncate components
        "reaction": 5,
        "rna": 5,
    }

    def _linked_entities_for_prompt(self, entity, resolver) -> Dict:
        """Render the entity's enriched linked_entities, truncated by type.

        Each linked entity in the prompt includes both the public
        display name and a one-time bracket reference to its
        canonical id, e.g. ``"LacI repressor [protein.P03023]"``.
        Downstream code (the report, the conflict renderer) is
        responsible for remembering the id after the first mention
        so subsequent references can be just the display name.
        """
        enriched = self._get_enriched(entity.entity_id)
        if enriched is None:
            return {}
        linked = enriched.linked_entities or {}
        cap = self._LINKED_CAPS.get(entity.entity_type, 5)
        result: Dict[str, List[Dict]] = {}
        for key, value in linked.items():
            if isinstance(value, list):
                items = value[: cap]
            elif isinstance(value, dict):
                items = [value]
            else:
                continue
            rendered = []
            for item in items:
                if not isinstance(item, dict):
                    continue
                entity_id = item.get("entity_id")
                if not entity_id:
                    continue
                public_name = resolver.to_public(entity_id)
                rendered.append(
                    {
                        "label": f"{public_name} [{entity_id}]",
                        "public_name": public_name,
                        "entity_id": entity_id,
                        "entity_type": item.get("entity_type"),
                    }
                )
            if rendered:
                result[key] = rendered
        return result

    def _format_conflict_signals(self, context, resolver) -> Dict:
        """Render the conflict report into a prompt-friendly block.

        The LLM receives:
          * the list of incoming signals with their inferred direction
          * whether the directions conflict
          * a specific hint telling the LLM where to look for the answer
            (the entity's annotation)
        """
        report = context.conflict
        signals_payload = []
        for signal in report.signals:
            signals_payload.append(
                {
                    "source": resolver.to_public(signal.source),
                    "source_id_hint": signal.source,
                    "relation_type": signal.relation_type,
                    "source_state": signal.source_state,
                    "inferred_direction": signal.direction,
                    "note": signal.note,
                }
            )
        if not report.conflict:
            return {
                "status": "no_conflict",
                "axis_summary": dict(report.axis_summary),
                "signals": signals_payload,
                "hint": "",
            }
        return {
            "status": "conflict",
            "axis_summary": dict(report.axis_summary),
            "signals": signals_payload,
            "hint": report.hint or (
                "你的上游调控因子发出了方向不一致的信号。"
                "读你的功能注释（annotation），决定净方向。"
            ),
            "mock_refused": True,
        }

    @staticmethod
    def _summarize_rule(rule: Rule, source_public: str, target_public: str) -> str:
        relation = rule.participants.get("relation_type", "")
        effect_hint = ""
        if rule.effects:
            first_effect = rule.effects[0]
            effect_hint = first_effect.get("effect_hint", "") or first_effect.get("relation_type", "")
        if relation in {"represses", "activates"}:
            return f"{source_public} {relation} {target_public} ({effect_hint or relation})"
        if relation in {"encodes", "transcribed_as"}:
            return f"{source_public} {relation} {target_public}"
        if relation in {"is_product_of", "is_substrate_of", "catalyzes", "produces", "consumes"}:
            return f"{source_public} {relation} {target_public}"
        if relation == "interacts":
            return f"{source_public} physically interacts with {target_public} (direction undecided — you decide)"
        if relation:
            return f"{source_public} {relation} {target_public}"
        return rule.notes or rule.rule_id
