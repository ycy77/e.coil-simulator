---
entity_id: "gene.b4008"
entity_type: "gene"
name: "gltV"
source_database: "NCBI RefSeq"
source_id: "gene-b4008"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4008"
  - "gltV"
---

# gltV

`gene.b4008`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4008`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gltV (gene.b4008) is a gene entity. EcoCyc product frame: gltV-tRNA. EcoCyc synonyms: tgtE. Genomic coordinates: 4209774-4209849.

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

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=gltV; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013105,ECOCYC:EG30034,GeneID:948510`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:4209774-4209849:+; feature_type=gene
