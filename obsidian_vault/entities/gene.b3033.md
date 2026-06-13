---
entity_id: "gene.b3033"
entity_type: "gene"
name: "yqiB"
source_database: "NCBI RefSeq"
source_id: "gene-b3033"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3033"
  - "yqiB"
---

# yqiB

`gene.b3033`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3033`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yqiB (gene.b3033) is a gene entity. It encodes yqiB (protein.P0ADU7). Encoded protein function: Uncharacterized protein YqiB EcoCyc product frame: G7580-MONOMER. EcoCyc synonyms: yzzH. Genomic coordinates: 3176858-3177280. EcoCyc protein note: A predicted deleterious SNP (Q117K) arose in yqiB during an experiment evaluating evolution of metabolic auxotrophy. A reconstructed strain containing only the YqiB Q117A allele was not an amino acid auxotroph, but had a fitness advantage compared to wild type when amino acids were present in the medium .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADU7|protein.P0ADU7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009959,ECOCYC:G7580,GeneID:947518`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3176858-3177280:-; feature_type=gene
