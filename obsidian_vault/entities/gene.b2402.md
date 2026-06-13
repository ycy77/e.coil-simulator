---
entity_id: "gene.b2402"
entity_type: "gene"
name: "valX"
source_database: "NCBI RefSeq"
source_id: "gene-b2402"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2402"
  - "valX"
---

# valX

`gene.b2402`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2402`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

valX (gene.b2402) is a gene entity. EcoCyc product frame: valX-tRNA. EcoCyc synonyms: valU-beta, valUbeta. Genomic coordinates: 2521051-2521126.

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

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=valX; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007916,ECOCYC:EG30113,GeneID:946817`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:2521051-2521126:+; feature_type=gene
