---
entity_id: "gene.b4456"
entity_type: "gene"
name: "glmZ"
source_database: "NCBI RefSeq"
source_id: "gene-b4456"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4456"
  - "glmZ"
---

# glmZ

`gene.b4456`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4456`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glmZ (gene.b4456) is a gene entity. EcoCyc product frame: SRAJ-RNA. EcoCyc synonyms: psrA20, sraJ, k19, ryiA. Genomic coordinates: 3986432-3986603.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=glmZ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0047274,ECOCYC:G0-8873,GeneID:2847678`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:3986432-3986603:+; feature_type=gene
