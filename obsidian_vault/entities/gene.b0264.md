---
entity_id: "gene.b0264"
entity_type: "gene"
name: "insB2"
source_database: "NCBI RefSeq"
source_id: "gene-b0264"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0264"
  - "insB2"
---

# insB2

`gene.b0264`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0264`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

insB2 (gene.b0264) is a gene entity. It encodes insB2 (protein.P0CF26). Encoded protein function: FUNCTION: Absolutely required for transposition of IS1. EcoCyc product frame: G6138-MONOMER. Genomic coordinates: 279178-279681. EcoCyc protein note: IS1 is the smallest insertion sequence in E. coli. It codes for three proteins, InsA, InsB and InsAB'. InsAB' is the transposase for IS1 . Its translation depends on a -1 frameshift within the 3' end region of insA which allows translational readthrough into insB . In the absence of this frameshift, the IS1 transcriptional repressor protein InsA is produced instead .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0CF26|protein.P0CF26]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000906,ECOCYC:G6138,GeneID:947698`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:279178-279681:-; feature_type=gene
