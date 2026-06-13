---
entity_id: "gene.b2136"
entity_type: "gene"
name: "yohD"
source_database: "NCBI RefSeq"
source_id: "gene-b2136"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2136"
  - "yohD"
---

# yohD

`gene.b2136`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2136`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yohD (gene.b2136) is a gene entity. It encodes yohD (protein.P33366). Encoded protein function: Inner membrane protein YohD EcoCyc product frame: EG12017-MONOMER. Genomic coordinates: 2225801-2226379. EcoCyc protein note: YohD is predicted to be an inner membrane protein with four transmembrane domains; topology analysis suggests the C-terminus is located in the cytoplasm . A yghB yqjA double mutant is temperature sensitive for growth, forms chains of cells at permissive temperatures, and can be complemented by yghB, yqjA, yohD, or yabI expressed from a plasmid . YohD is a member of the DedA family of inner membrane proteins . E. coli K-12 contains 7 other DedA family members, namely EG10216 "DedA", EG11824 "YghB", EG11571 "YabI", G7609-MONOMER "YqjA", G7407 "YqaA", G6945-MONOMER "YdjX" and G6947 "YdjZ". Collectively, the DedA family is essential in E. coli K-12 .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33366|protein.P33366]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007059,ECOCYC:EG12017,GeneID:946661`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2225801-2226379:+; feature_type=gene
