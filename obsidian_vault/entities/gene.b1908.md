---
entity_id: "gene.b1908"
entity_type: "gene"
name: "yecA"
source_database: "NCBI RefSeq"
source_id: "gene-b1908"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1908"
  - "yecA"
---

# yecA

`gene.b1908`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1908`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yecA (gene.b1908) is a gene entity. It encodes yecA (protein.P0AD05). Encoded protein function: Uncharacterized protein YecA EcoCyc product frame: EG11139-MONOMER. Genomic coordinates: 1990954-1991619. EcoCyc protein note: YecA contains a SecA-like metal binding domain and co-purifies with iron .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD05|protein.P0AD05]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006357,ECOCYC:EG11139,GeneID:945061`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1990954-1991619:-; feature_type=gene
