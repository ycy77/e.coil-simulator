---
entity_id: "gene.b4370"
entity_type: "gene"
name: "leuQ"
source_database: "NCBI RefSeq"
source_id: "gene-b4370"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4370"
  - "leuQ"
---

# leuQ

`gene.b4370`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4370`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

leuQ (gene.b4370) is a gene entity. EcoCyc product frame: leuQ-tRNA. EcoCyc synonyms: leuVgamma. Genomic coordinates: 4606315-4606401.

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

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=leuQ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0014333,ECOCYC:EG30048,GeneID:948893`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:4606315-4606401:-; feature_type=gene
