"""LLM-driven perturbation intake.

Turns a free-text request or an uploaded file ("add 2 mg/L ciprofloxacin",
"knock out recA and shift to anaerobic") into canonical graph entry points the
simulation engine can run from. The biology -- which drug hits which target,
which gene a sloppy name refers to -- is the LLM's job; this module only
orchestrates and applies deterministic safety guards. There is no hand-written
drug->target table (decisions to the model).

Pipeline
--------
1. **extract** (LLM): pull perturbation intents from the text, including, for an
   exogenous agent, the likely molecular target *concept* (e.g. ciprofloxacin ->
   "DNA gyrase").
2. **ground** (deterministic): :class:`EntityGrounder` retrieves candidate
   entities for each mention/concept from the graph + perturbagen catalog.
3. **resolve** (LLM, guided_json): given the text + candidate lists, the model
   emits structured perturbations (entity_id + target_state + evidence) chosen
   from the candidates, plus an ``unresolved`` list for anything it can't ground.
4. **validate** (deterministic): drop/flag any entity_id not in the graph or any
   target_state outside that entity's allowed_states -- the LLM proposes, the
   guards keep it honest.

The result is a :class:`PerturbationProposal` meant to be shown to the user for
confirmation (judgment to humans) before it drives a run.

The LLM is injected as a ``complete(system, user, guided_json) -> str`` callable
so the orchestration and guards are unit-testable offline with a stub; the real
vLLM call lives in :class:`VLLMJsonCompleter` (used on the GPU host).
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Dict, List, Optional

from ecoil_sim.graph import StaticGraph
from ecoil_sim.llm.response_parser import parse_llm_output
from ecoil_sim.sim.grounding import Candidate, EntityGrounder

CompleteFn = Callable[[str, str, Optional[dict]], str]


@dataclass
class GroundedPerturbation:
    entity_id: str
    target_state: str
    agent_mention: str
    agent_kind: str = "endogenous"
    evidence: str = ""
    confidence: float = 0.0
    reason: str = ""

    def to_engine_change(self) -> Dict:
        return {
            "entity_id": self.entity_id,
            "state": self.target_state,
            "source": "llm_inference",
            "input_source": "llm_perturbation",
            "reason": self.reason or f"grounded from '{self.agent_mention}'",
        }


@dataclass
class PerturbationProposal:
    perturbations: List[GroundedPerturbation] = field(default_factory=list)
    unresolved: List[Dict] = field(default_factory=list)

    def to_engine_changes(self) -> List[Dict]:
        return [p.to_engine_change() for p in self.perturbations]

    def render(self) -> str:
        """Human-readable confirmation block (shown before a run)."""
        lines = ["Proposed perturbation entry points (please confirm):", ""]
        if not self.perturbations:
            lines.append("  (none grounded)")
        for p in self.perturbations:
            lines.append(
                f"  • {p.entity_id} -> {p.target_state}  [{p.agent_kind}, conf={p.confidence:.2f}]"
            )
            lines.append(f"      from: \"{p.agent_mention}\"")
            if p.evidence:
                lines.append(f"      evidence: {p.evidence}")
        if self.unresolved:
            lines.append("")
            lines.append("Unresolved (need human input):")
            for u in self.unresolved:
                lines.append(f"  • {u.get('mention','?')} — {u.get('reason','')}")
        return "\n".join(lines)


# Intent-extraction schema (pass 1). Kept small; guided_json-friendly.
INTENT_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": ["intents"],
    "properties": {
        "intents": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["mention", "kind"],
                "properties": {
                    "mention": {"type": "string"},
                    "kind": {"type": "string"},
                    "target_concepts": {"type": "array", "items": {"type": "string"}},
                    "dose": {"type": "string"},
                },
            },
        }
    },
}


class LLMPerturbationParser:
    def __init__(
        self,
        graph: StaticGraph,
        grounder: EntityGrounder,
        complete: CompleteFn,
        *,
        prompts_dir: Path,
        intake_schema: Optional[dict] = None,
        candidates_per_mention: int = 8,
    ) -> None:
        self.graph = graph
        self.grounder = grounder
        self.complete = complete
        self.prompts_dir = Path(prompts_dir)
        self.intake_schema = intake_schema
        self.candidates_per_mention = candidates_per_mention

    # -- input adapters ----------------------------------------------------- #
    def parse_text(self, text: str) -> PerturbationProposal:
        intents = self._extract_intents(text)
        candidate_map = self._ground_intents(intents)
        proposal = self._resolve(text, intents, candidate_map)
        return self._validate(proposal)

    def parse_file(self, path: Path) -> PerturbationProposal:
        return self.parse_text(Path(path).read_text(encoding="utf-8"))

    # -- pipeline stages ---------------------------------------------------- #
    def _extract_intents(self, text: str) -> List[Dict]:
        system = self._prompt("perturbation_parse.system.md")
        raw = self.complete(system, text, INTENT_SCHEMA)
        parsed, _ = parse_llm_output(raw)
        intents = parsed.get("intents", [])
        return [i for i in intents if isinstance(i, dict) and i.get("mention")]

    def _ground_intents(self, intents: List[Dict]) -> Dict[str, List[Candidate]]:
        """For each mention (and any LLM-proposed target concept), retrieve
        candidate entities. Drug names rarely match endogenous entities, so the
        target concepts the model proposes are what ground to real targets."""
        out: Dict[str, List[Candidate]] = {}
        for intent in intents:
            queries = [intent.get("mention", "")]
            queries += [c for c in intent.get("target_concepts", []) if c]
            seen: Dict[str, Candidate] = {}
            for q in queries:
                for cand in self.grounder.candidates(q, limit=self.candidates_per_mention):
                    if cand.entity_id not in seen or cand.score > seen[cand.entity_id].score:
                        seen[cand.entity_id] = cand
            ranked = sorted(seen.values(), key=lambda c: (-c.score, c.entity_id))
            out[intent.get("mention", "")] = ranked[: self.candidates_per_mention]
        return out

    def _resolve(self, text: str, intents: List[Dict], candidate_map: Dict[str, List[Candidate]]) -> PerturbationProposal:
        system = self._prompt("perturbation_ground.system.md")
        user = json.dumps(
            {
                "request": text,
                "intents": intents,
                "candidates": {
                    mention: [c.to_dict() for c in cands]
                    for mention, cands in candidate_map.items()
                },
            },
            ensure_ascii=False,
        )
        raw = self.complete(system, user, self.intake_schema)
        parsed, _ = parse_llm_output(raw)
        return _proposal_from_dict(parsed)

    def _validate(self, proposal: PerturbationProposal) -> PerturbationProposal:
        """Deterministic guards on the LLM's choices."""
        kept: List[GroundedPerturbation] = []
        for p in proposal.perturbations:
            entity = self.graph.entities.get(p.entity_id)
            if entity is None:
                proposal.unresolved.append(
                    {"mention": p.agent_mention, "reason": f"entity_id not in graph: {p.entity_id}"}
                )
                continue
            if entity.allowed_states and p.target_state not in entity.allowed_states:
                proposal.unresolved.append(
                    {
                        "mention": p.agent_mention,
                        "reason": f"target_state '{p.target_state}' not in allowed_states of {p.entity_id} "
                        f"({'|'.join(entity.allowed_states)})",
                    }
                )
                continue
            kept.append(p)
        proposal.perturbations = kept
        return proposal

    def _prompt(self, name: str) -> str:
        path = self.prompts_dir / name
        return path.read_text(encoding="utf-8") if path.exists() else ""


