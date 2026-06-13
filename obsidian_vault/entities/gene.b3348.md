---
entity_id: "gene.b3348"
entity_type: "gene"
name: "slyX"
source_database: "NCBI RefSeq"
source_id: "gene-b3348"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3348"
  - "slyX"
---

# slyX

`gene.b3348`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3348`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

slyX (gene.b3348) is a gene entity. It encodes slyX (protein.P0A8R4). Encoded protein function: Protein SlyX EcoCyc product frame: EG11664-MONOMER. Genomic coordinates: 3477640-3477858. EcoCyc protein note: slyX does not complement the slyD1 defect for cell lysis by φX174 .

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8R4|protein.P0A8R4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010944,ECOCYC:EG11664,GeneID:947849`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3477640-3477858:+; feature_type=gene
