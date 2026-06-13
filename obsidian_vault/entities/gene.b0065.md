---
entity_id: "gene.b0065"
entity_type: "gene"
name: "yabI"
source_database: "NCBI RefSeq"
source_id: "gene-b0065"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0065"
  - "yabI"
---

# yabI

`gene.b0065`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0065`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yabI (gene.b0065) is a gene entity. It encodes yabI (protein.P30149). Encoded protein function: Inner membrane protein YabI EcoCyc product frame: EG11571-MONOMER. Genomic coordinates: 71351-72115. EcoCyc protein note: YabI is a member of the DedA family of inner membrane proteins . E. coli K-12 contains 7 other DedA family members, namely EG10216 "DedA", EG11824 "YghB", G7609-MONOMER "YqjA", EG12017 "YohD", G7407 "YqaA", G6945-MONOMER "YdjX" and G6947 "YdjZ". Collectively, the DedA family is essential in E. coli K-12 . YabI is predicted to be an inner membrane protein with five transmembrane domains; topology analysis suggests the C-terminus is located in the periplasm . The yabI gene may have a σ54-dependent promoter . Expression of yabI is induced by AI-2 quorum signaling . A yghB yqjA double mutant is temperature sensitive for growth, forms chains of cells at permissive temperatures, and can be complemented by yghB, yqjA, yohD, or yabI expressed from a plasmid . yabI insertion mutants were identified in a genetic screen for genes that are important for survival of exposure to ionizing radiation (IR). A yabI deletion mutant has a modest decrease in IR survival .

## Biological Role

Activated by rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30149|protein.P30149]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=yabI; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000241,ECOCYC:EG11571,GeneID:944783`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:71351-72115:+; feature_type=gene
