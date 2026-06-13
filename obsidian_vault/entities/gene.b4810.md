---
entity_id: "gene.b4810"
entity_type: "gene"
name: "ftsO"
source_database: "NCBI RefSeq"
source_id: "gene-b4810"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4810"
  - "ftsO"
---

# ftsO

`gene.b4810`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4810`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ftsO (gene.b4810) is a gene entity. EcoCyc product frame: RNA0-413. Genomic coordinates: 92485-92658.

## Biological Role

Repressed by pdhR (protein.P0ACL9), mraZ (protein.P22186).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `S` - regulator=PdhR; target=ftsO; function=-
- `represses` <-- [[protein.P22186|protein.P22186]] `RegulonDB` `C` - regulator=MraZ; target=ftsO; function=-

## External IDs

- `Dbxref:ECOCYC:G0-17085,GeneID:71004551`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:92485-92658:+; feature_type=gene
