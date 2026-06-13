---
entity_id: "gene.b2876"
entity_type: "gene"
name: "yqeC"
source_database: "NCBI RefSeq"
source_id: "gene-b2876"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2876"
  - "yqeC"
---

# yqeC

`gene.b2876`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2876`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yqeC (gene.b2876) is a gene entity. It encodes yqeC (protein.Q46809). Encoded protein function: Uncharacterized protein YqeC EcoCyc product frame: G7495-MONOMER. Genomic coordinates: 3014287-3015057. EcoCyc protein note: Partial phylogenetic profiling suggested that yqeC belongs to a system connected to selenium-dependent molybdenum hydroxylases .

## Biological Role

Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46809|protein.Q46809]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009443,ECOCYC:G7495,GeneID:947350`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3014287-3015057:-; feature_type=gene
