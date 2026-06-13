---
entity_id: "gene.b0504"
entity_type: "gene"
name: "allS"
source_database: "NCBI RefSeq"
source_id: "gene-b0504"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0504"
  - "allS"
---

# allS

`gene.b0504`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0504`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

allS (gene.b0504) is a gene entity. It encodes allS (protein.P0ACR0). Encoded protein function: FUNCTION: Positive regulator essential for the expression of allD operon. Binds to the allD promoter. {ECO:0000269|PubMed:12460564}. EcoCyc product frame: G6274-MONOMER. EcoCyc synonyms: ybbS, glxA1. Genomic coordinates: 531295-532221.

## Biological Role

Repressed by allR (protein.P0ACN4).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACR0|protein.P0ACR0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACN4|protein.P0ACN4]] `RegulonDB` `C` - regulator=AllR; target=allS; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001742,ECOCYC:G6274,GeneID:945139`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:531295-532221:-; feature_type=gene
