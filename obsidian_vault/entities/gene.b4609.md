---
entity_id: "gene.b4609"
entity_type: "gene"
name: "ryfD"
source_database: "NCBI RefSeq"
source_id: "gene-b4609"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4609"
  - "ryfD"
---

# ryfD

`gene.b4609`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4609`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ryfD (gene.b4609) is a gene entity. EcoCyc product frame: RNA0-331. Genomic coordinates: 2734153-2734295.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ryfD; function=+

## External IDs

- `Dbxref:ECOCYC:G0-10600,GeneID:5061506`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:2734153-2734295:-; feature_type=gene
