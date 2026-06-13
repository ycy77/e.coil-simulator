---
entity_id: "gene.b4806"
entity_type: "gene"
name: "C0293"
source_database: "NCBI RefSeq"
source_id: "gene-b4806"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4806"
  - "C0293"
---

# C0293

`gene.b4806`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4806`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

C0293 (gene.b4806) is a gene entity. EcoCyc product frame: RNA0-409. Genomic coordinates: 1196711-1196782.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (3)

- `represses` --> [[gene.b1187|gene.b1187]] `RegulonDB` `S` - regulator=C0293; target=fadR; function=-
- `represses` --> [[gene.b2537|gene.b2537]] `RegulonDB` `S` - regulator=C0293; target=hcaR; function=-
- `represses` --> [[gene.b4706|gene.b4706]] `RegulonDB` `S` - regulator=C0293; target=iroK; function=-

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ECOCYC:G0-8897,GeneID:71004560`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:1196711-1196782:+; feature_type=gene
