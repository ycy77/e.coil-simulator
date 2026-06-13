---
entity_id: "gene.b4762"
entity_type: "gene"
name: "sroA"
source_database: "NCBI RefSeq"
source_id: "gene-b4762"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4762"
  - "sroA"
---

# sroA

`gene.b4762`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4762`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sroA (gene.b4762) is a gene entity. EcoCyc product frame: RNA0-404. EcoCyc synonyms: tpe79. Genomic coordinates: 75516-75608.

## Biological Role

Repressed by sgrR (protein.P33595).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `represses` <-- [[protein.P33595|protein.P33595]] `RegulonDB` `C` - regulator=SgrR; target=sroA; function=-

## External IDs

- `Dbxref:ECOCYC:G0-9381,GeneID:63925622`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:75516-75608:-; feature_type=gene
