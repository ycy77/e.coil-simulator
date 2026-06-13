---
entity_id: "gene.b4226"
entity_type: "gene"
name: "ppa"
source_database: "NCBI RefSeq"
source_id: "gene-b4226"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4226"
  - "ppa"
---

# ppa

`gene.b4226`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4226`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ppa (gene.b4226) is a gene entity. It encodes ppa (protein.P0A7A9). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of inorganic pyrophosphate (PPi) forming two phosphate ions. {ECO:0000255|HAMAP-Rule:MF_00209}. EcoCyc product frame: INORGPYROPHOSPHAT-MONOMER. Genomic coordinates: 4449122-4449652.

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7A9|protein.P0A7A9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013824,ECOCYC:EG10755,GeneID:948748`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4449122-4449652:-; feature_type=gene
