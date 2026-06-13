---
entity_id: "gene.b3240"
entity_type: "gene"
name: "aaeB"
source_database: "NCBI RefSeq"
source_id: "gene-b3240"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3240"
  - "aaeB"
---

# aaeB

`gene.b3240`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3240`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aaeB (gene.b3240) is a gene entity. It encodes aaeB (protein.P46481). Encoded protein function: FUNCTION: Forms an efflux pump with AaeA. Could function as a metabolic relief valve, allowing to eliminate certain compounds when they accumulate to high levels in the cell. Substrates are p-hydroxybenzoic acid (pHBA), 6-hydroxy-2-naphthoic and 2-hydroxycinnamate. {ECO:0000255|HAMAP-Rule:MF_01545, ECO:0000269|PubMed:15489430}. EcoCyc product frame: G7685-MONOMER. EcoCyc synonyms: yhcP. Genomic coordinates: 3386221-3388188.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P46481|protein.P46481]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010629,ECOCYC:G7685,GeneID:947747`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3386221-3388188:-; feature_type=gene
