# Audit and Curation

## The audit pipeline

```
   entities.csv
        │
        ▼
   scripts/audit_entities.py   (vLLM, strict, no fallback)
        │
        ▼
   data/audit/decisions/<type>.jsonl
   data/audit/ambiguous/<type>.jsonl
   data/audit/reports/<type>.report.md
        │
        ▼
   scripts/canonicalize_v2.py
        │
        ▼
   data/normalized/_v2/
```

## What `audit_entities.py` actually does

For every entity in `entities.csv` it builds a structured prompt with:

* raw signals (`name`, `aliases`, `source_database`, `source_id`,
  `external_ids`, `annotation` excerpt, `notes` excerpt,
  `default_state`, `is_external`, `in_edge_count`, `out_edge_count`,
  drug-keyword hits, enriched summary excerpt)
* the model's expected classification (`endogenous`, `exogenous-drug`,
  `exogenous-chemical`, `class-abstraction`, `unsure`)
* the model's expected `name_uniqueness` judgment with a list of
  colliding ids

It calls the local vLLM endpoint at `http://127.0.0.1:8000` via the
OpenAI-compatible `/v1/chat/completions` route, with
`response_format={"type": "json_object"}` so the reply must be JSON.
The model id is auto-detected from `/v1/models`.

### Concurrency

The script uses a `ThreadPoolExecutor`. With `--concurrency 96`, vLLM's
internal continuous-batching scheduler keeps the two A100 GPUs (TP=2)
saturated at roughly **20 entities/s**.

### Failure policy (no fallback)

* Transport / 5xx / timeout → `SystemExit(2)` with the failing
  `entity_id`.
* JSON parse error → retry once with a larger `max_tokens` budget; if
  it still fails, the entity is routed to `ambiguous/` with
  `audit_method=parse_error`.

There is **no** mock / rule-only / placeholder path. If vLLM is down,
the audit stops.

### Resume

`--resume` skips any entity_id already present in either
`decisions/<type>.jsonl` or `ambiguous/<type>.jsonl`. This is the
canonical way to recover from an interrupted run.

## What `canonicalize_v2.py` does

1. **Derives `family_key`** for each entity using deterministic rules:
   * `protein`: UniProt accession from `external_ids`
   * `complex`: SHA1 of the sorted `components` set
   * `reaction`: EC number from `external_ids` / `notes` / `annotation`
   * `small_molecule`: KEGG compound id, else CHEBI id, else name
   * `gene`: SHA1 of the sorted alias set
   * `rna`: source_id

2. **Merges** every entity that shares the same
   `(entity_type, family_key)`. The highest-priority source (UniProt
   > NCBI > KEGG > RegulonDB > EcoCyc) becomes the canonical row;
   every other row's `external_ids`, `aliases`, `annotation`,
   `notes`, `source_database` is unioned into the canonical row.

3. **Writes unique `display_name`s**: same `(entity_type, name)`
   across distinct `family_key`s get a stable source-id suffix
   (e.g. `InsAB' transposase (MONOMER0-4229 #2)`).

4. **Populates `is_exogenous`** from the vLLM audit decision:
   `exogenous-drug` / `exogenous-chemical` / `class-abstraction` →
   `true`; `endogenous` → `false`; `unsure` → `unsure`.

5. **Rewrites edges** through the canonical map. Orphan edges are
   reported, never silently dropped.

## What `enrich_entities_v2.py` does

Re-builds the per-entity card from the canonicalized row, walking
every cross-source row listed in `merged_from`. The summary is
composed from the union of:

* the primary annotation
* the merged notes
* the merged aliases
* `subcellular_location`
* incoming `represses` / `activates` neighbours
* outgoing `encodes` / `catalyzes` neighbours

The `lite` JSONL is what the UI loads. The full JSONL is what the
prompt builder reads.

## `verify_uniqueness.py`

`python scripts/verify_uniqueness.py --strict` exits 1 on any of:

* duplicate `entity_id`
* duplicate `(entity_type, name)` row
* orphan edges
* enriched card missing the canonical entity

This script is the gate that the data layer is honest. Run it after
every `canonicalize_v2.py` and every `enrich_entities_v2.py`.