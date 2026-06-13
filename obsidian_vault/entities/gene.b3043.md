---
entity_id: "gene.b3043"
entity_type: "gene"
name: "ygiL"
source_database: "NCBI RefSeq"
source_id: "gene-b3043"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3043"
  - "ygiL"
---

# ygiL

`gene.b3043`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3043`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygiL (gene.b3043) is a gene entity. It encodes ygiL (protein.P39834). Encoded protein function: Uncharacterized fimbrial-like protein YgiL EcoCyc product frame: EG12363-MONOMER. Genomic coordinates: 3185414-3185965. EcoCyc protein note: E. coli K-12 contains 12 chaperone-usher fimbrial operons, including ygiLyqiGHI; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised .

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39834|protein.P39834]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ygiL; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009992,ECOCYC:EG12363,GeneID:947522`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3185414-3185965:+; feature_type=gene
