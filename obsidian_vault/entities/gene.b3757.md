---
entity_id: "gene.b3757"
entity_type: "gene"
name: "gltU"
source_database: "NCBI RefSeq"
source_id: "gene-b3757"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3757"
  - "gltU"
---

# gltU

`gene.b3757`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3757`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gltU (gene.b3757) is a gene entity. EcoCyc product frame: gltU-tRNA. EcoCyc synonyms: tgtC. Genomic coordinates: 3943435-3943510.

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by fis (protein.P0A6R3).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=gltU; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=gltU; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012281,ECOCYC:EG30033,GeneID:948271`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:3943435-3943510:+; feature_type=gene
