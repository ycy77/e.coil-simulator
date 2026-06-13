---
entity_id: "gene.b4730"
entity_type: "gene"
name: "yahV"
source_database: "NCBI RefSeq"
source_id: "gene-b4730"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4730"
  - "yahV"
---

# yahV

`gene.b4730`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4730`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yahV (gene.b4730) is a gene entity. It encodes yahV (protein.P0DPN0). Encoded protein function: Protein YahV EcoCyc product frame: MONOMER0-4407. Genomic coordinates: 331802-331876. EcoCyc protein note: YahV was identified as a previously unannotated small protein; its expression is higher during exponential phase than during stationary phase . Based on co-occurrence literature analysis among E. coli K-12 strains in addition to genomic co-localization and sequence analysis, yahV is hypothesized to be a membrane-bound small protein that may help stabilize membranes during osmotic shock .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DPN0|protein.P0DPN0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ECOCYC:G0-16725,GeneID:38094940`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:331802-331876:+; feature_type=gene
