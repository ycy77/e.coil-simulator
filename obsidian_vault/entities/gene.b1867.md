---
entity_id: "gene.b1867"
entity_type: "gene"
name: "yecD"
source_database: "NCBI RefSeq"
source_id: "gene-b1867"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1867"
  - "yecD"
---

# yecD

`gene.b1867`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1867`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yecD (gene.b1867) is a gene entity. It encodes yecD (protein.P0ADI7). Encoded protein function: Isochorismatase family protein YecD (EC 3.-.-.-) EcoCyc product frame: EG12378-MONOMER. Genomic coordinates: 1950832-1951398. EcoCyc protein note: No information about this protein was found by a literature search conducted on July 3, 2019.

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADI7|protein.P0ADI7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yecD; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006231,ECOCYC:EG12378,GeneID:946384`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1950832-1951398:+; feature_type=gene
