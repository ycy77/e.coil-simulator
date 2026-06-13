---
entity_id: "gene.b0718"
entity_type: "gene"
name: "ybgQ"
source_database: "NCBI RefSeq"
source_id: "gene-b0718"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0718"
  - "ybgQ"
---

# ybgQ

`gene.b0718`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0718`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybgQ (gene.b0718) is a gene entity. It encodes ybgQ (protein.P75750). Encoded protein function: FUNCTION: Could be involved in the export and assembly of the putative YbgD fimbrial subunit across the outer membrane. EcoCyc product frame: G6387-MONOMER. Genomic coordinates: 749722-752169. EcoCyc protein note: Sequence similarity suggests that YbgQ is a fimbrial usher protein . ybgOPQD is a putative chaperone-usher fimbrial operon . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including ybgOPQD. When this operon is removed, the cells are larger, produce polyhydroxyalkanoates (PHAs) and grows better, particularly in M9G media. A fimbrial-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised; it also grows faster and produces PHAs and had higher efficiency of glucose utilization .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75750|protein.P75750]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002446,ECOCYC:G6387,GeneID:946537`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:749722-752169:-; feature_type=gene
