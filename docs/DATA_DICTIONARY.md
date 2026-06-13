# Data Dictionary

Every file under `data/` that is consumed by the simulator or the
diagnostic UI. Column types are positional; semantic types are
written in the description.

## `data/normalized/entities.csv`

One row per canonical entity, after `canonicalize_v2.py`. Schema
fields, in order:

| Column | Type | Description |
|---|---|---|
| `entity_id` | string | Stable canonical id. Primary key. |
| `entity_type` | enum | `gene` / `protein` / `complex` / `reaction` / `small_molecule` / `rna`. |
| `name` | string | Original EcoCyc/UniProt/KEGG name. May collide across sources. |
| `aliases` | pipe-list | Other names, deduplicated. |
| `default_state` | string | Initial state in `glucose_log_phase.yaml`. |
| `allowed_states` | pipe-list | States the Agent can be in. |
| `annotation` | string | Best annotation after multi-source merge (longest informative wins). |
| `pathways` | pipe-list | Pathway memberships. |
| `subcellular_location` | string | Best location string. |
| `source_database` | pipe-list | Source databases that contributed to this canonical row. |
| `source_id` | string | Primary source_id (the highest-priority source wins). |
| `external_ids` | pipe-list | Union of every external id from the merged rows. |
| `is_external` | string | Legacy EcoCyc "external" flag. Preserved for back-compat. |
| `is_exogenous` | bool-string | `true` / `false` / `unsure`. From vLLM audit. |
| `family_key` | string | Stable cross-source family identifier. The dedupe key. |
| `display_name` | string | Unique, human-readable. Globally unique across the catalog. |
| `merged_from` | pipe-list | Original `entity_id`s merged into this canonical row. |
| `complex_type` | string | EcoCyc complex class (e.g. `TRANSPORT`). |
| `is_virtual` | string | EcoCyc virtual-entity flag. |
| `components` | pipe-list | For `entity_type=complex`. Drives `family_key` derivation. |
| `critical_components` | pipe-list | Required components for assembly. |
| `assembly_condition` | string | Conditions required for the complex to form. |
| `notes` | string | Merged notes from every source row. |

## `data/normalized/edges.csv`

| Column | Type | Description |
|---|---|---|
| `source_id` | entity_id | Must exist in `entities.csv` after `canonicalize_v2`. |
| `relation_type` | enum | `encodes` / `activates` / `represses` / `inhibits` / `binds` / `catalyzes` / `is_substrate_of` / `is_product_of` / `is_component_of` / `participates_in` / `transports`. |
| `target_id` | entity_id or pathway_id | Canonical entity id, or pathway id if `relation_type=participates_in`. |
| `direction` | enum | `directed` / `undirected` / `both`. |
| `evidence` | enum | `confirmed` / `strong` / `database` / `curated` / `weak`. |
| `source_database` | pipe-list | Source DBs that reported this edge. |
| `source_record_id` | pipe-list | Provenance record ids. |
| `notes` | string | Free-form notes merged from each source. |

## `data/normalized/pathways.csv`

| Column | Type | Description |
|---|---|---|
| `pathway_id` | string | EcoCyc / KEGG pathway id. |
| `pathway_name` | string | Display name. |
| `source` | enum | `EcoCyc` / `KEGG`. |
| `description` | string | Long description. |
| `organism` | string | `Escherichia coli K-12 substr. MG1655`. |

## `data/enriched/entities_enriched_v2_lite.jsonl`

One JSON object per canonical entity. The **lite** file is the one
loaded by the diagnostic UI. The full file (`entities_enriched_v2.jsonl`)
holds the long-form `raw_annotations` and is consumed by the LLM
prompt builder via `EnrichedService`.

Fields:

| Field | Type | Description |
|---|---|---|
| `entity_id` | string | Canonical id. |
| `entity_type` | enum | Same as `entities.csv`. |
| `display_name` | string | Globally unique. |
| `canonical_name` | string | Pre-disambiguation name. |
| `family_key` | string | Same as `entities.csv`. |
| `summary` | string | Multi-source merged summary (1400 chars). |
| `aliases` | string-list | All merged aliases. |
| `external_ids` | string-list | All merged external ids. |
| `linked_entities` | dict | `encoded_protein`, `encoding_genes`, `catalyzes`, etc. |
| `evidence_sources` | string-list | DBs that contributed. |
| `source_databases` | string-list | Same, sorted. |
| `is_exogenous` | bool-string | From vLLM audit. |
| `quality` | dict | `raw_annotation_quality` / `enriched_summary_quality` / `enrichment_sources` / `family_key_present` / `merged_source_count`. |

## `data/audit/decisions/<type>.jsonl`

One decision per audited entity. Schema in
`scripts/audit_entities.py`:

```json
{
  "entity_id": "...",
  "entity_type": "...",
  "name": "...",
  "audit": {
    "endogenous": "endogenous|exogenous-drug|exogenous-chemical|class-abstraction|unsure",
    "name_uniqueness": "unique|collides",
    "collides_with": ["..."],
    "confidence": 0.95,
    "rationale": "...",
    "model": "/home/.../Qwen3_5-9B",
    "audit_method": "vllm",
    "raw_signals": {...}
  }
}
```

## `data/audit/ambiguous/<type>.jsonl`

Same shape as `decisions/`, but only entities whose `audit.endogenous`
is `unsure`, whose confidence is below 0.55, or whose JSON parse
failed.

## `data/normalized/_v2/`

Pre-promotion output of `canonicalize_v2.py`. `apply-in-place`
copies these into the canonical `data/normalized/` location after
backing up the originals as `*.pre_canonical_v2`.

## `data/enriched/_v2/`

Pre-promotion output of `enrich_entities_v2.py`.