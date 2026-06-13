---
entity_id: "gene.b4010"
entity_type: "gene"
name: "rrfE"
source_database: "NCBI RefSeq"
source_id: "gene-b4010"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4010"
  - "rrfE"
---

# rrfE

`gene.b4010`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4010`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rrfE (gene.b4010) is a gene entity. EcoCyc product frame: RRFE-RRNA. Genomic coordinates: 4213040-4213159.

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

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=rrfE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013109,ECOCYC:EG30074,GeneID:948516`
- `gbkey:Gene`
- `gene_biotype:rRNA`

## Notes

NC_000913.3:4213040-4213159:+; feature_type=gene
