"""Validate and canonicalize LLM-emitted action proposals.

The validator accepts payloads shaped like::

    {
        "actions": [
            {
                "action_type": "change_activity",
                "rule_id": "R#3",                       # may also be the canonical rule id
                "targets": ["LacI repressor", "protein.P03023"],
                "direction": "up",
                "strength": 1,
                "reason": "..."
            }
        ]
    }

* ``rule_id`` may be a hint string such as ``"R#3"`` that the prompt builder
  assigned. The validator resolves it against the candidate rules in the
  call context.
* ``targets`` may list public names, KEGG ids, UniProt accessions or the
  canonical internal entity id. They are resolved through
  :class:`NameResolver`.
* If a target cannot be resolved, the action is dropped rather than silently
  applied to a wrong entity.

A :class:`ValidatedAction` contains both the resolved canonical form and the
provenance of every translated field, so the interpreter can later reason
about confidence.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple


@dataclass
class ValidatedAction:
    action_type: str
    rule_id: str
    targets: List[str]
    direction: str
    strength: int
    reason: str
    diagnostics: Dict[str, Any] = field(default_factory=dict)

    def as_dict(self) -> Dict[str, Any]:
        return {
            "action_type": self.action_type,
            "rule_id": self.rule_id,
            "targets": list(self.targets),
            "direction": self.direction,
            "strength": self.strength,
            "reason": self.reason,
            **({"diagnostics": self.diagnostics} if self.diagnostics else {}),
        }


class ActionValidator:
    ACTION_TYPES = {
        "change_abundance",
        "change_mrna_abundance",
        "change_efficiency",
        "change_activity",
        "bind",
        "unbind",
        "assemble_complex",
        "disassemble_complex",
        "move_between_locations",
        "consume",
        "produce",
        "mark_inhibited",
        "mark_mutated",
        "sleep",
        "no_op",
    }
    DIRECTIONS = {"up", "down", "set", "none"}
    REQUIRED = {"action_type", "rule_id", "targets", "direction", "strength", "reason"}

    def __init__(self, name_resolver=None) -> None:
        self.name_resolver = name_resolver

    def validate(
        self,
        payload: Any,
        candidate_rule_ids: Optional[Set[str]] = None,
        rule_hint_map: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        if not isinstance(payload, dict):
            return {"actions": []}
        actions = payload.get("actions", [])
        if not isinstance(actions, list):
            return {"actions": []}
        valid: List[Dict[str, Any]] = []
        for action in actions:
            cleaned = self._clean_action(
                action,
                candidate_rule_ids=candidate_rule_ids,
                rule_hint_map=rule_hint_map,
            )
            if cleaned is not None:
                valid.append(cleaned.as_dict())
        return {"actions": valid}

    def _clean_action(
        self,
        action: Any,
        candidate_rule_ids: Optional[Set[str]] = None,
        rule_hint_map: Optional[Dict[str, str]] = None,
    ) -> Optional[ValidatedAction]:
        if not isinstance(action, dict):
            return None
        if not self.REQUIRED.issubset(action.keys()):
            return None
        action_type = str(action.get("action_type", "")).strip()
        direction = str(action.get("direction", "")).strip()
        if action_type not in self.ACTION_TYPES or direction not in self.DIRECTIONS:
            return None
        try:
            strength = int(action.get("strength", 0))
        except (TypeError, ValueError):
            return None
        if strength < 0 or strength > 2:
            return None
        raw_targets = action.get("targets", [])
        if not isinstance(raw_targets, list) or not all(isinstance(item, str) for item in raw_targets):
            return None
        raw_rule_id = str(action.get("rule_id", "")).strip()
        if not raw_rule_id:
            return None
        rule_id, rule_diag = self._resolve_rule_id(
            raw_rule_id,
            candidate_rule_ids=candidate_rule_ids,
            rule_hint_map=rule_hint_map,
        )
        if not rule_id:
            return None
        targets, target_diag = self._resolve_targets(raw_targets)
        if raw_targets and not targets:
            return None
        reason = str(action.get("reason", "")).strip()[:500]
        diagnostics: Dict[str, Any] = {}
        if rule_diag:
            diagnostics["rule_id"] = rule_diag
        if target_diag:
            diagnostics["targets"] = target_diag
        return ValidatedAction(
            action_type=action_type,
            rule_id=rule_id,
            targets=targets,
            direction=direction,
            strength=strength,
            reason=reason,
            diagnostics=diagnostics,
        )

    def _resolve_rule_id(
        self,
        raw: str,
        candidate_rule_ids: Optional[Set[str]],
        rule_hint_map: Optional[Dict[str, str]],
    ) -> Tuple[Optional[str], Dict[str, Any]]:
        diag: Dict[str, Any] = {"raw": raw}
        if rule_hint_map and raw in rule_hint_map:
            resolved = rule_hint_map[raw]
            diag.update({"resolved_via": "hint", "resolved_to": resolved})
            if candidate_rule_ids is not None and resolved not in candidate_rule_ids:
                diag["rejected"] = "hint_not_in_candidate_set"
                return None, diag
            return resolved, diag
        if candidate_rule_ids is not None and raw not in candidate_rule_ids:
            diag["rejected"] = "raw_not_in_candidate_set"
            return None, diag
        diag.update({"resolved_via": "exact", "resolved_to": raw})
        return raw, diag

    def _resolve_targets(self, raw_targets: Sequence[str]) -> Tuple[List[str], Dict[str, Any]]:
        if not raw_targets:
            return [], {"count": 0}
        resolved: List[str] = []
        diag: Dict[str, Any] = {"items": [], "unresolved": []}
        for raw in raw_targets:
            stripped = raw.strip()
            if not stripped:
                continue
            entity_id = self._resolve_one(stripped)
            if entity_id is None:
                diag["unresolved"].append(stripped)
                continue
            if entity_id not in resolved:
                resolved.append(entity_id)
            diag["items"].append({"raw": stripped, "resolved_to": entity_id})
        diag["count"] = len(resolved)
        return resolved, diag

    def _resolve_one(self, text: str) -> Optional[str]:
        if self.name_resolver is None:
            return text
        resolved = self.name_resolver.from_public(text)
        if resolved is not None:
            return resolved.entity_id
        return None
