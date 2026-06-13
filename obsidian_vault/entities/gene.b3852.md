---
entity_id: "gene.b3852"
entity_type: "gene"
name: "ileT"
source_database: "NCBI RefSeq"
source_id: "gene-b3852"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3852"
  - "ileT"
---

# ileT

`gene.b3852`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3852`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ileT (gene.b3852) is a gene entity. EcoCyc product frame: ileT-tRNA. EcoCyc synonyms: tilA. Genomic coordinates: 4037141-4037217.

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

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=ileT; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012581,ECOCYC:EG30043,GeneID:948339`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:4037141-4037217:+; feature_type=gene
