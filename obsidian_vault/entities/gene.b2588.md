---
entity_id: "gene.b2588"
entity_type: "gene"
name: "rrfG"
source_database: "NCBI RefSeq"
source_id: "gene-b2588"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2588"
  - "rrfG"
---

# rrfG

`gene.b2588`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2588`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rrfG (gene.b2588) is a gene entity. EcoCyc product frame: RRFG-RRNA. Genomic coordinates: 2726069-2726188.

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

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=rrfG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008519,ECOCYC:EG30075,GeneID:947070`
- `gbkey:Gene`
- `gene_biotype:rRNA`

## Notes

NC_000913.3:2726069-2726188:-; feature_type=gene
