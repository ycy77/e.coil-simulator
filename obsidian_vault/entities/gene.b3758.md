---
entity_id: "gene.b3758"
entity_type: "gene"
name: "rrlC"
source_database: "NCBI RefSeq"
source_id: "gene-b3758"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3758"
  - "rrlC"
---

# rrlC

`gene.b3758`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3758`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rrlC (gene.b3758) is a gene entity. EcoCyc product frame: RRLC-RRNA. Genomic coordinates: 3943704-3946607.

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

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=rrlC; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=rrlC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012283,ECOCYC:EG30079,GeneID:948268`
- `gbkey:Gene`
- `gene_biotype:rRNA`

## Notes

NC_000913.3:3943704-3946607:+; feature_type=gene
