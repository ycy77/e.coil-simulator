---
entity_id: "gene.b4808"
entity_type: "gene"
name: "chiZ"
source_database: "NCBI RefSeq"
source_id: "gene-b4808"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4808"
  - "chiZ"
---

# chiZ

`gene.b4808`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4808`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

chiZ (gene.b4808) is a gene entity. EcoCyc product frame: RNA0-411. Genomic coordinates: 708236-708333.

## Biological Role

Repressed by chiX (gene.b4585), nagC (protein.P0AF20).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `represses` <-- [[gene.b4585|gene.b4585]] `RegulonDB` `S` - regulator=ChiX; target=chiZ; function=-
- `represses` <-- [[protein.P0AF20|protein.P0AF20]] `RegulonDB` `S` - regulator=NagC; target=chiZ; function=-

## External IDs

- `Dbxref:ECOCYC:G0-17083,GeneID:71004556`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:708236-708333:+; feature_type=gene
