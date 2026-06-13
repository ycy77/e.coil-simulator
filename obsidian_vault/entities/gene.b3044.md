---
entity_id: "gene.b3044"
entity_type: "gene"
name: "insC5"
source_database: "NCBI RefSeq"
source_id: "gene-b3044"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3044"
  - "insC5"
---

# insC5

`gene.b3044`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3044`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

insC5 (gene.b3044) is a gene entity. It encodes insC5 (protein.P0CF44). Encoded protein function: FUNCTION: Involved in the transposition of the insertion sequence IS2. EcoCyc product frame: MONOMER0-4253. EcoCyc synonyms: yi21-5. Genomic coordinates: 3186187-3186552.

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0CF44|protein.P0CF44]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009997,ECOCYC:G7583,GeneID:947520`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3186187-3186552:+; feature_type=gene
