---
entity_id: "gene.b4449"
entity_type: "gene"
name: "sraG"
source_database: "NCBI RefSeq"
source_id: "gene-b4449"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4449"
  - "sraG"
---

# sraG

`gene.b4449`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4449`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sraG (gene.b4449) is a gene entity. EcoCyc product frame: SRAG-RNA. EcoCyc synonyms: psrA15, p3, psrO. Genomic coordinates: 3311183-3311398.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=sraG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0047269,ECOCYC:G0-8870,GeneID:2847685`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:3311183-3311398:+; feature_type=gene
