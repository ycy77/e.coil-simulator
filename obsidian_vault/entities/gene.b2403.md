---
entity_id: "gene.b2403"
entity_type: "gene"
name: "valY"
source_database: "NCBI RefSeq"
source_id: "gene-b2403"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2403"
  - "valY"
---

# valY

`gene.b2403`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2403`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

valY (gene.b2403) is a gene entity. EcoCyc product frame: valY-tRNA. EcoCyc synonyms: valUgamma. Genomic coordinates: 2521173-2521248.

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

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=valY; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007918,ECOCYC:EG30114,GeneID:946870`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:2521173-2521248:+; feature_type=gene
