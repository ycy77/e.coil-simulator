---
entity_id: "gene.b2401"
entity_type: "gene"
name: "valU"
source_database: "NCBI RefSeq"
source_id: "gene-b2401"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2401"
  - "valU"
---

# valU

`gene.b2401`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2401`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

valU (gene.b2401) is a gene entity. EcoCyc product frame: valU-tRNA. EcoCyc synonyms: valUalpha. Genomic coordinates: 2520931-2521006.

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

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=valU; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007914,ECOCYC:EG30110,GeneID:946824`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:2520931-2521006:+; feature_type=gene
