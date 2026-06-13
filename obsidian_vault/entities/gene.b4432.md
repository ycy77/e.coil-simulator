---
entity_id: "gene.b4432"
entity_type: "gene"
name: "ryeA"
source_database: "NCBI RefSeq"
source_id: "gene-b4432"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4432"
  - "ryeA"
---

# ryeA

`gene.b4432`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4432`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ryeA (gene.b4432) is a gene entity. EcoCyc product frame: RYEA-RNA. EcoCyc synonyms: sraC, psrA8, tkpe79, IS091. Genomic coordinates: 1923066-1923337.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ryeA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0047252,ECOCYC:G0-8865,GeneID:2847771`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:1923066-1923337:+; feature_type=gene
