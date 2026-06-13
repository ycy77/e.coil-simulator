---
entity_id: "gene.b3855"
entity_type: "gene"
name: "rrfA"
source_database: "NCBI RefSeq"
source_id: "gene-b3855"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3855"
  - "rrfA"
---

# rrfA

`gene.b3855`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3855`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rrfA (gene.b3855) is a gene entity. EcoCyc product frame: RRFA-RRNA. Genomic coordinates: 4040517-4040636.

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

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=rrfA; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=rrfA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012588,ECOCYC:EG30070,GeneID:948345`
- `gbkey:Gene`
- `gene_biotype:rRNA`

## Notes

NC_000913.3:4040517-4040636:+; feature_type=gene
