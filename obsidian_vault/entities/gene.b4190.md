---
entity_id: "gene.b4190"
entity_type: "gene"
name: "yjfP"
source_database: "NCBI RefSeq"
source_id: "gene-b4190"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4190"
  - "yjfP"
---

# yjfP

`gene.b4190`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4190`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjfP (gene.b4190) is a gene entity. It encodes yjfP (protein.P39298). Encoded protein function: FUNCTION: Displays esterase activity toward palmitoyl-CoA and pNP-butyrate. {ECO:0000269|PubMed:15808744}. EcoCyc product frame: G7853-MONOMER. Genomic coordinates: 4416952-4417701.

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39298|protein.P39298]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013711,ECOCYC:G7853,GeneID:948707`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4416952-4417701:+; feature_type=gene
