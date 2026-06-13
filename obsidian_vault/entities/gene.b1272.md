---
entity_id: "gene.b1272"
entity_type: "gene"
name: "sohB"
source_database: "NCBI RefSeq"
source_id: "gene-b1272"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1272"
  - "sohB"
---

# sohB

`gene.b1272`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1272`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sohB (gene.b1272) is a gene entity. It encodes sohB (protein.P0AG14). Encoded protein function: FUNCTION: Multicopy suppressor of the HtrA (DegP) null phenotype. It is possibly a protease, not essential for bacterial viability. EcoCyc product frame: EG10956-MONOMER. Genomic coordinates: 1329332-1330381. EcoCyc protein note: SohB is an inner membrane protein with similarity to the signal peptide peptidase CPLX0-2941 "protease IV" . It contains one predicted transmembrane domain; the C terminus is located in the cytoplasm . SohB is subject to posttranslational processing of a signal sequence; the precursor is 39 kDa and the mature protein is 37 kDa . Multicopy expression of sohB suppresses the heat sensitivity of an EG10463 htrA mutant . SohB: "suppressor of htrA B"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG14|protein.P0AG14]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004267,ECOCYC:EG10956,GeneID:945858`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1329332-1330381:+; feature_type=gene
