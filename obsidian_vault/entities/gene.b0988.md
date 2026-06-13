---
entity_id: "gene.b0988"
entity_type: "gene"
name: "insB4"
source_database: "NCBI RefSeq"
source_id: "gene-b0988"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0988"
  - "insB4"
---

# insB4

`gene.b0988`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0988`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

insB4 (gene.b0988) is a gene entity. It encodes insB4 (protein.P57998). Encoded protein function: FUNCTION: Absolutely required for transposition of IS1. EcoCyc product frame: G6509-MONOMER. Genomic coordinates: 1050027-1050530. EcoCyc protein note: IS1 is the smallest insertion sequence in E. coli. It codes for three proteins, InsA, InsB and InsAB'. InsAB' is the transposase for IS1 . Its translation depends on a -1 frameshift within the 3' end region of insA which allows translational readthrough into insB . In the absence of this frameshift, the IS1 transcriptional repressor protein InsA is produced instead .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P57998|protein.P57998]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003338,ECOCYC:G6509,GeneID:945009`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1050027-1050530:+; feature_type=gene
