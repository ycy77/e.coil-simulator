---
entity_id: "gene.b3756"
entity_type: "gene"
name: "rrsC"
source_database: "NCBI RefSeq"
source_id: "gene-b3756"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3756"
  - "rrsC"
---

# rrsC

`gene.b3756`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3756`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rrsC (gene.b3756) is a gene entity. EcoCyc product frame: RRSC-RRNA. Genomic coordinates: 3941808-3943349.

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by fis (protein.P0A6R3).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=rrsC; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=rrsC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012279,ECOCYC:EG30086,GeneID:948270`
- `gbkey:Gene`
- `gene_biotype:rRNA`

## Notes

NC_000913.3:3941808-3943349:+; feature_type=gene
