---
entity_id: "gene.b3851"
entity_type: "gene"
name: "rrsA"
source_database: "NCBI RefSeq"
source_id: "gene-b3851"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3851"
  - "rrsA"
---

# rrsA

`gene.b3851`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3851`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rrsA (gene.b3851) is a gene entity. EcoCyc product frame: RRSA-RRNA. Genomic coordinates: 4035531-4037072.

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

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=rrsA; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=rrsA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012579,ECOCYC:EG30084,GeneID:948332`
- `gbkey:Gene`
- `gene_biotype:rRNA`

## Notes

NC_000913.3:4035531-4037072:+; feature_type=gene
