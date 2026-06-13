---
entity_id: "gene.b0624"
entity_type: "gene"
name: "crcB"
source_database: "NCBI RefSeq"
source_id: "gene-b0624"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0624"
  - "crcB"
---

# crcB

`gene.b0624`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0624`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

crcB (gene.b0624) is a gene entity. It encodes fluC (protein.P37002). Encoded protein function: FUNCTION: Fluoride-specific ion channel (PubMed:25156118). Important for reducing fluoride concentration in the cell, thus reducing its toxicity (PubMed:22194412, PubMed:25156118). Required to counteract cytoplasmic fluoride accumulation driven by pH gradients across the bacterial inner membrane set up by mild acidification of the growth medium (PubMed:25156118). {ECO:0000269|PubMed:22194412, ECO:0000269|PubMed:25156118}. EcoCyc product frame: EG12209-MONOMER. EcoCyc synonyms: ybeI. Genomic coordinates: 657555-657938.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37002|protein.P37002]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002144,ECOCYC:EG12209,GeneID:945798`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:657555-657938:-; feature_type=gene
