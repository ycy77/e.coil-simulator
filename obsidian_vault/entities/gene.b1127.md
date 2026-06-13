---
entity_id: "gene.b1127"
entity_type: "gene"
name: "pepT"
source_database: "NCBI RefSeq"
source_id: "gene-b1127"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1127"
  - "pepT"
---

# pepT

`gene.b1127`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1127`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pepT (gene.b1127) is a gene entity. It encodes pepT (protein.P29745). Encoded protein function: FUNCTION: Cleaves the N-terminal amino acid of tripeptides. {ECO:0000250}. EcoCyc product frame: EG11549-MONOMER. Genomic coordinates: 1185844-1187070.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P29745|protein.P29745]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003800,ECOCYC:EG11549,GeneID:946333`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1185844-1187070:+; feature_type=gene
