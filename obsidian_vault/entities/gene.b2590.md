---
entity_id: "gene.b2590"
entity_type: "gene"
name: "gltW"
source_database: "NCBI RefSeq"
source_id: "gene-b2590"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2590"
  - "gltW"
---

# gltW

`gene.b2590`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2590`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gltW (gene.b2590) is a gene entity. EcoCyc product frame: gltW-tRNA. Genomic coordinates: 2729369-2729444.

## Biological Role

Activated by fis (protein.P0A6R3).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=gltW; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008523,ECOCYC:EG30035,GeneID:947076`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:2729369-2729444:-; feature_type=gene
