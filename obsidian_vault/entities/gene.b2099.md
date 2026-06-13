---
entity_id: "gene.b2099"
entity_type: "gene"
name: "yegU"
source_database: "NCBI RefSeq"
source_id: "gene-b2099"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2099"
  - "yegU"
---

# yegU

`gene.b2099`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2099`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yegU (gene.b2099) is a gene entity. It encodes yegU (protein.P76418). Encoded protein function: Putative ADP-ribosylglycohydrolase YegU (EC 3.2.2.-) EcoCyc product frame: G7131-MONOMER. Genomic coordinates: 2180095-2181099. EcoCyc protein note: The products of yegT, yegU, and yegV are implicated in glycogen accumulation .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76418|protein.P76418]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006948,ECOCYC:G7131,GeneID:946630`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2180095-2181099:+; feature_type=gene
