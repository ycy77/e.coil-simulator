---
entity_id: "gene.b4714"
entity_type: "gene"
name: "ralA"
source_database: "NCBI RefSeq"
source_id: "gene-b4714"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4714"
  - "ralA"
---

# ralA

`gene.b4714`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4714`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ralA (gene.b4714) is a gene entity. EcoCyc product frame: RNA0-385. Genomic coordinates: 1413556-1413734.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `represses` --> [[gene.b1348|gene.b1348]] `RegulonDB` `S` - regulator=RalA; target=ralR; function=-

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ECOCYC:G0-16600,GeneID:20160642`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:1413556-1413734:+; feature_type=gene
