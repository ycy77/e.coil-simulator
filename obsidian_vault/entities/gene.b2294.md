---
entity_id: "gene.b2294"
entity_type: "gene"
name: "yfbU"
source_database: "NCBI RefSeq"
source_id: "gene-b2294"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2294"
  - "yfbU"
---

# yfbU

`gene.b2294`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2294`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfbU (gene.b2294) is a gene entity. It encodes yfbU (protein.P0A8W8). Encoded protein function: UPF0304 protein YfbU EcoCyc product frame: G7188-MONOMER. Genomic coordinates: 2412100-2412594.

## Biological Role

Activated by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8W8|protein.P0A8W8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yfbU; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007571,ECOCYC:G7188,GeneID:946767`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2412100-2412594:-; feature_type=gene
