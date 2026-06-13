---
entity_id: "gene.b4416"
entity_type: "gene"
name: "rybA"
source_database: "NCBI RefSeq"
source_id: "gene-b4416"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4416"
  - "rybA"
---

# rybA

`gene.b4416`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4416`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rybA (gene.b4416) is a gene entity. EcoCyc product frame: RYBA-RNA. Genomic coordinates: 852725-853064.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rybA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0047240,ECOCYC:G0-8881,GeneID:2847681`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:852725-853064:-; feature_type=gene
