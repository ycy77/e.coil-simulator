---
entity_id: "gene.b3241"
entity_type: "gene"
name: "aaeA"
source_database: "NCBI RefSeq"
source_id: "gene-b3241"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3241"
  - "aaeA"
---

# aaeA

`gene.b3241`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3241`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aaeA (gene.b3241) is a gene entity. It encodes aaeA (protein.P46482). Encoded protein function: FUNCTION: Forms an efflux pump with AaeB. {ECO:0000255|HAMAP-Rule:MF_01544, ECO:0000269|PubMed:15489430}. EcoCyc product frame: G7686-MONOMER. EcoCyc synonyms: yhcQ. Genomic coordinates: 3388194-3389126.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P46482|protein.P46482]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010631,ECOCYC:G7686,GeneID:947748`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3388194-3389126:-; feature_type=gene
