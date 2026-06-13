---
entity_id: "gene.b4691"
entity_type: "gene"
name: "sroH"
source_database: "NCBI RefSeq"
source_id: "gene-b4691"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4691"
  - "sroH"
---

# sroH

`gene.b4691`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4691`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sroH (gene.b4691) is a gene entity. EcoCyc product frame: RNA0-128. Genomic coordinates: 4190327-4190487.

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ECOCYC:G0-9388,GeneID:7751646`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:4190327-4190487:-; feature_type=gene
