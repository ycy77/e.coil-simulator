---
entity_id: "gene.b2589"
entity_type: "gene"
name: "rrlG"
source_database: "NCBI RefSeq"
source_id: "gene-b2589"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2589"
  - "rrlG"
---

# rrlG

`gene.b2589`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2589`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rrlG (gene.b2589) is a gene entity. EcoCyc product frame: RRLG-RRNA. Genomic coordinates: 2726281-2729184.

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

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=rrlG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008521,ECOCYC:EG30082,GeneID:947585`
- `gbkey:Gene`
- `gene_biotype:rRNA`

## Notes

NC_000913.3:2726281-2729184:-; feature_type=gene
