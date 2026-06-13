---
entity_id: "gene.b0848"
entity_type: "gene"
name: "ybjM"
source_database: "NCBI RefSeq"
source_id: "gene-b0848"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0848"
  - "ybjM"
---

# ybjM

`gene.b0848`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0848`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybjM (gene.b0848) is a gene entity. It encodes ybjM (protein.P64439). Encoded protein function: Inner membrane protein YbjM EcoCyc product frame: G6446-MONOMER. Genomic coordinates: 890089-890466. EcoCyc protein note: YbjM is an inner membrane protein with four predicted transmembrane domains. The C terminus is located in the cytoplasm . Zheng et al. were not able to detect a transcript that would encode the YbjM protein; they propose the existence of an open reading frame on the opposite strand which may be encoded in an operon with grxA, and which shows OxyR-dependent induction of expression by hydrogen peroxide .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64439|protein.P64439]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002891,ECOCYC:G6446,GeneID:945477`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:890089-890466:+; feature_type=gene
