---
entity_id: "gene.b4608"
entity_type: "gene"
name: "ohsC"
source_database: "NCBI RefSeq"
source_id: "gene-b4608"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4608"
  - "ohsC"
---

# ohsC

`gene.b4608`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4608`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ohsC (gene.b4608) is a gene entity. EcoCyc product frame: RNA0-330. EcoCyc synonyms: ryfC. Genomic coordinates: 2700520-2700598.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ohsC; function=+

## External IDs

- `Dbxref:ECOCYC:G0-10598,GeneID:5061518`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:2700520-2700598:+; feature_type=gene
