---
entity_id: "gene.b0717"
entity_type: "gene"
name: "ybgP"
source_database: "NCBI RefSeq"
source_id: "gene-b0717"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0717"
  - "ybgP"
---

# ybgP

`gene.b0717`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0717`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybgP (gene.b0717) is a gene entity. It encodes ybgP (protein.P75749). Encoded protein function: FUNCTION: Could be required for the biogenesis of the putative YbgD fimbria. EcoCyc product frame: G6386-MONOMER. Genomic coordinates: 748979-749707. EcoCyc protein note: YbgP is a hypothetical protein. Sequence similarity suggests that it may be an outer membrane porin or a fimbrial subunit chaperone . ybgOPQD is a putative chaperone-usher fimbrial operon . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including ybgOPQD. When this operon is removed, the cells are larger, produce polyhydroxyalkanoates (PHAs) and grows better, particularly in M9G media. A fimbrial-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised; it also grows faster and produces PHAs and had higher efficiency of glucose utilization .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75749|protein.P75749]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002443,ECOCYC:G6386,GeneID:945110`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:748979-749707:-; feature_type=gene
