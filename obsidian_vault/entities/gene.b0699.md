---
entity_id: "gene.b0699"
entity_type: "gene"
name: "ybfA"
source_database: "NCBI RefSeq"
source_id: "gene-b0699"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0699"
  - "ybfA"
---

# ybfA

`gene.b0699`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0699`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybfA (gene.b0699) is a gene entity. It encodes ybfA (protein.P0AAU2). Encoded protein function: Uncharacterized protein YbfA EcoCyc product frame: EG11521-MONOMER. Genomic coordinates: 729134-729340. EcoCyc protein note: A ybfA deletion mutant is 12-fold more sensitive to X-radiation and 3-fold more sensitive to UV-radiation than wild type .

## Biological Role

Activated by arcA (protein.P0A9Q1).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAU2|protein.P0AAU2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=ybfA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002386,ECOCYC:EG11521,GeneID:947452`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:729134-729340:+; feature_type=gene
