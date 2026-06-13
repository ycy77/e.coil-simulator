---
entity_id: "gene.b0487"
entity_type: "gene"
name: "cueR"
source_database: "NCBI RefSeq"
source_id: "gene-b0487"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0487"
  - "cueR"
---

# cueR

`gene.b0487`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0487`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cueR (gene.b0487) is a gene entity. It encodes cueR (protein.P0A9G4). Encoded protein function: FUNCTION: Regulates the transcription of the copA and cueO genes. It detects cytoplasmic copper stress and activates transcription in response to increasing copper concentrations. {ECO:0000269|PubMed:10915804, ECO:0000269|PubMed:11167016, ECO:0000269|PubMed:11399769}. EcoCyc product frame: G6263-MONOMER. EcoCyc synonyms: copR, ybbI. Genomic coordinates: 513993-514400.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9G4|protein.P0A9G4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001693,ECOCYC:G6263,GeneID:945332`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:513993-514400:+; feature_type=gene
