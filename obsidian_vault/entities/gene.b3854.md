---
entity_id: "gene.b3854"
entity_type: "gene"
name: "rrlA"
source_database: "NCBI RefSeq"
source_id: "gene-b3854"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3854"
  - "rrlA"
---

# rrlA

`gene.b3854`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3854`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rrlA (gene.b3854) is a gene entity. EcoCyc product frame: RRLA-RRNA. Genomic coordinates: 4037519-4040423.

## Biological Role

Activated by fis (protein.P0A6R3).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=rrlA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012586,ECOCYC:EG30077,GeneID:948341`
- `gbkey:Gene`
- `gene_biotype:rRNA`

## Notes

NC_000913.3:4037519-4040423:+; feature_type=gene
