---
entity_id: "gene.b0304"
entity_type: "gene"
name: "rclA"
source_database: "NCBI RefSeq"
source_id: "gene-b0304"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0304"
  - "rclA"
---

# rclA

`gene.b0304`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0304`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rclA (gene.b0304) is a gene entity. It encodes rclA (protein.P77212). Encoded protein function: FUNCTION: Probably involved in reactive chlorine species (RCS) stress resistance. {ECO:0000269|PubMed:24078635}. EcoCyc product frame: G6174-MONOMER. EcoCyc synonyms: ykgC. Genomic coordinates: 318676-320001.

## Biological Role

Activated by rclR (protein.P77379).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77212|protein.P77212]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P77379|protein.P77379]] `RegulonDB` `S` - regulator=RclR; target=rclA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001048,ECOCYC:G6174,GeneID:946092`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:318676-320001:-; feature_type=gene
