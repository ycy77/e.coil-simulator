# Changelog

Each entry is signed "session-N" so future contributors can diff
chunks at a glance.

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