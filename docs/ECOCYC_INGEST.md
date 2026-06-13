# EcoCyc Ingest

## Source files actually consumed

`scripts/parse_ecocyc.py` only opens these ten files under
`data/raw/ecocyc/extracted/29.6/data/`:

| File | Read for |
|---|---|
| `genes.dat` | gene records, accession map |
| `proteins.dat` | protein records, MONOMER map |
| `compounds.dat` | small-molecule records, KEYS |
| `reactions.dat` | reaction equations |
| `enzrxns.dat` | enzyme–reaction links |
| `pathways.dat` | pathway membership |
| `regulation.dat` | TF–gene regulatory edges |
| `protligandcplxes.dat` | protein–ligand complexes |
| `protcplxs.col` | complex composition |
| `transporters.col` | transporter–substrate edges |

`wc-model/MIX0-*/wcm_*.tsv` are kept for downstream metabolic-model
work; nothing in the simulator reads them yet.

## Files explicitly trimmed

These were deleted because **no Python file imports them or reads
their paths**:

| File / dir | Size |
|---|---|
| `biopax-level2.owl` | 74M |
| `biopax-level3.owl` | 71M |
| `ecoli-COLI-K12-3659364498.fsa` | 4.5M |
| `dnaseq.fsa` | 4.6M |
| `protseq.fsa` | 1.9M |
| BLAST DB indices (`*.phr/.pin/.psd/.psi/.psq` and nt variants) | ~10M |
| `data/fba/` (FBA examples) | 52M |
| `data/moleculardiagrams/` (SVG diagrams) | 2.4M |
| `data/kb/` (Pathway Tools compiled KB) | 171M |
| `data/../reports/` (HTML hole reports) | 512K |
| `data/../rawdata/coli.dat` (single dump) | 908K |
| `data/../input/` (organism metadata) | 36K |
| `data/../wc-model-29.0/` and `wc-model-29.1/` | 16M |
| `*.gaf`, `*.gaf-errors`, `*.col` not in the consumed set, and 16 other `.dat` files | ~100M |

Total trimmed: ~700M → ~38M under
`data/raw/ecocyc/extracted/29.6/`.

If a future feature needs any of those files back, the easiest path is
to re-fetch them from EcoCyc with `scripts/fetch_ecocyc_flatfiles.py`
(only the manifest has been trimmed, not the script).

## Pipeline order

```
fetch_ecocyc_flatfiles.py        # pulls the EcoCyc tarball
  └─── tar xzf ... → extracted/<version>/data/*.dat / *.col
parse_ecocyc.py                  # reads the 10 files above
  └─── ecocyc_id_map.csv         # maps EcoCyc unique ids → entity_id
build_entities.py                # joins with UniProt / KEGG / NCBI / RegulonDB
build_edges.py
build_regulondb_edges.py
build_pathways.py
build_rule_registry.py
canonicalize_normalized.py       # first-gen, small-molecule only (preserved)
canonicalize_v2.py               # second-gen, full graph
enrich_entities.py               # first-gen enricher (preserved)
enrich_entities_v2.py            # second-gen, multi-source
audit_entities.py                # vLLM audit
verify_uniqueness.py             # invariant gate
```