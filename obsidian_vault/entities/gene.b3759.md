---
entity_id: "gene.b3759"
entity_type: "gene"
name: "rrfC"
source_database: "NCBI RefSeq"
source_id: "gene-b3759"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3759"
  - "rrfC"
---

# rrfC

`gene.b3759`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3759`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rrfC (gene.b3759) is a gene entity. EcoCyc product frame: RRFC-RRNA. Genomic coordinates: 3946700-3946819.

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

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=rrfC; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=rrfC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012285,ECOCYC:EG30072,GeneID:948273`
- `gbkey:Gene`
- `gene_biotype:rRNA`

## Notes

NC_000913.3:3946700-3946819:+; feature_type=gene
