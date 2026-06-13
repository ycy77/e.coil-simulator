---
entity_id: "gene.b4009"
entity_type: "gene"
name: "rrlE"
source_database: "NCBI RefSeq"
source_id: "gene-b4009"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4009"
  - "rrlE"
---

# rrlE

`gene.b4009`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4009`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rrlE (gene.b4009) is a gene entity. EcoCyc product frame: RRLE-RRNA. Genomic coordinates: 4210043-4212946.

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

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=rrlE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013107,ECOCYC:EG30081,GeneID:948509`
- `gbkey:Gene`
- `gene_biotype:rRNA`

## Notes

NC_000913.3:4210043-4212946:+; feature_type=gene
