---
entity_id: "gene.b0716"
entity_type: "gene"
name: "ybgO"
source_database: "NCBI RefSeq"
source_id: "gene-b0716"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0716"
  - "ybgO"
---

# ybgO

`gene.b0716`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0716`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybgO (gene.b0716) is a gene entity. It encodes ybgO (protein.P75748). Encoded protein function: FUNCTION: May be involved in a fimbrial system chaperoned by YbgP and exported by YbgQ. EcoCyc product frame: G6385-MONOMER. Genomic coordinates: 747921-748982. EcoCyc protein note: YbgO is a hypothetical protein. Sequence similarity suggests that it may be a outer membrane porin . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including ybgOPQD. When this operon is removed, the cells are larger, produce polyhydroxyalkanoates (PHAs) and grows better, particularly in M9G media. A fimbrial-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised; it also grows faster and produces PHAs and had higher efficiency of glucose utilization .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75748|protein.P75748]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002441,ECOCYC:G6385,GeneID:947550`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:747921-748982:-; feature_type=gene
