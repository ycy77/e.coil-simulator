---
entity_id: "gene.b4828"
entity_type: "gene"
name: "motR"
source_database: "NCBI RefSeq"
source_id: "gene-b4828"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4828"
  - "motR"
---

# motR

`gene.b4828`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4828`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

motR (gene.b4828) is a gene entity. EcoCyc product frame: RNA0-421. Genomic coordinates: 1977208-1977302.

## Biological Role

Repressed by cpxR (protein.P0AE88).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `represses` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=motR; function=-

## External IDs

- `Dbxref:ECOCYC:G0-17103,GeneID:71004565`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:1977208-1977302:-; feature_type=gene
