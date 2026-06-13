---
entity_id: "gene.b0803"
entity_type: "gene"
name: "ybiI"
source_database: "NCBI RefSeq"
source_id: "gene-b0803"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0803"
  - "ybiI"
---

# ybiI

`gene.b0803`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0803`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybiI (gene.b0803) is a gene entity. It encodes ybiI (protein.P41039). Encoded protein function: Uncharacterized protein YbiI EcoCyc product frame: EG12421-MONOMER. Genomic coordinates: 838190-838456. EcoCyc protein note: An unpublished solution structure of YbiI is available. No information about this protein was found by a literature search conducted on March 15, 2017.

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P41039|protein.P41039]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002744,ECOCYC:EG12421,GeneID:945434`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:838190-838456:-; feature_type=gene
