---
entity_id: "gene.b4369"
entity_type: "gene"
name: "leuP"
source_database: "NCBI RefSeq"
source_id: "gene-b4369"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4369"
  - "leuP"
---

# leuP

`gene.b4369`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4369`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

leuP (gene.b4369) is a gene entity. EcoCyc product frame: leuP-tRNA. EcoCyc synonyms: leuV-beta, leuVbeta. Genomic coordinates: 4606200-4606286.

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

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=leuP; function=+

## External IDs

- `Dbxref:ASAP:ABE-0014331,ECOCYC:EG30047,GeneID:948875`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:4606200-4606286:-; feature_type=gene
