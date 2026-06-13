---
entity_id: "gene.b3602"
entity_type: "gene"
name: "yibL"
source_database: "NCBI RefSeq"
source_id: "gene-b3602"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3602"
  - "yibL"
---

# yibL

`gene.b3602`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3602`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yibL (gene.b3602) is a gene entity. It encodes yibL (protein.P0ADK8). Encoded protein function: Uncharacterized protein YibL EcoCyc product frame: EG11964-MONOMER. Genomic coordinates: 3776665-3777027. EcoCyc protein note: YibL was found to associate with the 50S subunit of the ribosome .

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADK8|protein.P0ADK8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011773,ECOCYC:EG11964,GeneID:948115`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3776665-3777027:+; feature_type=gene
