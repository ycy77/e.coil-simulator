---
entity_id: "gene.b0022"
entity_type: "gene"
name: "insA1"
source_database: "NCBI RefSeq"
source_id: "gene-b0022"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0022"
  - "insA1"
---

# insA1

`gene.b0022`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0022`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

insA1 (gene.b0022) is a gene entity. It encodes insA1 (protein.P0CF07). Encoded protein function: FUNCTION: Absolutely required for transposition of IS1. EcoCyc product frame: G6086-MONOMER. Genomic coordinates: 20233-20508. EcoCyc protein note: IS1 is the smallest insertion sequence in E. coli. It codes for three proteins, InsA, InsB and InsAB'. InsAB' is the transposase for IS1 . Its translation depends on a -1 frameshift within the 3' end region of insA which allows translational readthrough into insB . In the absence of this frameshift, the IS1 transcriptional repressor protein InsA is produced instead .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0CF07|protein.P0CF07]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000078,ECOCYC:G6086,GeneID:948449`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:20233-20508:-; feature_type=gene
