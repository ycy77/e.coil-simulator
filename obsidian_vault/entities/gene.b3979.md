---
entity_id: "gene.b3979"
entity_type: "gene"
name: "thrT"
source_database: "NCBI RefSeq"
source_id: "gene-b3979"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3979"
  - "thrT"
---

# thrT

`gene.b3979`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3979`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

thrT (gene.b3979) is a gene entity. EcoCyc product frame: thrT-tRNA. Genomic coordinates: 4175754-4175829.

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

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=thrT; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013018,ECOCYC:EG30101,GeneID:948480`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:4175754-4175829:+; feature_type=gene
