---
entity_id: "gene.b0265"
entity_type: "gene"
name: "insA2"
source_database: "NCBI RefSeq"
source_id: "gene-b0265"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0265"
  - "insA2"
---

# insA2

`gene.b0265`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0265`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

insA2 (gene.b0265) is a gene entity. It encodes insA2 (protein.P0CF08). Encoded protein function: FUNCTION: Absolutely required for transposition of IS1. EcoCyc product frame: G6139-MONOMER. Genomic coordinates: 279600-279875. EcoCyc protein note: IS1 is the smallest insertion sequence in E. coli. It codes for three proteins, InsA, InsB and InsAB'. InsAB' is the transposase for IS1 . Its translation depends on a -1 frameshift within the 3' end region of insA which allows translational readthrough into insB . In the absence of this frameshift, the IS1 transcriptional repressor protein InsA is produced instead .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0CF08|protein.P0CF08]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000909,ECOCYC:G6139,GeneID:944946`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:279600-279875:-; feature_type=gene
