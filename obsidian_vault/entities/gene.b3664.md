---
entity_id: "gene.b3664"
entity_type: "gene"
name: "adeQ"
source_database: "NCBI RefSeq"
source_id: "gene-b3664"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3664"
  - "adeQ"
---

# adeQ

`gene.b3664`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3664`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

adeQ (gene.b3664) is a gene entity. It encodes adeQ (protein.P31440). Encoded protein function: FUNCTION: High-affinity transporter for adenine. {ECO:0000269|PubMed:24214977}. EcoCyc product frame: EG11691-MONOMER. EcoCyc synonyms: yicO. Genomic coordinates: 3842455-3843789. EcoCyc protein note: AdeQ is a high-affinity adenine transporter in E. coli K-12. Cloned and overexpressed AdeQ transports labelled adenine but not guanine, hypoxanthine, xanthine, uric acid or uracil in an E. coli ΔpurP strain . AdeQ is a member of the nucleobase:cation symporter 2 (NCS2) family of transporters . Transcription is regulated by BaeR, which plays a role in novobiocin and deoxycholate resistance . adeQ: adenine permease

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31440|protein.P31440]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011975,ECOCYC:EG11691,GeneID:948174`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3842455-3843789:-; feature_type=gene
