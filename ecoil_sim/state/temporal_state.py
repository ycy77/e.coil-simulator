from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, List, Optional

from ecoil_sim.models import AgentState, Entity


@dataclass
class TemporalState:
    current_round: int = 0
    states: Dict[str, AgentState] = field(default_factory=dict)
    history: Dict[str, List[Dict]] = field(default_factory=dict)
    round_history: List[Dict] = field(default_factory=list)

    @classmethod
    def initialize(cls, entities: Iterable[Entity], initial_profile: Dict[str, Any] | None = None) -> "TemporalState":
        state = cls()
        for entity in entities:
            default_state = entity.default_state or (entity.allowed_states[0] if entity.allowed_states else "unknown")
            state.states[entity.entity_id] = AgentState(
                entity_id=entity.entity_id,
                state=default_state,
                abundance_label="medium" if entity.entity_type == "small_molecule" else "",
                metadata={"source": "database", "initialization": "entity_default"},
            )
            state.history[entity.entity_id] = [
                {
                    "round": 0,
                    **state.states[entity.entity_id].to_dict(),
                    "reason": "initial default state",
                }
            ]
        if initial_profile:
            state.apply_initial_profile(initial_profile)
        state.round_history.append(state.snapshot())
        return state

    @classmethod
    def from_snapshot(
        cls,
        entities: Iterable[Entity],
        snapshot: Dict[str, Any],
        source_run: str = "",
    ) -> "TemporalState":
        state = cls.initialize(entities)
        snapshot_states = snapshot.get("states", {}) if isinstance(snapshot, dict) else {}
        for entity_id, payload in snapshot_states.items():
            if entity_id not in state.states or not isinstance(payload, dict):
                continue
            old = state.states[entity_id]
            resumed = AgentState(
                entity_id=entity_id,
                state=payload.get("state", old.state),
                abundance_label=payload.get("abundance_label", old.abundance_label),
                changed=False,
                reason="continued baseline from previous simulation state",
                changed_neighbors=[],
                metadata={
                    **(payload.get("metadata", {}) if isinstance(payload.get("metadata"), dict) else {}),
                    "source": "database",
                    "initialization": "resume_run",
                    "source_run": source_run,
                    "source_round": snapshot.get("round", ""),
                },
            )
            state.states[entity_id] = resumed
            state.history[entity_id] = [{"round": 0, **resumed.to_dict()}]
        state.round_history = [state.snapshot()]
        return state

    def apply_initial_profile(self, profile: Dict[str, Any]) -> None:
        profile_id = str(profile.get("profile_id", "unnamed_profile"))
        source = str(profile.get("source", "database"))
        overrides = profile.get("overrides", {})
        if not isinstance(overrides, dict):
            return
        for entity_id, spec in overrides.items():
            if entity_id not in self.states or not isinstance(spec, dict):
                continue
            old = self.states[entity_id]
            next_state = spec.get("state", old.state)
            next_abundance = spec.get("abundance_label", old.abundance_label)
            initialized = AgentState(
                entity_id=entity_id,
                state=next_state,
                abundance_label=next_abundance,
                changed=False,
                reason=spec.get("reason", f"initial condition profile {profile_id}"),
                changed_neighbors=[],
                metadata={
                    "source": source,
                    "initialization": "initial_profile",
                    "profile_id": profile_id,
                    "confidence": spec.get("confidence", profile.get("confidence", "medium")),
                },
            )
            self.states[entity_id] = initialized
            self.history[entity_id] = [{"round": 0, **initialized.to_dict()}]

    def get(self, entity_id: str) -> Optional[AgentState]:
        return self.states.get(entity_id)

    def changed_entities(self) -> List[str]:
        return [entity_id for entity_id, state in self.states.items() if state.changed]

    def apply_changes(self, changes: Iterable[AgentState], reason_prefix: str = "") -> int:
        changed_count = 0
        for new_state in changes:
            old = self.states.get(new_state.entity_id)
            if old is None:
                continue
            did_change = old.state != new_state.state or old.abundance_label != new_state.abundance_label
            new_state.changed = did_change or new_state.changed
            if reason_prefix and new_state.reason:
                new_state.reason = f"{reason_prefix}: {new_state.reason}"
            self.states[new_state.entity_id] = new_state
            if new_state.changed:
                changed_count += 1
            self.history.setdefault(new_state.entity_id, []).append(
                {"round": self.current_round, **new_state.to_dict()}
            )
        return changed_count

    def begin_round(self) -> None:
        self.current_round += 1
        for state in self.states.values():
            state.changed = False
            state.changed_neighbors = []

    def end_round(self) -> Dict:
        snap = self.snapshot()
        self.round_history.append(snap)
        return snap

    def snapshot(self) -> Dict:
        return {
            "round": self.current_round,
            "states": {entity_id: state.to_dict() for entity_id, state in self.states.items()},
        }
