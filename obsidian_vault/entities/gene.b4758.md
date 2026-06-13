---
entity_id: "gene.b4758"
entity_type: "gene"
name: "pspH"
source_database: "NCBI RefSeq"
source_id: "gene-b4758"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4758"
  - "pspH"
---

# pspH

`gene.b4758`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4758`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pspH (gene.b4758) is a gene entity. EcoCyc product frame: RNA0-400. Genomic coordinates: 4263139-4263249.

## Biological Role

Activated by rpoN (protein.P24255), pspF (protein.P37344).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=pspH; function=+
- `activates` <-- [[protein.P37344|protein.P37344]] `RegulonDB` `S` - regulator=PspF; target=pspH; function=+

## External IDs

- `Dbxref:ECOCYC:G0-16700,GeneID:63925664`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:4263139-4263249:+; feature_type=gene