def _proposal_from_dict(data: Dict) -> PerturbationProposal:
    proposal = PerturbationProposal()
    for item in data.get("perturbations", []) or []:
        if not isinstance(item, dict) or not item.get("entity_id"):
            continue
        proposal.perturbations.append(
            GroundedPerturbation(
                entity_id=item.get("entity_id", ""),
                target_state=item.get("target_state", ""),
                agent_mention=item.get("agent_mention", ""),
                agent_kind=item.get("agent_kind", "endogenous"),
                evidence=item.get("evidence", ""),
                confidence=float(item.get("confidence", 0.0) or 0.0),
                reason=item.get("reason", ""),
            )
        )
    for item in data.get("unresolved", []) or []:
        if isinstance(item, dict) and item.get("mention"):
            proposal.unresolved.append({"mention": item["mention"], "reason": item.get("reason", "")})
    return proposal


class VLLMJsonCompleter:
    """Real ``complete`` callable backed by the vLLM OpenAI endpoint.

    GPU-host only (the laptop cannot reach the endpoint). Sends ``guided_json``
    at the top level so the model is constrained to the intake schema.
    """

    def __init__(self, base_url: str, model: str, api_key: str = "EMPTY",
                 temperature: float = 0.1, max_tokens: int = 1024, timeout: float = 120.0):
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.api_key = api_key
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout

    def __call__(self, system: str, user: str, guided_json: Optional[dict]) -> str:
        import httpx

        payload: Dict = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "chat_template_kwargs": {"enable_thinking": False},
        }
        if guided_json:
            payload["guided_json"] = guided_json
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        with httpx.Client(timeout=self.timeout) as client:
            resp = client.post(f"{self.base_url}/chat/completions", json=payload, headers=headers)
            resp.raise_for_status()
            return resp.json().get("choices", [{}])[0].get("message", {}).get("content") or ""
