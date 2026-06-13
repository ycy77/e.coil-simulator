---
entity_id: "gene.b4760"
entity_type: "gene"
name: "rirA"
source_database: "NCBI RefSeq"
source_id: "gene-b4760"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4760"
  - "rirA"
---

# rirA

`gene.b4760`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4760`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rirA (gene.b4760) is a gene entity. EcoCyc product frame: RNA0-390. Genomic coordinates: 3808166-3808238.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=rirA; function=+

## External IDs

- `Dbxref:ECOCYC:G0-16662,GeneID:63925660`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:3808166-3808238:-; feature_type=gene
