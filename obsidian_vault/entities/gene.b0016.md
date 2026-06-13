---
entity_id: "gene.b0016"
entity_type: "gene"
name: "insL1"
source_database: "NCBI RefSeq"
source_id: "gene-b0016"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0016"
  - "insL1"
---

# insL1

`gene.b0016`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0016`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

insL1 (gene.b0016) is a gene entity. It encodes insL1 (protein.P0CF91). Encoded protein function: FUNCTION: Involved in the transposition of the insertion sequence IS186. EcoCyc product frame: G6083-MONOMER. EcoCyc synonyms: yi81-1. Genomic coordinates: 15445-16557. EcoCyc protein note: IS186 is an insertion sequence element that appears three times in a typical E. coli genome. IS186 is an insertion sequence element with an apparent preference for GC-rich sequences . As a consequence, it can insert at the tail end of cDNA clones . At the DNA level, the various IS186 genes have terminal inverted repeats and produce variable-length DNA duplications at the insertion site (10, 12 or 13 bp) .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0CF91|protein.P0CF91]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000058,ECOCYC:G6083,GeneID:944754`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:15445-16557:+; feature_type=gene
