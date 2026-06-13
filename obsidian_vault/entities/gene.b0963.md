---
entity_id: "gene.b0963"
entity_type: "gene"
name: "mgsA"
source_database: "NCBI RefSeq"
source_id: "gene-b0963"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0963"
  - "mgsA"
---

# mgsA

`gene.b0963`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0963`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mgsA (gene.b0963) is a gene entity. It encodes mgsA (protein.P0A731). Encoded protein function: FUNCTION: Catalyzes the formation of methylglyoxal from dihydroxyacetone phosphate. {ECO:0000255|HAMAP-Rule:MF_00549, ECO:0000269|PubMed:11389594, ECO:0000269|PubMed:15049687, ECO:0000269|PubMed:9665712}. EcoCyc product frame: METHGLYSYN-MONOMER. EcoCyc synonyms: mgs, yccG. Genomic coordinates: 1026557-1027015.

## Enriched Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A731|protein.P0A731]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003259,ECOCYC:G6497,GeneID:945574`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1026557-1027015:-; feature_type=gene
