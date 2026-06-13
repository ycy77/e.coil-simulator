---
entity_id: "gene.b2033"
entity_type: "gene"
name: "wbbJ"
source_database: "NCBI RefSeq"
source_id: "gene-b2033"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2033"
  - "wbbJ"
---

# wbbJ

`gene.b2033`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2033`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

wbbJ (gene.b2033) is a gene entity. It encodes wbbJ (protein.P37750). Encoded protein function: FUNCTION: Putative O-acetyltransferase that transfers an O-acetyl group to the O antigen. EcoCyc product frame: EG11984-MONOMER. EcoCyc synonyms: yefH. Genomic coordinates: 2104494-2105084. EcoCyc protein note: wbbJ is predicted to encode an O-acetyltransferase involved in the biosynthesis of O-antigen repeat units (see ). E. coli K-12 is phenotypically rough and does not express O-antigen due to mutations in the rfb region; E. coli K-12 MG1655 contains the rfb-50 mutation - an IS5 element which disrupts EG11986 wbbL encoding rhamnose transferase; an engineered strain of E. coli K-12 with all rfb genes intact synthesizes CPD0-2249 O16 antigen . For information on bacterial polysaccharide gene nomenclature see .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37750|protein.P37750]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006749,ECOCYC:EG11984,GeneID:946556`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2104494-2105084:-; feature_type=gene
