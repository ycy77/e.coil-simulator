---
entity_id: "gene.b4334"
entity_type: "gene"
name: "yjiL"
source_database: "NCBI RefSeq"
source_id: "gene-b4334"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4334"
  - "yjiL"
---

# yjiL

`gene.b4334`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4334`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjiL (gene.b4334) is a gene entity. It encodes yjiL (protein.P39383). Encoded protein function: Uncharacterized protein YjiL EcoCyc product frame: G7931-MONOMER. Genomic coordinates: 4563922-4564689. EcoCyc protein note: YjiL is implicated in the uptake of proline-rich antimicrobial peptides (PrAMPS) in cells lacking the peptide uptake permease, CPLX0-8097 "SbmA"

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39383|protein.P39383]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0014212,ECOCYC:G7931,GeneID:948837`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4563922-4564689:-; feature_type=gene
