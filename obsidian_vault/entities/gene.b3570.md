---
entity_id: "gene.b3570"
entity_type: "gene"
name: "bax"
source_database: "NCBI RefSeq"
source_id: "gene-b3570"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3570"
  - "bax"
---

# bax

`gene.b3570`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3570`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bax (gene.b3570) is a gene entity. It encodes bax (protein.P27297). Encoded protein function: Protein bax EcoCyc product frame: EG11360-MONOMER. Genomic coordinates: 3736353-3737177. EcoCyc protein note: Bax: "between avtA and xyl"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27297|protein.P27297]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011655,ECOCYC:EG11360,GeneID:948089`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3736353-3737177:-; feature_type=gene
