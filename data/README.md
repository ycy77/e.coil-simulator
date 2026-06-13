# Data status

## Current public-data build

Generated on the local workspace from public UniProt, KEGG, NCBI RefSeq sources, plus manually downloaded RegulonDB TSV files.
EcoCyc/BioCyc access has now been licensed for this project; confidential
download details are intentionally not stored in this repository.

```text
data/raw/uniprot/
data/raw/kegg/
data/raw/ncbi_refseq/
data/regulationDB/
data/normalized/entities.csv
data/normalized/ncbi_entities.csv
data/normalized/regulondb_edges.csv
data/normalized/regulondb_skipped.tsv
data/normalized/edges.csv
data/normalized/pathways.csv
data/registry/native_rules.jsonl
```

Current normalized counts:

```text
entities.csv: 13194 entities
  protein: 4403
  small_molecule: 3480
  reaction: 590
  gene: 4506
  rna: 215

edges.csv: 27232 edges
  encodes: 4402
  participates_in: 9867
  catalyzes: 4415
  activates: 3721
  represses: 2356
  is_substrate_of: 1164
  is_product_of: 1307

pathways.csv: 137 pathways

native_rules.jsonl: 27232 rules
```

## Included sources

- UniProt proteome `UP000000625`: protein entities, function comments, location comments, GO IDs, KEGG/GeneID mappings.
- KEGG organism `eco`: pathways, gene-pathway links, gene-EC links, pathway details, pathway compound/gene members.
- KEGG reaction API: EC-to-reaction mapping and reaction equations for reaction entities plus substrate/product edges.
- NCBI RefSeq assembly `GCF_000005845.2_ASM584v2`: gene and RNA entities from GFF; genome, RNA, CDS, protein, and GenBank raw files are cached.
- RegulonDB downloaded datasets: confirmed/strong regulator-gene and sigma-gene interactions, normalized into `activates` and `represses` edges.
- Native rule registry: generated from `edges.csv` by `scripts/build_rule_registry.py`; it is the current rule source used by the simulator.

## Not yet included

These require licensed/manual downloads or later parsers:

- EcoCyc: license acquired; flat files should be downloaded to `data/raw/ecocyc/` via `scripts/fetch_ecocyc_flatfiles.py`, then parsed into complexes, curated reactions, transport, regulation, and response-pattern annotations.
- RegulonDB deeper layers: transcription-unit/operon expansion, promoter architecture, binding-site intervals, and regulator conformation details.
- Complex Portal / STRING / IntAct / BioGRID: optional complex and PPI supplements.
- ChEBI: compound synonyms and chemical identifiers beyond KEGG.

## Known limitations

- `entities.csv` currently has protein, small-molecule, reaction, gene, and RNA entities. Complex and regulatory-region entities are not yet fully generated.
- `edges.csv` currently covers gene-protein encoding, KEGG pathway membership, protein-to-EC/reaction catalysis, reaction substrate/product edges, and high-confidence RegulonDB transcriptional activation/repression.
- Protein complex membership, PPI, binding, inhibition, transport, and detailed promoter/operon structure are still not fully represented.
- EcoCyc is now the next highest-priority integration source for curated complex membership, transport reactions, and richer reaction/regulation annotations.
