---
entity_id: "gene.b2490"
entity_type: "gene"
name: "hyfJ"
source_database: "NCBI RefSeq"
source_id: "gene-b2490"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2490"
  - "hyfJ"
---

# hyfJ

`gene.b2490`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2490`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hyfJ (gene.b2490) is a gene entity. It encodes hyfJ (protein.P77453). Encoded protein function: FUNCTION: Possible component of hydrogenase 4. {ECO:0000305|PubMed:9387241}. EcoCyc product frame: G7307-MONOMER. Genomic coordinates: 2611457-2611870. EcoCyc protein note: The hyfJ gene is part of the hyf operon, and expression of adjacent genes may be translationally coupled . HyfJ shares 45% overall amino acid sequence identity with EG10481-MONOMER "HycH" and the two proteins may share overlapping functions .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77453|protein.P77453]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008200,ECOCYC:G7307,GeneID:947713`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2611457-2611870:+; feature_type=gene
