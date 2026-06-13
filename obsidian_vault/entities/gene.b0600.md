---
entity_id: "gene.b0600"
entity_type: "gene"
name: "ybdL"
source_database: "NCBI RefSeq"
source_id: "gene-b0600"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0600"
  - "ybdL"
---

# ybdL

`gene.b0600`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0600`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybdL (gene.b0600) is a gene entity. It encodes ybdL (protein.P77806). Encoded protein function: FUNCTION: Shows aminotransferase activity with methionine and histidine as substrates, and to a lesser extent also with phenylalanine. {ECO:0000269|PubMed:15280032}. EcoCyc product frame: G6329-MONOMER. Genomic coordinates: 633586-634746.

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77806|protein.P77806]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002069,ECOCYC:G6329,GeneID:945211`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:633586-634746:+; feature_type=gene
