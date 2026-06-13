---
entity_id: "gene.b1870"
entity_type: "gene"
name: "cmoA"
source_database: "NCBI RefSeq"
source_id: "gene-b1870"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1870"
  - "cmoA"
---

# cmoA

`gene.b1870`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1870`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cmoA (gene.b1870) is a gene entity. It encodes cmoA (protein.P76290). Encoded protein function: FUNCTION: Catalyzes the conversion of S-adenosyl-L-methionine (SAM) to carboxy-S-adenosyl-L-methionine (Cx-SAM). {ECO:0000255|HAMAP-Rule:MF_01589, ECO:0000269|PubMed:23676670}. EcoCyc product frame: G7020-MONOMER. EcoCyc synonyms: yecO. Genomic coordinates: 1952702-1953445.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76290|protein.P76290]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006237,ECOCYC:G7020,GeneID:946380`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1952702-1953445:+; feature_type=gene
