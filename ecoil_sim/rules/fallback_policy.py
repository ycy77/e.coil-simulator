"""Configurable deterministic-fallback policy.

When the LLM returns no actionable signal, the simulator falls back to a
deterministic rule so the propagation chain never stalls. The fallback is
declared in ``configs/fallback_rules.yaml`` and is loaded at startup.

The policy format is intentionally compact::

    rules:
      - relation: represses
        conflict_free_only: true
        active_source:
          action_type: change_activity
          direction: down
          strength: 1
        inactive_source:
          action_type: change_activity
          direction: up
          strength: 1

Each rule maps a relation and a coarse source-activity bucket to a single
canonical action. The interpreter walks the candidate edges in retrieval
order and applies the first matching rule.

Key design rule
---------------

The mock is not a "priority judge". When the candidate has conflicting
incoming signals (e.g. one regulator pushing UP while another pushes
DOWN), the rules with ``conflict_free_only: true`` deliberately *opt
out* and let the LLM handle the conflict. The mock is only allowed to
act when its decision is unambiguous (single direction or same-direction
multi-signal).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

from ecoil_sim.config import load_yaml_like


_INACTIVE_STATES = {
    "inhibited",
    "degraded",
    "sequestered",
    "knocked_out",
    "mutated",
    "repressed",
    "absent",
    "low",
    "impaired",
    "disrupted",
    "disassembled",
}


_ACTIVE_STATES = {
    "active",
    "expressed",
    "overexpressed",
    "assembled",
    "medium",
    "high",
}


@dataclass
class FallbackActionTemplate:
    action_type: str
    direction: str
    strength: int = 1
    reason: str = ""

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "FallbackActionTemplate":
        return cls(
            action_type=str(data.get("action_type", "no_op")).strip(),
            direction=str(data.get("direction", "none")).strip(),
            strength=int(data.get("strength", 1)),
            reason=str(data.get("reason", "")).strip(),
        )


@dataclass
class FallbackRule:
    relation: str
    active_source: Optional[FallbackActionTemplate] = None
    inactive_source: Optional[FallbackActionTemplate] = None
    target_entity_type: Optional[str] = None
    source_entity_type: Optional[str] = None
    requires_target_role: str = "downstream"
    name: str = ""
    # When True, the rule only fires if the candidate's incoming signals
    # do not include direction conflicts. When False, the rule fires
    # regardless of conflict status (legacy behaviour, useful only for
    # relations that don't produce direction signals such as encoding).
    conflict_free_only: bool = True

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "FallbackRule":
        active = data.get("active_source")
        inactive = data.get("inactive_source")
        return cls(
            relation=str(data.get("relation", "")).strip(),
            active_source=FallbackActionTemplate.from_dict(active) if active else None,
            inactive_source=FallbackActionTemplate.from_dict(inactive) if inactive else None,
            target_entity_type=data.get("target_entity_type"),
            source_entity_type=data.get("source_entity_type"),
            requires_target_role=str(data.get("requires_target_role", "downstream")),
            name=str(data.get("name", "")).strip(),
            conflict_free_only=bool(data.get("conflict_free_only", True)),
        )


@dataclass
class FallbackPolicy:
    rules: List[FallbackRule] = field(default_factory=list)
    inactive_states: set = field(default_factory=lambda: set(_INACTIVE_STATES))
    active_states: set = field(default_factory=lambda: set(_ACTIVE_STATES))
    enabled: bool = True
    max_candidates_per_call: int = 8

    @classmethod
    def empty(cls) -> "FallbackPolicy":
        return cls(rules=[], enabled=False)

    @classmethod
    def from_config(cls, path: Path) -> "FallbackPolicy":
        if not path.exists():
            return cls.empty()
        raw = load_yaml_like(path)
        rules_data = raw.get("rules", []) if isinstance(raw, dict) else []
        rules = [FallbackRule.from_dict(item) for item in rules_data if isinstance(item, dict)]
        return cls(
            rules=rules,
            inactive_states=set(raw.get("inactive_states", list(_INACTIVE_STATES))) if isinstance(raw, dict) else set(_INACTIVE_STATES),
            active_states=set(raw.get("active_states", list(_ACTIVE_STATES))) if isinstance(raw, dict) else set(_ACTIVE_STATES),
            enabled=bool(raw.get("enabled", True)) if isinstance(raw, dict) else True,
            max_candidates_per_call=int(raw.get("max_candidates_per_call", 8)) if isinstance(raw, dict) else 8,
        )

    def is_source_active(self, state: str) -> bool:
        return state in self.active_states

    def is_source_inactive(self, state: str) -> bool:
        return state in self.inactive_states

    def match(self, relation: str) -> Optional[FallbackRule]:
        for rule in self.rules:
            if rule.relation == relation:
                return rule
        return None

    def summary(self) -> Dict[str, int]:
        return {"rules": len(self.rules)}
