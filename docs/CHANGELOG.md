# Changelog

Each entry is signed "session-N" so future contributors can diff
chunks at a glance.

## session-2026-06-13 — runnability fixes + engine↔baseline reconciliation

### Fixed (foundation — the project did not run out of the box)
* `requirements.txt` added (was missing). Core: PyYAML + httpx; web:
  fastapi + uvicorn; tests: pytest.
* `ecoil_sim/config.py` — `load_yaml_like` previously fell back to a
  hand-rolled mini-parser when PyYAML was absent, which silently
  *corrupted* nested config (block scalars, flow maps, lists became
  garbage; e.g. `expected_states: {}` parsed to the string `"{}"`,
  crashing the reporter). PyYAML is now a hard dependency and config
  loading fails loudly — in line with the #1 hard rule (no silent
  fallback).
* `ecoil_sim/report/reporter.py` — `_response_pattern_match` guards
  non-dict `expected_states`.
* `ecoil_sim/llm/response_parser.py` — truncated-JSON recovery rewritten.
  The old `rfind("{")` grabbed an inner action fragment and dropped the
  whole decision; now we balance brackets from the *outer* wrapper and
  drop only a dangling partial element. This is the #1 vLLM failure mode
  at high concurrency with small `decision_max_tokens`.

### Changed (cell rules — use the curated, STRING-dense baseline)
* `configs/simulation.yaml` — simulator now runs on
  `data/normalized/simulation` + `data/registry/simulation` (the curated
  baseline: endogenous-only, STRING PPIs integrated, reactions folded
  into produces/consumes). Density 4.6 edges/entity vs 1.9; isolated
  nodes 2% vs 20%; STRING was previously absent from the simulated graph.
* Engine now understands the baseline relation vocabulary
  (`interacts`, `produces`, `consumes`, `transcribed_as`, `paralog_of`,
  `bound_by`) across `configs/edge_weights.yaml`,
  `ecoil_sim/llm/signal_direction.py`, `configs/fallback_rules.yaml`,
  `ecoil_sim/agents/prompt_builder.py` (decision_policy), and
  `scripts/build_rule_registry.py`. Previously these 6 relation types
  (53% of baseline edges, all STRING PPIs) got a flat 0.1 noise weight.
* `ecoil_sim/models.py::Edge` now loads per-edge `edge_weight`
  (STRING confidence) + `string_channel`; `TemporalGraphRAG` scales the
  relation-type weight by per-edge confidence so a high-confidence PPI
  wakes its partner strongly and a weak one barely registers.
* PPI relations (`interacts`, `paralog_of`, `bound_by`) deliberately have
  NO deterministic fallback: a physical interaction carries no fixed
  direction, so the LLM is the sole decision-maker (decisions to the
  model; rules to the cell).

### Added
* `tests/test_engine_integration.py` — end-to-end lac-operon derepression
  on the baseline + glucose-log-phase profile, and a negative control.
* `tests/test_retrieval_ppi.py` — STRING PPI partners are woken on
  perturbation, with retrieval scores modulated by STRING confidence.
* `data/registry/simulation/native_rules.jsonl` — rule registry rebuilt
  from the baseline edges (49,742 rules).

## session-2026-06-10 — workspace governance + vLLM audit pipeline

### Added
* `scripts/audit_entities.py` — strict vLLM audit. 24,369 entities
  classified as `endogenous` / `exogenous-drug` / `exogenous-chemical`
  / `class-abstraction` / `unsure`. Auto-detects the served model
  from `/v1/models`. Supports `--concurrency N` and `--resume`.
  Refuses to silently fall back to mock / rules.
* `scripts/canonicalize_v2.py` — full-graph canonicalizer. Derives
  `family_key` from UniProt accession / EC number / KEGG compound id /
  complex components set / gene alias set; merges duplicate rows;
  rewrites edges; writes a globally-unique `display_name`; populates
  `is_exogenous` from the audit; outputs to `data/normalized/_v2/`
  with `--apply-in-place` promotion.
