from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List

from ecoil_sim.graph import StaticGraph
from ecoil_sim.llm import ConflictReport, build_conflict_report, compute_signals
from ecoil_sim.models import Edge, Rule
from ecoil_sim.registry import RuleRegistry
from ecoil_sim.state import TemporalState


@dataclass
class RetrievedContext:
    entity_id: str
    score: float
    edges: List[Edge] = field(default_factory=list)
    rules: List[Rule] = field(default_factory=list)
    changed_neighbors: List[str] = field(default_factory=list)
    score_details: Dict[str, float] = field(default_factory=dict)
    conflict: ConflictReport = field(default_factory=lambda: ConflictReport(signals=[], conflict=False, axis_summary={}))

    def conflict_summary(self) -> Dict:
        return self.conflict.to_dict()


class TemporalGraphRAG:
    """Retrieve relevant local graph and temporal evidence for each round."""

    def __init__(
        self,
        graph: StaticGraph,
        registry: RuleRegistry,
        edge_weights: Dict[str, float],
        state_distance: Dict[str, Dict[str, float]] | None = None,
        min_score: float = 0.2,
        recent_window: int = 3,
        decay_base: float = 0.7,
        recent_change_bonus: float = 0.3,
    ) -> None:
        self.graph = graph
        self.registry = registry
        self.edge_weights = edge_weights
        self.state_distance = state_distance or {}
        self.min_score = min_score
        self.recent_window = recent_window
        self.decay_base = decay_base
        self.recent_change_bonus = recent_change_bonus

    def retrieve(
        self,
        state: TemporalState,
        changed_entities: List[str],
        max_agents: int = 64,
    ) -> List[RetrievedContext]:
        contexts: Dict[str, RetrievedContext] = {}
        for changed_id in changed_entities:
            changed_magnitude = self._change_magnitude(state, changed_id)
            changed_state = state.states.get(changed_id)
            for edge in self.graph.incident_edges(changed_id):
                if self._transport_blocked(edge, changed_id, changed_state.state if changed_state else ""):
                    continue
                candidate = edge.target_id if edge.source_id == changed_id else edge.source_id
                if candidate not in self.graph.entities or candidate == changed_id:
                    continue
                edge_weight = self._edge_weight(edge)
                rounds_unchanged = self._rounds_unchanged(state, candidate)
                decay = self.decay_base ** rounds_unchanged
                recent_changes = self._recent_changes(state, candidate)
                score = edge_weight * decay * changed_magnitude
                score += recent_changes * self.recent_change_bonus
                current = contexts.setdefault(candidate, RetrievedContext(entity_id=candidate, score=0.0))
                current.score += score
                current.edges.append(edge)
                current.changed_neighbors.append(changed_id)
                current.rules.extend(self.registry.candidate_rules_for_edge(edge))
                current.score_details["edge_weight_sum"] = current.score_details.get("edge_weight_sum", 0.0) + edge_weight
                current.score_details["decay_sum"] = current.score_details.get("decay_sum", 0.0) + decay
                current.score_details["changed_magnitude_sum"] = current.score_details.get("changed_magnitude_sum", 0.0) + changed_magnitude
                current.score_details["recent_changes"] = float(recent_changes)

        for context in contexts.values():
            unique_neighbors = sorted(set(context.changed_neighbors))
            signals = compute_signals(state, context.entity_id, unique_neighbors, context.edges)
            context.changed_neighbors = unique_neighbors
            context.conflict = build_conflict_report(signals)

        eligible = [
            ctx for ctx in contexts.values()
            if ctx.score >= self.min_score and state.get(ctx.entity_id) is not None
        ]
        return self._select_fair(eligible, max_agents)

    @staticmethod
    def _select_fair(eligible: List[RetrievedContext], max_agents: int) -> List[RetrievedContext]:
        """Pick up to ``max_agents`` contexts without starving any one hub.

        A plain global top-N truncated by ``(-score, entity_id)`` lets a single
        high-degree hub flood the budget, and breaks score ties by entity_id —
        so a legitimate target (e.g. katG under OxyR) can be silently dropped
        just because lower-id siblings filled the list. Instead we round-robin
        across the source that woke each candidate: round 0 takes each source's
        top target, round 1 the next, etc. Within a source, order is by score.
        """
        eligible.sort(key=lambda item: (-item.score, item.entity_id))
        if len(eligible) <= max_agents:
            return eligible
        # Bucket by the SIGNAL COMBINATION that woke each candidate -- the sorted
        # tuple of its sources. So "woken by crp only", "by rpoS only", and "by
        # crp+rpoS" are three separate buckets. Round-robin across buckets then
        # gives each combination a fair share, so a hub's unique targets are not
        # starved by another hub's flood, and a multi-source candidate is not
        # mis-attributed to a single source. Within a bucket, order is by score.
        buckets: Dict[tuple, List[RetrievedContext]] = {}
        for ctx in eligible:  # score order preserved within each bucket
            key = tuple(sorted(set(ctx.changed_neighbors))) or (ctx.entity_id,)
            buckets.setdefault(key, []).append(ctx)
        pointers: Dict[tuple, int] = {key: 0 for key in buckets}
        selected: Dict[str, RetrievedContext] = {}
        while len(selected) < max_agents:
            progressed = False
            for key, queue in buckets.items():
                if pointers[key] < len(queue):
                    ctx = queue[pointers[key]]
                    pointers[key] += 1
                    if ctx.entity_id not in selected:
                        selected[ctx.entity_id] = ctx
                        progressed = True
                        if len(selected) >= max_agents:
                            break
                    else:
                        progressed = True
            if not progressed:
                break
        return sorted(selected.values(), key=lambda item: (-item.score, item.entity_id))

    def _edge_weight(self, edge: Edge) -> float:
        """Retrieval weight for an edge.

        Relation type sets the base weight (configs/edge_weights.yaml). When an
        edge carries its own confidence (``edge_weight`` column, e.g. STRING
        score-derived), we scale the relation-type weight by it so a
        high-confidence physical interaction wakes its neighbour strongly while
        a weak association barely registers. Unknown relations fall back to a
        small non-zero weight so the signal still propagates for the LLM.
        """
        base = float(self.edge_weights.get(edge.relation_type, 0.1))
        if edge.edge_weight and edge.edge_weight > 0:
            # edge.edge_weight is a 0..1 confidence; blend so confidence
            # modulates but never fully zeroes a known relation.
            return base * edge.edge_weight
        return base

    def _recent_changes(self, state: TemporalState, entity_id: str) -> int:
        cutoff = max(0, state.current_round - self.recent_window)
        return sum(
            1 for item in state.history.get(entity_id, [])
            if item.get("changed") and item.get("round", 0) >= cutoff
        )

    def _rounds_unchanged(self, state: TemporalState, entity_id: str) -> int:
        changed_rounds = [
            item.get("round", 0)
            for item in state.history.get(entity_id, [])
            if item.get("changed")
        ]
        if not changed_rounds:
            return state.current_round
        return max(0, state.current_round - max(changed_rounds))

    def _change_magnitude(self, state: TemporalState, entity_id: str) -> float:
        history = state.history.get(entity_id, [])
        changed = [item for item in history if item.get("changed")]
        if not changed:
            return 1.0
        current = changed[-1]
        previous_state = ""
        previous_abundance = ""
        for item in reversed(history):
            if item.get("round", 0) < current.get("round", 0):
                previous_state = item.get("state", "")
                previous_abundance = item.get("abundance_label", "")
                break
        before = previous_state or previous_abundance
        after = current.get("state") or current.get("abundance_label")
        if not before or not after or before == after:
            return 1.0
        return float(
            self.state_distance.get(before, {}).get(
                after,
                self.state_distance.get("default", 1.0),
            )
        )

    @staticmethod
    def _transport_blocked(edge: Edge, changed_id: str, changed_state: str) -> bool:
        if edge.relation_type != "transports":
            return False
        transporter_is_source = edge.source_id == changed_id
        if not transporter_is_source:
            return False
        return changed_state in {"inhibited", "degraded", "disrupted"}
