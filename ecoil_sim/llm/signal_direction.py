"""Conflict detection between incoming regulation signals.

When a candidate agent is awakened with multiple changed neighbors, the
simulator needs to know whether those signals push the agent in the same
direction (no conflict, mock fallback can handle it) or in opposing
directions (conflict, only the LLM can reason about which one wins).

Direction of a single signal
----------------------------

Each (neighbor, edge) pair maps to one of the following "directions" the
neighbor pushes the candidate agent:

    up     the candidate's activity / abundance should rise
    down   the candidate's activity / abundance should fall
    abundance_up   the candidate's abundance should rise (e.g. encodes from an expressed gene)
    abundance_down the candidate's abundance should fall
    unknown       relation does not encode a clear direction

A conflict exists when the candidate receives at least one "up" and at
least one "down" direction from the changed neighbors. Two "up" signals
are not a conflict (they agree); two "abundance" signals are not a
conflict with "up" / "down" either (they act on a different axis).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Sequence, Set

from ecoil_sim.models import Edge
from ecoil_sim.state import TemporalState


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
class Signal:
    source: str
    relation_type: str
    direction: str        # up / down / abundance_up / abundance_down / unknown
    source_state: str
    note: str = ""

    def to_dict(self) -> Dict:
        return {
            "source": self.source,
            "relation_type": self.relation_type,
            "direction": self.direction,
            "source_state": self.source_state,
            "note": self.note,
        }


@dataclass
class ConflictReport:
    signals: List[Signal]
    conflict: bool
    axis_summary: Dict[str, int]
    hint: str = ""

    def to_dict(self) -> Dict:
        return {
            "signals": [signal.to_dict() for signal in self.signals],
            "conflict": self.conflict,
            "axis_summary": dict(self.axis_summary),
            "hint": self.hint,
        }


def compute_signals(
    state: TemporalState,
    entity_id: str,
    changed_neighbors: Sequence[str],
    edges: Sequence[Edge],
) -> List[Signal]:
    """Compute the direction that each changed neighbor pushes ``entity_id``."""
    signals: List[Signal] = []
    neighbor_states = {neighbor: state.states.get(neighbor) for neighbor in changed_neighbors}
    for edge in edges:
        if edge.relation_type == "transports":
            continue
        source_id = edge.source_id
        target_id = edge.target_id
        if source_id not in neighbor_states and target_id not in neighbor_states:
            continue
        if source_id == entity_id:
            neighbor_id = target_id
        elif target_id == entity_id:
            neighbor_id = source_id
        else:
            continue
        neighbor_state = neighbor_states.get(neighbor_id)
        if not neighbor_state:
            continue
        direction, note = _direction_for(edge.relation_type, neighbor_state.state, neighbor_state.abundance_label)
        signals.append(
            Signal(
                source=neighbor_id,
                relation_type=edge.relation_type,
                direction=direction,
                source_state=neighbor_state.state or neighbor_state.abundance_label or "",
                note=note,
            )
        )
    return signals


def build_conflict_report(signals: List[Signal]) -> ConflictReport:
    """Aggregate signals into a direction summary and decide whether they conflict."""
    axis_summary: Dict[str, int] = {}
    for signal in signals:
        axis_summary[signal.direction] = axis_summary.get(signal.direction, 0) + 1
    has_up = (axis_summary.get("up", 0) or 0) > 0
    has_down = (axis_summary.get("down", 0) or 0) > 0
    has_abundance_up = (axis_summary.get("abundance_up", 0) or 0) > 0
    has_abundance_down = (axis_summary.get("abundance_down", 0) or 0) > 0
    abundance_conflict = has_abundance_up and has_abundance_down
    state_conflict = has_up and has_down
    conflict = state_conflict or abundance_conflict
    hint = _make_hint(signals, axis_summary, conflict) if conflict else ""
    return ConflictReport(signals=signals, conflict=conflict, axis_summary=axis_summary, hint=hint)


def _direction_for(relation_type: str, state: str, abundance: str) -> tuple[str, str]:
    if not state and not abundance:
        return ("unknown", "no_state")
    is_active = state in _ACTIVE_STATES
    is_inactive = state in _INACTIVE_STATES
    is_high_abundance = abundance in {"high", "medium"}
    is_low_abundance = abundance in {"low", "absent"}
    if relation_type == "represses":
        if is_active:
            return ("down", "repressor_active_pushes_down")
        if is_inactive:
            return ("up", "repression_released")
    if relation_type in {"activates", "increases_activity_of"}:
        if is_active:
            return ("up", "activator_active_pushes_up")
        if is_inactive:
            return ("down", "activator_lost_pushes_down")
    if relation_type in {"encodes", "transcribed_as"}:
        # encodes: gene -> protein abundance; transcribed_as: gene -> RNA abundance.
        if is_active or is_high_abundance:
            return ("abundance_up", "gene_active_pushes_abundance_up")
        if is_inactive or is_low_abundance:
            return ("abundance_down", "gene_low_pushes_abundance_down")
    if relation_type in {"is_product_of", "produces"}:
        if is_active or is_high_abundance:
            return ("abundance_up", "producer_active_pushes_abundance_up")
        if is_inactive or is_low_abundance:
            return ("abundance_down", "producer_lost_pushes_abundance_down")
    if relation_type in {"is_substrate_of", "consumes"}:
        if is_active or is_high_abundance:
            return ("abundance_down", "consumer_active_drains_substrate")
        if is_inactive or is_low_abundance:
            return ("abundance_up", "consumer_lost_substrate_rises")
    return ("unknown", f"relation_{relation_type}_not_decoded")


def _make_hint(signals: List[Signal], axis_summary: Dict[str, int], conflict: bool) -> str:
    if not conflict:
        return ""
    if axis_summary.get("up", 0) and axis_summary.get("down", 0):
        upstream_repressors = [s for s in signals if s.relation_type == "represses"]
        upstream_activators = [s for s in signals if s.relation_type in {"activates", "increases_activity_of"}]
        if upstream_repressors and upstream_activators:
            return (
                "你同时收到抑制解除信号和激活减弱信号。\n"
                "读你的功能注释（annotation），判断在当前条件下哪个调控的净效果更主导。"
            )
    if axis_summary.get("abundance_up", 0) and axis_summary.get("abundance_down", 0):
        return (
            "你同时收到丰度上升和丰度下降的信号。\n"
            "读你的功能注释（annotation），判断合成与降解哪个在当前条件下更主导。"
        )
    if axis_summary.get("up", 0) >= 2:
        return (
            "你收到多个同向激活信号来自不同上游。\n"
            "读你的功能注释（annotation），判断这些信号是叠加增强、还是已经饱和。"
        )
    if axis_summary.get("down", 0) >= 2:
        return (
            "你收到多个同向抑制信号来自不同上游。\n"
            "读你的功能注释（annotation），判断是协同抑制、还是其中一个只是次要信号。"
        )
    return (
        "你的上游调控因子发出了方向不完全一致的信号。\n"
        "读你的功能注释（annotation），决定净方向。"
    )