* `scripts/enrich_entities_v2.py` — multi-source enriched card
  builder. Walks every cross-source row listed in `merged_from`;
  unions annotations, aliases, external_ids; emits a richer summary
  than `enrich_entities.py` did.
* `scripts/verify_uniqueness.py` — invariant gate. Exit 1 on duplicate
  `entity_id`, duplicate `(entity_type, name)`, orphan edges, or
  enriched card missing canonical entity.
* `docs/PROJECT_OVERVIEW.md`, `docs/ARCHITECTURE.md`,
  `docs/DATA_DICTIONARY.md`, `docs/AUDIT_AND_CURATION.md`,
  `docs/ECOCYC_INGEST.md`, `docs/SIMULATION.md`,
  `docs/LLM_PROMPTS.md`, `docs/DIAGNOSTIC_UI.md`, this changelog.
* `docs/inventory/` — file / metric snapshots.

### Changed
* `README.md` rewritten as the single entry point. Old
  `docs/architecture.md` moved to `docs/architecture.legacy.md`.
* `web/frontend/src/components/SubgraphView.vue`:
  * default hop is now `1` (was `2`)
  * added per-mount request-sequence guard so an in-flight
    `/subgraph` response cannot overwrite a newer selection
  * explicit `redraw()` + `fit()` after `setData()` to defeat
    vis-network's internal cache.
* `web/backend/graph_service.py`:
  * `subgraph()` now bounds the BFS by hop distance instead of
    truncating by lexicographic id order
  * dedupes edges by `(source, relation, target, source_db,
    source_record_id)`

### Removed
* `data/raw/ecocyc/extracted/29.6/data/biopax-level2.owl` (74M)
* `data/raw/ecocyc/extracted/29.6/data/biopax-level3.owl` (71M)
* `data/raw/ecocyc/extracted/29.6/data/ecoli-COLI-K12-3659364498.fsa` (4.5M)
* `data/raw/ecocyc/extracted/29.6/data/dnaseq.fsa` (4.6M)
* `data/raw/ecocyc/extracted/29.6/data/protseq.fsa` (1.9M)
* `data/raw/ecocyc/extracted/29.6/data/{kb,fba,moleculardiagrams,reports,rawdata,input}/` (~250M)
* `data/raw/ecocyc/extracted/29.6/data/wc-model-29.0/`, `wc-model-29.1/` (16M)
* `data/raw/ecocyc/extracted/29.6/data/*.dat/.col/.gaf` files not consumed by
  `scripts/parse_ecocyc.py` (~100M across 23 files; the 10
  `.dat/.col` files that `parse_ecocyc.py` actually reads are kept)
* `data/raw/ecocyc/extracted/ecoli.tar.gz`
* `data/normalized/*.pre_canonical`, `*.pre_ecocyc` (26M)
* `scripts/__pycache__/`

### Invariants enforced (verify with `python scripts/verify_uniqueness.py --strict`)
* `entity_id` is unique
* `(entity_type, name)` is unique
* `display_name` is unique
* `family_key` is unique within `(entity_type,)`
* every edge source/target resolves to an entity or pathway id
* every enriched card maps to an entity id

## session-2026-06-09 — first diagnostic UI + initial conditions

* Stand up FastAPI + Vue 2 + vis-network on ports 28932 / 40211.
* `web/frontend/src/components/{EntitySearch,SubgraphView,EntityDetail,RunTimeline,DuplicateReport}.vue`.
* `web/backend/{data_loader,graph_service,run_service,enriched_loader}.py`.
* `data/enriched/entities_enriched.jsonl`, `entities_enriched_lite.jsonl`.
* `data/initial_conditions/glucose_log_phase.yaml`.

## session-2026-06-08 — first simulation loop

* `ecoil_sim/{agents,llm,graph,sim,registry,report,retrieval,rules,storage,state,validation,actions}/`.
* `scripts/parse_ecocyc.py`, `scripts/build_*.py`.
* `data/normalized/{entities,edges,pathways,canonical_entity_map,canonicalization_report}.csv/json`.
* `data/registry/native_rules.jsonl`.