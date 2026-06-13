from __future__ import annotations

from typing import Iterable, List

from ecoil_sim.graph import StaticGraph
from ecoil_sim.models import AgentState
from ecoil_sim.state import TemporalState


class RuleEngine:
    """Deterministic state updates. LLM handles only unresolved cases."""

    def __init__(self, graph: StaticGraph | None = None) -> None:
        self.graph = graph

    def apply_perturbations(self, state: TemporalState, perturbations: Iterable[dict]) -> List[AgentState]:
        updates: List[AgentState] = []
        for item in perturbations:
            entity_id = item.get("entity_id")
            if not entity_id or entity_id not in state.states:
                continue
            old = state.states[entity_id]
            updates.append(
                AgentState(
                    entity_id=entity_id,
                    state=item.get("state", old.state),
                    abundance_label=item.get("abundance_label", old.abundance_label),
                    changed=True,
                    reason=item.get("reason", "user perturbation"),
                    metadata={
                        "source": item.get("source", "database"),
                        "confidence": item.get("confidence", "medium"),
                        "raw_input": item.get("raw_input", ""),
                        "input_source": item.get("input_source", "user"),
                        "perturbation_layer": item.get("perturbation_layer", ""),
                    },
                )
            )
        return updates

    def apply_structural_complexes(self, state: TemporalState) -> List[AgentState]:
        if not self.graph:
            return []
        updates: List[AgentState] = []
        for entity in self.graph.entities.values():
            if entity.entity_type != "complex" or entity.complex_type != "structural" or not entity.critical_components:
                continue
            old = state.states.get(entity.entity_id)
            if not old:
                continue
            component_states = [
                state.states.get(component_id)
                for component_id in entity.critical_components
            ]
            if not component_states or any(component is None for component in component_states):
                continue
            values = {component.state for component in component_states if component is not None}
            if "degraded" in values or "disrupted" in values:
                next_state = self._allowed_state(entity.allowed_states, "disrupted", "degraded", old.state)
            elif "inhibited" in values or "impaired" in values:
                next_state = self._allowed_state(entity.allowed_states, "impaired", "inhibited", old.state)
            elif all(value == "active" for value in values):
                next_state = self._allowed_state(entity.allowed_states, "active", "assembled", old.state)
            else:
                next_state = old.state
            if next_state != old.state:
                updates.append(
                    AgentState(
                        entity_id=entity.entity_id,
                        state=next_state,
                        abundance_label=old.abundance_label,
                        changed=True,
                        reason="structural complex state computed from critical components",
                        changed_neighbors=list(entity.critical_components),
                        metadata={
                            "source": "database",
                            "confidence": "high",
                            "rule_layer": "deterministic_structural_complex",
                        },
                    )
                )
        return updates

    @staticmethod
    def _allowed_state(allowed_states: List[str], *candidates: str) -> str:
        allowed = set(allowed_states)
        for candidate in candidates:
            if candidate in allowed:
                return candidate
        return candidates[-1]
