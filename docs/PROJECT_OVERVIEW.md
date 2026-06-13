# Project Overview

## What we are simulating

The simulation is a single *E. coli* cell. The intracellular state is
a set of `Agent`s — one per entity in the canonical knowledge graph.
When the user injects a perturbation (a small molecule at non-zero
concentration, a gene knockout, a transcription factor activation),
the scheduler walks the graph one BFS step at a time, wakes the
neighbouring Agents, and lets each Agent decide how its own state
should change.

## The agent contract

Each Agent sees **only** what propagated to it:

* its own canonical id, type, name, display name
* its current state, efficiency, and abundance
* the incoming signals (source_id, relation, new state)
* the `candidate_rules` that touch the Agent
* the local enriched annotation (`summary`, `linked_entities`)

It does **not** see:

* the original perturbation (e.g. "allolactose was added at t=0")
* the global graph topology
* any state changes that did not propagate to it

This is the same contract that real biological entities obey: *lacZ*
does not "know" that lactose was added to the medium; it only senses
that LacI left the operator.

## The audit / curation stack

The simulator is only as good as the knowledge graph. Two pipelines
keep that graph honest:

1. **vLLM audit.** `scripts/audit_entities.py` calls the local Qwen3.5-9B
   model via the OpenAI-compatible endpoint at
   `http://127.0.0.1:8000/v1/chat/completions`. Each entity is asked
   to classify itself as `endogenous`, `exogenous-drug`,
   `exogenous-chemical`, `class-abstraction`, or `unsure`, and to
   flag whether its `display_name` collides with another entity's.
   The script refuses to fall back to mock / rules when vLLM is
   unreachable.

2. **Canonicalization v2.** `scripts/canonicalize_v2.py` consumes the
   audit plus deterministic rules (UniProt accession, EC number, KEGG
   compound id, complex `components` set, etc.) to assign every entity
   a `family_key`. Entities sharing the same `(entity_type, family_key)`
   are merged; entities sharing the same `name` but different
   `family_key` get a stable source-id suffix on `display_name`.

The end state is that **the diagnostic UI never shows two nodes with
the same label**, and the simulation's initial-condition loader only
treats `is_exogenous=false` entities as part of the native cell.

## Why the Agent model is *local*

The Agent-only-knows-local-signal constraint is not a performance
choice. It is a correctness choice for the perturbation-reasoning
story we want to tell. If an Agent knew the original perturbation,
the LLM would pattern-match on the perturbation text instead of
reasoning about the propagated biology. We saw this concretely with
the LacI / CRP / lacZ conflict scenario: when the Agent knew only
that two regulators had flipped, it had to fall back on its own
annotation to decide the net effect. That is the *whole point* of the
project.

## What is in scope

* L0/L1 single-signal perturbations (mock + LLM agree)
* L2 conflict perturbations (LLM reasoning review, mock is refusal baseline)
* Endogenous graph deduplication + multi-source enrichment
* Diagnostic UI for graph / entity / run inspection
* vLLM-audited exogenous-drug tagging

## What is out of scope

* Wet-lab / experimental data ingestion
* Multi-cell or population dynamics
* Non-*E. coli* species (the entire pipeline is hardcoded to K-12
  substrate and b-numbers)
* Generic drug-discovery scoring (we only annotate, we don't predict
  binding affinity)

## Reading order for new contributors

1. `README.md` (you are here).
2. `docs/PROJECT_OVERVIEW.md` (this file).
3. `docs/ARCHITECTURE.md` — module map.
4. `docs/AUDIT_AND_CURATION.md` — how the audit pipeline works.
5. `docs/DATA_DICTIONARY.md` — every column / field.
6. `docs/SIMULATION.md` — what actually runs at runtime.
7. `docs/LLM_PROMPTS.md` — how the prompts are constructed.