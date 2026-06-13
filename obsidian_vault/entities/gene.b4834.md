---
entity_id: "gene.b4834"
entity_type: "gene"
name: "xylZ"
source_database: "NCBI RefSeq"
source_id: "gene-b4834"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4834"
  - "xylZ"
---

# xylZ

`gene.b4834`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4834`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

xylZ (gene.b4834) is a gene entity. EcoCyc product frame: RNA0-427. Genomic coordinates: 3729386-3729545.

## Biological Role

Repressed by araC (protein.P0A9E0). Activated by xylR (protein.P0ACI3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACI3|protein.P0ACI3]] `RegulonDB` `S` - regulator=XylR; target=xylZ; function=+
- `represses` <-- [[protein.P0A9E0|protein.P0A9E0]] `RegulonDB` `S` - regulator=AraC; target=xylZ; function=-

## External IDs

- `Dbxref:ECOCYC:G0-17109,GeneID:71004573`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:3729386-3729545:-; feature_type=gene
