---
entity_id: "gene.b3888"
entity_type: "gene"
name: "fabY"
source_database: "NCBI RefSeq"
source_id: "gene-b3888"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3888"
  - "fabY"
---

# fabY

`gene.b3888`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3888`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fabY (gene.b3888) is a gene entity. It encodes fabY (protein.P0ADQ2). Encoded protein function: FUNCTION: Supports initiation of fatty acid biosynthesis in the absence of FabH. {ECO:0000269|PubMed:31331975}. EcoCyc product frame: EG11853-MONOMER. EcoCyc synonyms: yiiD, fabY. Genomic coordinates: 4077449-4078438.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADQ2|protein.P0ADQ2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012692,ECOCYC:EG11853,GeneID:948387`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4077449-4078438:+; feature_type=gene
