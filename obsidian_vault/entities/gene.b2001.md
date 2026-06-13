---
entity_id: "gene.b2001"
entity_type: "gene"
name: "yeeR"
source_database: "NCBI RefSeq"
source_id: "gene-b2001"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2001"
  - "yeeR"
---

# yeeR

`gene.b2001`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2001`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yeeR (gene.b2001) is a gene entity. It encodes yeeR (protein.P76361). Encoded protein function: Inner membrane protein YeeR EcoCyc product frame: G7081-MONOMER. Genomic coordinates: 2074779-2076311. EcoCyc protein note: Expression of yeeR is significantly increased in a gcvB mutant compared to wild type in E. coli NCM3722. The effect may be due to repression of a putative flu-yeeR operon by OxyR .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76361|protein.P76361]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006648,ECOCYC:G7081,GeneID:946512`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2074779-2076311:+; feature_type=gene
