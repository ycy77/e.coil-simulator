# E.coil — Diagnostic-Grade Intracellular Multi-Agent Simulator

This project turns the *E. coli* knowledge graph into a runtime
where each biological entity — gene, protein, complex, reaction, RNA,
metabolite, drug — is a local **Agent**. The Agents wake up when a
neighbour's state changes, see only the signal that propagated to them,
and decide what to do next with a language model (or a deterministic
mock). The result is a perturbation-replayable, biologically explainable
simulation that doubles as a data-quality diagnostic for the underlying
graph.

This README is the entry point for a new human or a new AI. Every
other document in `docs/` assumes you have read this one.

## What this project is

* A **strict simulator** for *E. coli* intracellular dynamics.
  Each entity is an Agent that only sees its local neighbourhood.
* A **vLLM audit pipeline** that classifies every entity (endogenous,
  exogenous-drug, class-abstraction, etc.) using the local Qwen3.5-9B
  model served on `http://127.0.0.1:8000`.
* A **canonicalization pipeline** that deduplicates the 24,369-row
  knowledge graph by cross-source family keys, writes unique
  `display_name`s, and surfaces an `is_exogenous` flag derived from
  the audit.
* A **diagnostic UI** (FastAPI + Vue 2 + vis-network) for graph
  inspection, name-collision review, and per-entity timeline.
* A **simulation control surface** (initial conditions, perturbations,
  phenotypes, run history) built on top of the same graph.

## What this project is *not*

* Not a metabolic FBA solver — that lives in the raw EcoCyc flat
  files we deliberately trimmed.
* Not a wet-lab pipeline. The data is *in-silico* knowledge.
* Not a generic biology foundation model. The LLM only audits entities
  and reasons inside one perturbation at a time.

## Quick start (auditor / data engineer)

```bash
# 1. Make sure vLLM is up.
scripts/start_vllm.sh --gpus 2 --devices 6,7 --port 8000 &

# 2. Audit every entity (strict, no fallback).
python scripts/audit_entities.py --apply \
    --vllm-url http://127.0.0.1:8000 --concurrency 96

# 3. Canonicalize based on the audit + cross-source rules.
python scripts/canonicalize_v2.py            # writes data/normalized/_v2/
python scripts/canonicalize_v2.py --apply-in-place   # promotes to normalized/

# 4. Re-enrich with the canonical map.
python scripts/enrich_entities_v2.py --apply-in-place

# 5. Verify invariants (must exit 0).
python scripts/verify_uniqueness.py --strict
```

## Quick start (interactive diagnostic UI)

```bash
bash web/start.sh
# backend:  http://127.0.0.1:28932/api/health
# frontend: http://127.0.0.1:40211/
```

The diagnostic UI consumes `data/normalized/entities.csv`,
`data/normalized/edges.csv`, and `data/enriched/entities_enriched_v2_lite.jsonl`.

## Repository layout

```
data/
  normalized/              # canonical graph (post-canonicalize_v2)
  enriched/                # LLM-friendly entity cards
  raw/                     # trimmed EcoCyc / KEGG / NCBI / UniProt / RegulonDB snapshots
  initial_conditions/      # glucose_log_phase.yaml + LLM-drafted variants
  perturbations/           # natural-language perturbation library
  phenotypes/              # L0 / L1 / L2 / L3 phenotype expectations
  registry/                # rule_registry / native_rules.jsonl
  audit/                   # vLLM decisions + ambiguous samples + reports

docs/
  PROJECT_OVERVIEW.md
  ARCHITECTURE.md
  DATA_DICTIONARY.md
  ECOCYC_INGEST.md
  SIMULATION.md
  LLM_PROMPTS.md
  DIAGNOSTIC_UI.md
  AUDIT_AND_CURATION.md
  inventory/               # file / metric snapshots
  CHANGELOG.md

ecoil_sim/
  agents/                  # prompt builder, mock LLM
  llm/                     # async vLLM client, name resolver
  graph/                   # entity / edge / pathway models
  sim/                     # SimulationEngine, perturbation, enriched service
  registry/                # rule registry loader
  report/                  # stage reporter
  retrieval/               # temporal graph-RAG
  rules/                   # native rule evaluator
  storage/                 # simulation_store (round jsonl)
  state/                   # AgentState, initial conditions
  validation/              # ActionValidator
  actions/                 # ActionInterpreter

web/
  backend/                 # FastAPI diagnostic
  frontend/                # Vue 2 + vis-network
  start.sh                 # one-shot launcher

scripts/
  fetch_ecocyc_flatfiles.py
  parse_ecocyc.py
  build_entities.py
  build_edges.py
  build_ncbi_entities.py
  build_regulondb_edges.py
  build_pathways.py
  build_rule_registry.py
  canonicalize_normalized.py    # first-gen, small-molecule only
  canonicalize_v2.py            # second-gen, full graph
  enrich_entities.py            # first-gen
  enrich_entities_v2.py         # second-gen, multi-source
  audit_entities.py             # vLLM strict auditor
  verify_uniqueness.py          # invariant checker
  clean_apple_double.py         # macOS _* stripper
  clean_workspace.py            # bulk workspace cleaner
  test_offline_iteration.py     # offline regression
  eval_baseline.py              # L0/L1/L2/L3 eval harness

prompts/
  agent_decision.system.md

schemas/                       # action / state schemas

runs/                          # simulation run history (timestamped dirs)
```

## Hard rules (do not violate)

1. **No silent fallback in audits.** If vLLM is unreachable, the audit
   script exits with code 2 and prints the failing entity_id. Never
   route through mock / rule_only to "make progress".
2. **Every entity gets a stable `family_key`.** Two entities with the
   same `(entity_type, family_key)` are merged; two entities with the
   same name but different `family_key` get a stable source-id suffix
   on `display_name`.
3. **Edges are always between canonical ids.** `rewrite_edges` enforces
   this; orphan edges are reported, not silently dropped.
4. **No `._*` files in the repo.** `scripts/clean_apple_double.py` is
   part of CI.
5. **No raw EcoCyc binaries under git.** OWL/FASTA/wc-model-29.0/29.1
   are stripped; only the 10 flat files actually consumed by
   `parse_ecocyc.py` remain.

## Where to read next

* `docs/VALIDATION_SUMMARY.md` — what is validated against external standards
  (RegulonDB 94.4% strong recall / 100% sign; co-expression; literature patterns),
  with current numbers and the honest remaining gap.
* `docs/REMOTE_WORK_PLAN.md` — the forward plan for the agent working on
  the vLLM host: measure decisions → improve them → scale → cell-rule quality.
* `docs/PROJECT_OVERVIEW.md` — one-paragraph recap of the simulation
  semantics, agent model, and design constraints.
* `docs/ARCHITECTURE.md` — module map and data flow.
* `docs/AUDIT_AND_CURATION.md` — how the vLLM audit is structured,
  what each decision field means, and how `is_exogenous` is derived.
* `docs/DATA_DICTIONARY.md` — every column in every CSV / JSONL.

## License

Internal research code. No public licence attached.