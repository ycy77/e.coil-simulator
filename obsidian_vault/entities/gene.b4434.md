---
entity_id: "gene.b4434"
entity_type: "gene"
name: "azuR"
source_database: "NCBI RefSeq"
source_id: "gene-b4434"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4434"
  - "azuR"
---

# azuR

`gene.b4434`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4434`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

azuR (gene.b4434) is a gene entity. EcoCyc product frame: RNA0-430. EcoCyc synonyms: isrB, IS092, G0-8904. Genomic coordinates: 1987843-1988001.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=azuR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0047254,ECOCYC:G0-17112,GeneID:2847689`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:1987843-1988001:-; feature_type=gene
