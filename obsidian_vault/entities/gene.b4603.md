---
entity_id: "gene.b4603"
entity_type: "gene"
name: "rseX"
source_database: "NCBI RefSeq"
source_id: "gene-b4603"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4603"
  - "rseX"
---

# rseX

`gene.b4603`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4603`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rseX (gene.b4603) is a gene entity. EcoCyc product frame: RNA0-327. EcoCyc synonyms: IS096. Genomic coordinates: 2033649-2033739.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (2)

- `represses` --> [[gene.b0912|gene.b0912]] `RegulonDB` `S` - regulator=RseX; target=ihfB; function=-
- `represses` --> [[gene.b4312|gene.b4312]] `RegulonDB` `S` - regulator=RseX; target=fimB; function=-

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ECOCYC:G0-10574,GeneID:5061507`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:2033649-2033739:+; feature_type=gene
