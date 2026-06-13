---
entity_id: "gene.b1811"
entity_type: "gene"
name: "yoaH"
source_database: "NCBI RefSeq"
source_id: "gene-b1811"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1811"
  - "yoaH"
---

# yoaH

`gene.b1811`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1811`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yoaH (gene.b1811) is a gene entity. It encodes yoaH (protein.P67338). Encoded protein function: UPF0181 protein YoaH EcoCyc product frame: G6995-MONOMER. Genomic coordinates: 1894552-1894731. EcoCyc protein note: No information about this protein was found by a literature search conducted on April 6, 2017.

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P67338|protein.P67338]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006026,ECOCYC:G6995,GeneID:946346`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1894552-1894731:-; feature_type=gene
