---
entity_id: "gene.b2998"
entity_type: "gene"
name: "yghW"
source_database: "NCBI RefSeq"
source_id: "gene-b2998"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2998"
  - "yghW"
---

# yghW

`gene.b2998`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2998`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yghW (gene.b2998) is a gene entity. It encodes yghW (protein.P64574). Encoded protein function: Uncharacterized protein YghW EcoCyc product frame: G7555-MONOMER. Genomic coordinates: 3146450-3146737. EcoCyc protein note: yghW expression is down regulated in an E. coli K-12 strain engineered for increased tolerance to n-butanol; a ΔyghW strain has increased n-butanol tolerance and an increased proportion of unsaturated fatty acids (especially palmitoleic and oleic acid) in total fatty acids compared to wild type .

## Biological Role

Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64574|protein.P64574]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009839,ECOCYC:G7555,GeneID:947485`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3146450-3146737:-; feature_type=gene
