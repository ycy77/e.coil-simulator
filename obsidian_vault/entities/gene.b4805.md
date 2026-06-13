---
entity_id: "gene.b4805"
entity_type: "gene"
name: "raiZ"
source_database: "NCBI RefSeq"
source_id: "gene-b4805"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4805"
  - "raiZ"
---

# raiZ

`gene.b4805`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4805`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

raiZ (gene.b4805) is a gene entity. EcoCyc product frame: RNA0-407. Genomic coordinates: 2737381-2737542.

## Biological Role

Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=raiZ; function=+

## External IDs

- `Dbxref:ECOCYC:G0-17078,GeneID:71004571`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:2737381-2737542:+; feature_type=gene
