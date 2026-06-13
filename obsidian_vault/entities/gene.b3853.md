---
entity_id: "gene.b3853"
entity_type: "gene"
name: "alaT"
source_database: "NCBI RefSeq"
source_id: "gene-b3853"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3853"
  - "alaT"
---

# alaT

`gene.b3853`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3853`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

alaT (gene.b3853) is a gene entity. EcoCyc product frame: charged-alaT-tRNA. EcoCyc synonyms: talA. Genomic coordinates: 4037260-4037335.

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

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=alaT; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012584,ECOCYC:EG30008,GeneID:948337`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:4037260-4037335:+; feature_type=gene
