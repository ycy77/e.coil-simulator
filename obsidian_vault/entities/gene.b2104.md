---
entity_id: "gene.b2104"
entity_type: "gene"
name: "thiM"
source_database: "NCBI RefSeq"
source_id: "gene-b2104"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2104"
  - "thiM"
---

# thiM

`gene.b2104`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2104`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

thiM (gene.b2104) is a gene entity. It encodes thiM (protein.P76423). Encoded protein function: FUNCTION: Catalyzes the phosphorylation of the hydroxyl group of 4-methyl-5-beta-hydroxyethylthiazole (THZ). {ECO:0000255|HAMAP-Rule:MF_00228, ECO:0000269|PubMed:2542220}. EcoCyc product frame: THZ-KIN-MONOMER. Genomic coordinates: 2184513-2185301.

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76423|protein.P76423]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006960,ECOCYC:M007,GeneID:945142`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2184513-2185301:-; feature_type=gene
