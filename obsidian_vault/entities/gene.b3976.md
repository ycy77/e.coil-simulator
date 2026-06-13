---
entity_id: "gene.b3976"
entity_type: "gene"
name: "thrU"
source_database: "NCBI RefSeq"
source_id: "gene-b3976"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3976"
  - "thrU"
---

# thrU

`gene.b3976`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3976`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

thrU (gene.b3976) is a gene entity. EcoCyc product frame: thrU-tRNA. Genomic coordinates: 4175388-4175463.

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

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=thrU; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013011,ECOCYC:EG30102,GeneID:948476`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:4175388-4175463:+; feature_type=gene
