---
entity_id: "gene.b3123"
entity_type: "gene"
name: "rnpB"
source_database: "NCBI RefSeq"
source_id: "gene-b3123"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3123"
  - "rnpB"
---

# rnpB

`gene.b3123`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3123`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rnpB (gene.b3123) is a gene entity. EcoCyc product frame: RNPB-RNA. Genomic coordinates: 3270216-3270592.

## Biological Role

Repressed by fis (protein.P0A6R3), fur (protein.P0A9A9). Activated by fis (protein.P0A6R3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=rnpB; function=-+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=rnpB; function=-+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=rnpB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010269,ECOCYC:EG30069,GeneID:947634`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:3270216-3270592:-; feature_type=gene
