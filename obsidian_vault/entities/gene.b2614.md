---
entity_id: "gene.b2614"
entity_type: "gene"
name: "grpE"
source_database: "NCBI RefSeq"
source_id: "gene-b2614"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2614"
  - "grpE"
---

# grpE

`gene.b2614`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2614`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

grpE (gene.b2614) is a gene entity. It encodes grpE (protein.P09372). Encoded protein function: FUNCTION: Participates actively in the response to hyperosmotic and heat shock by preventing the aggregation of stress-denatured proteins, in association with DnaK and GrpE. It is the nucleotide exchange factor for DnaK and may function as a thermosensor. Unfolded proteins bind initially to DnaJ; upon interaction with the DnaJ-bound protein, DnaK hydrolyzes its bound ATP, resulting in the formation of a stable complex. GrpE releases ADP from DnaK; ATP binding to DnaK triggers the release of the substrate protein, thus completing the reaction cycle. Several rounds of ATP-dependent interactions between DnaJ, DnaK and GrpE are required for fully efficient folding. {ECO:0000269|PubMed:15102842, ECO:0000269|PubMed:8890154}. EcoCyc product frame: EG10416-MONOMER. Genomic coordinates: 2750115-2750708.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09372|protein.P09372]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008598,ECOCYC:EG10416,GeneID:947097`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2750115-2750708:-; feature_type=gene
