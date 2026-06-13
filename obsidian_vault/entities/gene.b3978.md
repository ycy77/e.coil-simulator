---
entity_id: "gene.b3978"
entity_type: "gene"
name: "glyT"
source_database: "NCBI RefSeq"
source_id: "gene-b3978"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3978"
  - "glyT"
---

# glyT

`gene.b3978`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3978`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glyT (gene.b3978) is a gene entity. EcoCyc product frame: glyT-tRNA. EcoCyc synonyms: sumA, sup15B, supA36. Genomic coordinates: 4175673-4175747.

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

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=glyT; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013016,ECOCYC:EG30036,GeneID:948481`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:4175673-4175747:+; feature_type=gene
