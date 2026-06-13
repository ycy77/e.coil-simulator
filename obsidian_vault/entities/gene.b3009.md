---
entity_id: "gene.b3009"
entity_type: "gene"
name: "yghB"
source_database: "NCBI RefSeq"
source_id: "gene-b3009"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3009"
  - "yghB"
---

# yghB

`gene.b3009`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3009`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yghB (gene.b3009) is a gene entity. It encodes yghB (protein.P0AA60). Encoded protein function: FUNCTION: May be a membrane transporter required for proton motive force (PMF)-dependent drug efflux. Required, with YqjA, for the proper export of certain periplasmic amidases and, possibly, other Tat substrates. May play a role in determining membrane lipid composition. {ECO:0000269|PubMed:18456815, ECO:0000269|PubMed:19880597, ECO:0000269|PubMed:24277026}. EcoCyc product frame: EG11824-MONOMER. Genomic coordinates: 3153563-3154222. EcoCyc protein note: YghB is predicted to be an inner membrane protein with four transmembrane domains; topology analysis suggests the C-terminus is located in the cytoplasm . A yghB yqjA double null strain has a synthetic growth defect at elevated temperatures, forms chains of cells at permissive temperatures, and can be complemented by yghB, yqjA, yohD, or yabI expressed from a plasmid . The double and single mutants displayed altered phospholipid compositions . An E. coli ΔyghB ΔyqjA strain is hypersensitive to a number of structurally diverse drugs and dyes including ethidium bromide, methyl viologen, acriflavine, nalidixic acid and β-lactam antibiotics. A wild-type response is restored by expression of yghB from a plasmid...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA60|protein.P0AA60]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009882,ECOCYC:EG11824,GeneID:947490`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3153563-3154222:+; feature_type=gene
