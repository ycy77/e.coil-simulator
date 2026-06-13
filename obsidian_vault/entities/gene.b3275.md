---
entity_id: "gene.b3275"
entity_type: "gene"
name: "rrlD"
source_database: "NCBI RefSeq"
source_id: "gene-b3275"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3275"
  - "rrlD"
---

# rrlD

`gene.b3275`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3275`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rrlD (gene.b3275) is a gene entity. EcoCyc product frame: RRLD-RRNA. Genomic coordinates: 3423880-3426783.

## Biological Role

Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rrlD; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=rrlD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010746,ECOCYC:EG30080,GeneID:947773`
- `gbkey:Gene`
- `gene_biotype:rRNA`

## Notes

NC_000913.3:3423880-3426783:-; feature_type=gene
