"""Translate validated LLM actions into canonical AgentState updates.

Inputs are :class:`ecoil_sim.retrieval.RetrievedContext` (graph neighbors and
candidate rules) plus an LLM-emitted payload. The interpreter:

1. Confirms the action's rule_id is among the candidate rules.
2. Confirms the action's targets (now resolved by the validator) include
   the current agent.
3. Applies the action via :meth:`_apply_action` to compute the new state
   and abundance.
4. If the LLM emitted no actionable signal, applies the configurable
   :class:`FallbackPolicy` so propagation never stalls.
"""

from __future__ import annotations

from typing import Any, Dict, Iterable, List, Set

from ecoil_sim.graph import StaticGraph
from ecoil_sim.models import AgentState
from ecoil_sim.retrieval import RetrievedContext
from ecoil_sim.rules import FallbackActionTemplate, FallbackPolicy
from ecoil_sim.state import TemporalState


class ActionInterpreter:
    """Translate validated LLM actions into canonical AgentState updates."""

    def __init__(
        self,
        graph: StaticGraph,
        fallback_policy: FallbackPolicy | None = None,
    ) -> None:
        self.graph = graph
        self.fallback_policy = fallback_policy or FallbackPolicy.empty()

    def interpret(
        self,
        state: TemporalState,
        context: RetrievedContext,
        output: Dict,
    ) -> AgentState:
        old = state.states[context.entity_id]
        entity = self.graph.entities[context.entity_id]
        candidate_rule_ids = {rule.rule_id for rule in context.rules}
        actions = output.get("actions", []) if isinstance(output, dict) else []
        valid_actions = [
            action for action in actions
            if self._is_valid_action(action, context.entity_id, candidate_rule_ids)
        ]

        if not valid_actions:
            fallback = self._fallback_action(state, context)
            if fallback:
                next_state, next_abundance = self._apply_action(
                    entity_type=entity.entity_type,
                    allowed_states=set(entity.allowed_states),
                    current_state=old.state,
                    current_abundance=old.abundance_label,
                    action=fallback,
                )
                next_efficiency = self._apply_efficiency(old.efficiency, fallback)
                did_change = (
                    next_state != old.state
                    or next_abundance != old.abundance_label
                    or next_efficiency != old.efficiency
                )
                metadata = self._llm_metadata(output)
                metadata["deterministic_fallback"] = True
                metadata.setdefault("fallback_rule", fallback.get("_fallback_rule", ""))
                return AgentState(
                    entity_id=context.entity_id,
                    state=next_state,
                    abundance_label=next_abundance,
                    efficiency=next_efficiency,
                    changed=did_change,
                    reason=fallback.get("reason", "deterministic fallback action"),
                    changed_neighbors=sorted(set(context.changed_neighbors)),
                    metadata=metadata,
                )
            return AgentState(
                entity_id=context.entity_id,
                state=old.state,
                abundance_label=old.abundance_label,
                efficiency=old.efficiency,
                changed=False,
                reason="no supported action",
                changed_neighbors=sorted(set(context.changed_neighbors)),
                metadata=self._llm_metadata(output),
            )

        # We may receive multiple actions. ``change_efficiency`` is
        # composed separately from state/abundance actions, so we
        # iterate once for state/abundance and once for efficiency.
        state_actions = [a for a in valid_actions if a.get("action_type") != "change_efficiency"]
        eff_actions = [a for a in valid_actions if a.get("action_type") == "change_efficiency"]
        action = self._choose_action(state_actions) if state_actions else None
        eff_action = eff_actions[0] if eff_actions else None

        next_state, next_abundance = old.state, old.abundance_label
        reason = "no supported action"
        if action is not None:
            next_state, next_abundance = self._apply_action(
                entity_type=entity.entity_type,
                allowed_states=set(entity.allowed_states),
                current_state=old.state,
                current_abundance=old.abundance_label,
                action=action,
            )
            reason = action.get("reason", "supported action")
        next_efficiency = old.efficiency
        if eff_action is not None:
            next_efficiency = self._apply_efficiency(old.efficiency, eff_action) or old.efficiency
        did_change = (
            next_state != old.state
            or next_abundance != old.abundance_label
            or next_efficiency != old.efficiency
        )
        return AgentState(
            entity_id=context.entity_id,
            state=next_state,
            abundance_label=next_abundance,
            efficiency=next_efficiency,
            changed=did_change,
            reason=reason,
            changed_neighbors=sorted(set(context.changed_neighbors)),
            metadata=self._llm_metadata(output),
        )

    @staticmethod
    def _llm_metadata(output: Dict) -> Dict:
        metadata: Dict[str, Any] = {}
        if not isinstance(output, dict):
            return metadata
        if output.get("_error"):
            metadata["llm_error"] = output.get("_error")
        if output.get("_raw_content"):
            metadata["llm_raw_content"] = output.get("_raw_content")
        if output.get("_parsed_payload"):
            metadata["llm_parsed_payload"] = output.get("_parsed_payload")
        if output.get("_parse_diagnostics"):
            metadata["llm_parse_diagnostics"] = output.get("_parse_diagnostics")
        if output.get("_attempt") is not None:
            metadata["llm_attempt"] = output.get("_attempt")
        return metadata

    def _fallback_action(self, state: TemporalState, context: RetrievedContext) -> Dict | None:
        if not self.fallback_policy.enabled or not self.fallback_policy.rules:
            return None
        current_id = context.entity_id
        current_entity = self.graph.entities.get(current_id)
        current_type = current_entity.entity_type if current_entity else ""
        candidate_rule_ids = {rule.rule_id for rule in context.rules}
        for edge in context.edges[: self.fallback_policy.max_candidates_per_call]:
            source = edge.source_id
            target = edge.target_id
            relation = edge.relation_type
            if current_id not in {source, target}:
                continue
            is_target = target == current_id
            is_source = source == current_id
            neighbor_id = source if is_target else target
            if neighbor_id not in set(context.changed_neighbors):
                continue
            neighbor_state = state.states.get(neighbor_id)
            if not neighbor_state:
                continue
            rule = self.fallback_policy.match(relation)
            if not rule:
                continue
            if rule.requires_target_role == "downstream" and not is_target:
                continue
            if rule.requires_target_role == "upstream" and not is_source:
                continue
            if rule.target_entity_type and rule.target_entity_type != current_type:
                continue
            if rule.source_entity_type:
                neighbor_entity = self.graph.entities.get(neighbor_id)
                if not neighbor_entity or neighbor_entity.entity_type != rule.source_entity_type:
                    continue
            if rule.conflict_free_only and context.conflict.conflict:
                # Mock refuses to act on a direction-conflicting candidate.
                # The LLM is expected to resolve the conflict using its
                # annotation; if it doesn't, the agent stays unchanged this
                # round, which is the correct safety default.
                continue
            template = self._pick_template(rule, neighbor_state.state)
            if not template:
                continue
            rule_id = self._matching_rule_id(context, source, target, relation, candidate_rule_ids)
            if not rule_id:
                continue
            return self._render_template(template, current_id, rule_id, rule.name)

        return None

    def _pick_template(self, rule, neighbor_state: str) -> FallbackActionTemplate | None:
        if self.fallback_policy.is_source_active(neighbor_state):
            return rule.active_source
        if self.fallback_policy.is_source_inactive(neighbor_state):
            return rule.inactive_source
        return None

    def _render_template(
        self,
        template: FallbackActionTemplate,
        current_id: str,
        rule_id: str,
        rule_name: str,
    ) -> Dict[str, Any]:
        reason = template.reason or f"deterministic fallback: {rule_name or rule_id}"
        return {
            "action_type": template.action_type,
            "rule_id": rule_id,
            "targets": [current_id],
            "direction": template.direction,
            "strength": template.strength,
            "reason": reason,
            "_fallback_rule": rule_name or rule_id,
        }

    def _matching_rule_id(
        self,
        context: RetrievedContext,
        source: str,
        target: str,
        relation: str,
        candidate_rule_ids: Set[str],
    ) -> str:
        for rule in context.rules:
            participants = rule.participants
            if (
                rule.rule_id in candidate_rule_ids
                and participants.get("source_id") == source
                and participants.get("target_id") == target
                and participants.get("relation_type") == relation
            ):
                return rule.rule_id
        return ""

    @staticmethod
    def _is_valid_action(action: Dict, current_entity_id: str, candidate_rule_ids: Set[str]) -> bool:
        if not isinstance(action, dict):
            return False
        if action.get("rule_id") not in candidate_rule_ids:
            return False
        targets = action.get("targets") or []
        return not targets or current_entity_id in targets

    @staticmethod
    def _choose_action(actions: List[Dict]) -> Dict:
        non_noop = [action for action in actions if action.get("action_type") not in {"sleep", "no_op"}]
        if not non_noop:
            return actions[0]
        non_noop.sort(key=lambda action: int(action.get("strength", 0)), reverse=True)
        return non_noop[0]

    def _apply_action(
        self,
        entity_type: str,
        allowed_states: Set[str],
        current_state: str,
        current_abundance: str,
        action: Dict,
    ) -> tuple[str, str]:
        action_type = action.get("action_type", "no_op")
        direction = action.get("direction", "none")
        strength = int(action.get("strength", 0))

        if action_type in {"sleep", "no_op", "move_between_locations"}:
            return current_state, current_abundance

        if action_type == "mark_inhibited":
            return self._allowed("inhibited", allowed_states, current_state), current_abundance
        if action_type == "mark_mutated":
            return self._allowed("mutated", allowed_states, current_state), current_abundance
        if action_type == "bind":
            return self._allowed("sequestered", allowed_states, current_state), current_abundance
        if action_type == "unbind":
            return self._activate(entity_type, allowed_states, strength), current_abundance
        if action_type == "assemble_complex":
            return self._allowed("assembled", allowed_states, self._allowed("active", allowed_states, current_state)), current_abundance
        if action_type in {"disassemble_complex", "degradation"}:
            return self._allowed("disassembled", allowed_states, self._allowed("degraded", allowed_states, current_state)), current_abundance

        if action_type in {"produce", "change_abundance"}:
            abundance = self._shift_abundance(current_abundance, direction, strength)
            state = self._state_from_abundance(abundance, allowed_states, current_state)
            return state, abundance

        if action_type == "consume":
            abundance = self._shift_abundance(current_abundance, "down", max(1, strength))
            state = self._state_from_abundance(abundance, allowed_states, current_state)
            return state, abundance

        if action_type == "change_mrna_abundance":
            if direction == "up":
                return self._allowed("overexpressed" if strength >= 2 else "expressed", allowed_states, current_state), current_abundance
            if direction == "down":
                return self._allowed("repressed", allowed_states, current_state), current_abundance
            return current_state, current_abundance

        if action_type == "change_activity":
            if direction == "up":
                return self._activate(entity_type, allowed_states, strength), current_abundance
            if direction == "down":
                return self._repress_or_inhibit(entity_type, allowed_states, current_state), current_abundance
            return current_state, current_abundance

        return current_state, current_abundance

    @staticmethod
    def _allowed(preferred: str, allowed_states: Set[str], fallback: str) -> str:
        return preferred if preferred in allowed_states else fallback

    def _activate(self, entity_type: str, allowed_states: Set[str], strength: int) -> str:
        if entity_type == "gene":
            return self._allowed("overexpressed" if strength >= 2 else "expressed", allowed_states, "expressed")
        if entity_type == "small_molecule":
            return self._allowed("high" if strength >= 2 else "medium", allowed_states, "medium")
        return self._allowed("active", allowed_states, "active")

    def _repress_or_inhibit(self, entity_type: str, allowed_states: Set[str], fallback: str) -> str:
        if entity_type == "gene":
            return self._allowed("repressed", allowed_states, fallback)
        if entity_type == "small_molecule":
            return self._allowed("low", allowed_states, fallback)
        return self._allowed("inhibited", allowed_states, fallback)

    @staticmethod
    def _shift_abundance(current: str, direction: str, strength: int) -> str:
        labels = ["absent", "low", "medium", "high"]
        current = current if current in labels else "medium"
        idx = labels.index(current)
        step = max(1, strength)
        if direction == "up":
            idx = min(len(labels) - 1, idx + step)
        elif direction == "down":
            idx = max(0, idx - step)
        elif direction == "set":
            idx = min(len(labels) - 1, step)
        return labels[idx]

    @staticmethod
    def _state_from_abundance(abundance: str, allowed_states: Set[str], fallback: str) -> str:
        return abundance if abundance in allowed_states else fallback

    @staticmethod
    def _shift_efficiency(direction: str) -> str:
        if direction == "up":
            return "high"
        if direction == "down":
            return "low"
        if direction == "set":
            return "medium"
        return ""

    def _apply_efficiency(self, current: str, action: Dict) -> str:
        """Translate a ``change_efficiency`` action into a new efficiency value.

        ``change_efficiency`` operates on the transcription efficiency
        axis (high / low), which is independent from state and
        abundance. It is the second-layer regulation: a gene can be
        ``expressed`` (RNA pol can bind) but still have ``low``
        efficiency (no CRP-cAMP, low transcription rate).
        """
        action_type = action.get("action_type", "")
        if action_type != "change_efficiency":
            return current
        direction = action.get("direction", "none")
        new_eff = self._shift_efficiency(direction)
        return new_eff or current
