# Validation summary — the credibility layer

What in this project is validated against EXTERNAL standards (not self-authored),
with current numbers, how to reproduce, and what is honestly still missing. This
is the layer a top-tier review demands; read it before believing any score.

## 1. Knowledge-graph quality vs RegulonDB (gold standard)

`scripts/validate_kg.py` → `docs/KG_VALIDATION_<date>.md`. Compares the graph's
regulatory edges against RegulonDB `NetworkRegulatorGene` (frozen, read-only).

| Metric | Value | Meaning |
| --- | --- | --- |
| **Strong-evidence recall** | **94.4%** (2957/3134) | of direct-experiment RegulonDB regulation, how much the graph contains |
| Weak-evidence recall | 12.2% (365/2991) | inferred edges, excluded by design (`--include-weak` to add, tagged) |
| **Sign accuracy** | **100.0%** (4072/4072) | every present edge has the correct activator/repressor direction |
| Structurally unrepresentable | ~362 interactions | sigma factors / sRNAs / ppGpp (gene→gene graph can't route these) |

Honest read: the **strong** regulatory layer is near-complete and directionally
exact; the headline "58.8% of all gold" is dragged down by deliberately-excluded
weak evidence, not by accidental gaps.

## 2. Perturbation-response benchmark vs RegulonDB

`scripts/benchmark_perturbation.py`. Knock out each regulator, predict each
target's direction, score vs the RegulonDB sign. Single-regulator targets have an
unambiguous expected direction (the rest need expression data — see §5).
Mock baseline: **~97% direction accuracy** on scorable single-regulator cases
(direction folds the two-axis efficiency). Real-LLM comparison: run `--mode both`
on the GPU host.

## 3. Independent co-expression validation (Tjaden 2023, no RegulonDB reuse)

`scripts/fetch_transcriptome_compendium.py` + `scripts/validate_coexpression.py`.
TPM across 3,376 RNA-seq samples: an `activates` edge should show positive
TF–target correlation, `represses` negative. Independent of RegulonDB → genuine
external check. Pending the data fetch on the GPU host (laptop has no egress).

## 4. Literature-grounded phenotype patterns (cited, not self-authored)

`data/phenotypes/phenotype_db_literature.yaml` on `configs/simulation_lit.yaml`.
3 DOI-cited patterns (SOS derepression / Cory 2024; Cra dual-output / Huang 2024;
RpoS–RssB feedback / Bouillet 2024), each with a biological resting state and an
expected outcome FROM THE PAPER. These validate that the graph reproduces cited
mechanisms (mock-solvable cascades). The self-authored `phenotype_db.yaml` is
marked DEV-ONLY (circular, not evidence).

Literature edges are ingested under 5 integrity rules (`scripts/ingest_literature_edges.py`,
ledger in `docs/LITERATURE_INGEST_LEDGER.md`): separate accounting from the frozen
validation graph (1); edges and tests not co-tuned (2); evidence gating —
direct+peer-reviewed+K-12 only (3); b-number/UniProt cross-checked against the KG,
no guessing (4, caught a real error: RssB listed as b3235 = degS); canonical ids,
conflicts flagged not overwritten (5).

## 5. The honest gap → the headline experiment for a paper

The literature patterns above are propagation/cascade tests the mock also solves;
they are NOT mock-vs-LLM discriminators. A true discriminator is a SINGLE-NODE
CONFLICT (a gene receiving opposing signals, where the rules must opt out and only
the model can decide). The graph has the conflict STRUCTURE (1005 dual-regulated
genes), but the net-direction ANSWER cannot be hand-set without it being
self-authored again — it must come from MEASURED data: a labeled expression
compendium (PRECISE-1K / iModulons) with knockout/condition contrasts. Building
that DE-grounded conflict benchmark is the path to the "LLM beats rules / beats
FBA" claim. See `docs/REMOTE_WORK_PLAN.md` Phase 6.3.

## 6. LLM decoding/action reliability (fixed; pending real-LLM confirmation)

Diagnosed by probing the deployed vLLM directly:
- Top-level `guided_json` was **silently ignored** (output kept `<think>`, ignored
  the schema, truncated the action). Switched to `response_format: json_schema`
  (honored; suppresses `<think>`).
- The model emitted invalid `rule_id`s that the interpreter rejected. Now each
  request carries a **per-agent schema constraining rule_id** to that agent's valid
  ids, so an invalid rule_id is impossible.
- `max_active_agents` **dropped** overflow; now overflow **spills to the next round**
  (a pure throughput cap — discrete turn-based).

These likely explain much of the L2/efficiency variance seen earlier; confirm with
`score_phenotypes.py --mode both` on the GPU host (deferred during parallel web dev).

## Reproduce (GPU host)

```bash
python scripts/validate_kg.py --date $(date +%Y%m%d)
python scripts/benchmark_perturbation.py --mode both --max-tfs 80
python scripts/fetch_transcriptome_compendium.py && python scripts/validate_coexpression.py --matrix data/raw/transcriptome_compendium/<file>
python scripts/build_literature_graph.py && python scripts/score_phenotypes.py --config configs/simulation_lit.yaml --phenotype-db data/phenotypes/phenotype_db_literature.yaml --mode both --repeat 3
```
