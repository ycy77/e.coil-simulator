---
entity_id: "gene.b0128"
entity_type: "gene"
name: "yadH"
source_database: "NCBI RefSeq"
source_id: "gene-b0128"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0128"
  - "yadH"
---

# yadH

`gene.b0128`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0128`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yadH (gene.b0128) is a gene entity. It encodes yadH (protein.P0AFN6). Encoded protein function: Inner membrane transport permease YadH EcoCyc product frame: YADH-MONOMER. Genomic coordinates: 143702-144472. EcoCyc protein note: YadH is the predicted membrane-spanning subunit of a putative ATP-binding cassette (ABC) exporter complex .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFN6|protein.P0AFN6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000450,ECOCYC:EG12321,GeneID:944836`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:143702-144472:+; feature_type=gene
