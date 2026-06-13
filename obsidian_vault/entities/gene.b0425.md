---
entity_id: "gene.b0425"
entity_type: "gene"
name: "panE"
source_database: "NCBI RefSeq"
source_id: "gene-b0425"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0425"
  - "panE"
---

# panE

`gene.b0425`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0425`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

panE (gene.b0425) is a gene entity. It encodes panE (protein.P0A9J4). Encoded protein function: FUNCTION: Catalyzes the NADPH-dependent reduction of ketopantoate into pantoic acid. {ECO:0000269|PubMed:10736170, ECO:0000269|PubMed:11123955}. EcoCyc product frame: 2-DEHYDROPANTOATE-REDUCT-MONOMER. EcoCyc synonyms: apbA. Genomic coordinates: 443604-444515. EcoCyc protein note: 2-Dehydropantoate 2-reductase catalyzes the NADPH-dependent reduction of ketopantoate to pantoate. The enzyme does not require added divalent metal ions . Kinetic data is consistent with an ordered sequential reaction mechanism, with NADPH binding followed by ketopantoate binding . Residues involved in catalysis and substrate binding were identified by site-directed mutagenesis . The enzyme has relatively high substrate specificity . Crystal structures of the enzyme have been solved . The enzyme is a monomer in solution and is comprised of an N-terminal Rossmann fold domain and a C-terminal α-helical domain . The enzyme was used as a target for fragment-based drug discovery . A panE mutant alone is not auxotrophic for pantothenate, because in both E. coli and S. typhimurium, the reaction can also be carried out by IlvC (CPLX0-7643) . ApbA: "alternative pyrimidine biosynthetic pathway" (Salmonella typhimurium) PanE: "pantothenate"

## Enriched Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9J4|protein.P0A9J4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001474,ECOCYC:G6239,GeneID:945065`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:443604-444515:-; feature_type=gene
