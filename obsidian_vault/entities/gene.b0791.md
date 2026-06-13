---
entity_id: "gene.b0791"
entity_type: "gene"
name: "ybhQ"
source_database: "NCBI RefSeq"
source_id: "gene-b0791"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0791"
  - "ybhQ"
---

# ybhQ

`gene.b0791`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0791`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybhQ (gene.b0791) is a gene entity. It encodes ybhQ (protein.P0AAW5). Encoded protein function: Inner membrane protein YbhQ EcoCyc product frame: G6408-MONOMER. Genomic coordinates: 824630-825040. EcoCyc protein note: YbhQ is an inner membrane protein with four predicted transmembrane domains. The C terminus is located in the cytoplasm .

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAW5|protein.P0AAW5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002699,ECOCYC:G6408,GeneID:945405`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:824630-825040:+; feature_type=gene
