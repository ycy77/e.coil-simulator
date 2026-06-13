---
entity_id: "gene.b4342"
entity_type: "gene"
name: "yjiT"
source_database: "NCBI RefSeq"
source_id: "gene-b4342"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4342"
  - "yjiT"
---

# yjiT

`gene.b4342`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4342`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjiT (gene.b4342) is a gene entity. It encodes yjiT (protein.P39391). Encoded protein function: Protein YjiT EcoCyc product frame: G7938-MONOMER. Genomic coordinates: 4572414-4573931. EcoCyc protein note: No information about this protein was found by a literature search conducted on March 22, 2018.

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39391|protein.P39391]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0014239,ECOCYC:G7938,GeneID:945056`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4572414-4573931:+; feature_type=gene
