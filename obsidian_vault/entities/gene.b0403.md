---
entity_id: "gene.b0403"
entity_type: "gene"
name: "malZ"
source_database: "NCBI RefSeq"
source_id: "gene-b0403"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0403"
  - "malZ"
---

# malZ

`gene.b0403`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0403`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

malZ (gene.b0403) is a gene entity. It encodes malZ (protein.P21517). Encoded protein function: FUNCTION: May play a role in regulating the intracellular level of maltotriose. Cleaves glucose from the reducing end of maltotriose and longer maltodextrins with a chain length of up to 7 glucose units. EcoCyc product frame: MALTODEXGLUCOSID-MONOMER. Genomic coordinates: 422518-424332.

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21517|protein.P21517]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001402,ECOCYC:EG10565,GeneID:949131`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:422518-424332:+; feature_type=gene
