---
entity_id: "gene.b4413"
entity_type: "gene"
name: "sokC"
source_database: "NCBI RefSeq"
source_id: "gene-b4413"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4413"
  - "sokC"
---

# sokC

`gene.b4413`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4413`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sokC (gene.b4413) is a gene entity. EcoCyc product frame: RNA0-141. EcoCyc synonyms: sof. Genomic coordinates: 16952-17010.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=sokC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0047238,ECOCYC:G0-9581,GeneID:2847745`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:16952-17010:+; feature_type=gene
