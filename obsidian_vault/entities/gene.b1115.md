---
entity_id: "gene.b1115"
entity_type: "gene"
name: "ycfT"
source_database: "NCBI RefSeq"
source_id: "gene-b1115"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1115"
  - "ycfT"
---

# ycfT

`gene.b1115`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1115`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycfT (gene.b1115) is a gene entity. It encodes ycfT (protein.P75955). Encoded protein function: Inner membrane protein YcfT EcoCyc product frame: G6572-MONOMER. Genomic coordinates: 1174092-1175165. EcoCyc protein note: Membrane topology predictions using experimentally determined C terminus locations indicate that YcfT has 8 transmembrane helices and the C-terminus is located in the cytoplasm . ycfT is induced upon deletion of tqsA, which controls biofilm development by influencing the export of autoinducer 2 .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75955|protein.P75955]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003767,ECOCYC:G6572,GeneID:945679`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1174092-1175165:-; feature_type=gene
