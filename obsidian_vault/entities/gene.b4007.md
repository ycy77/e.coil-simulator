---
entity_id: "gene.b4007"
entity_type: "gene"
name: "rrsE"
source_database: "NCBI RefSeq"
source_id: "gene-b4007"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4007"
  - "rrsE"
---

# rrsE

`gene.b4007`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4007`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rrsE (gene.b4007) is a gene entity. EcoCyc product frame: RRSE-RRNA. Genomic coordinates: 4208147-4209688.

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

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=rrsE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013103,ECOCYC:EG30088,GeneID:948511`
- `gbkey:Gene`
- `gene_biotype:rRNA`

## Notes

NC_000913.3:4208147-4209688:+; feature_type=gene
