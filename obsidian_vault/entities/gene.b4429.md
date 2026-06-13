---
entity_id: "gene.b4429"
entity_type: "gene"
name: "sokB"
source_database: "NCBI RefSeq"
source_id: "gene-b4429"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4429"
  - "sokB"
---

# sokB

`gene.b4429`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4429`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sokB (gene.b4429) is a gene entity. EcoCyc product frame: RNA0-165. Genomic coordinates: 1492119-1492175.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=sokB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0047249,ECOCYC:G0-9611,GeneID:2847728`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:1492119-1492175:+; feature_type=gene
