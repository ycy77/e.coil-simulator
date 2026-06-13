from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List

from ecoil_sim.models import Edge, Rule
from ecoil_sim.paths import REGISTRY_DIR


class RuleRegistry:
    """External rule registry. Simulation logic depends on this interface only."""

    def __init__(self, rules: Iterable[Rule]) -> None:
        self.rules = list(rules)
        self.by_id: Dict[str, Rule] = {rule.rule_id: rule for rule in self.rules}
        self.by_pair: Dict[tuple[str, str, str], List[Rule]] = defaultdict(list)
        self.by_entity: Dict[str, List[Rule]] = defaultdict(list)
        for rule in self.rules:
            source = rule.participants.get("source_id", "")
            target = rule.participants.get("target_id", "")
            relation = rule.participants.get("relation_type", "")
            if source and target and relation:
                self.by_pair[(source, target, relation)].append(rule)
                self.by_pair[(target, source, relation)].append(rule)
                self.by_entity[source].append(rule)
                self.by_entity[target].append(rule)

    @classmethod
    def from_registry_dir(cls, path: Path = REGISTRY_DIR) -> "RuleRegistry":
        rules: List[Rule] = []
        if not path.exists():
            return cls(rules)
        for file in sorted(path.glob("*.jsonl")):
            with file.open(encoding="utf-8") as handle:
                for line in handle:
                    line = line.strip()
                    if line:
                        rules.append(Rule.from_dict(json.loads(line)))
        return cls(rules)

    def candidate_rules_for_edge(self, edge: Edge) -> List[Rule]:
        return self.by_pair.get((edge.source_id, edge.target_id, edge.relation_type), [])

    def candidate_rules_for_entity(self, entity_id: str) -> List[Rule]:
        return list(self.by_entity.get(entity_id, []))

    def summary(self) -> Dict[str, int]:
        return {"rules": len(self.rules), "indexed_entities": len(self.by_entity)}
