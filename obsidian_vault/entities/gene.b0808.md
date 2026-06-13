---
entity_id: "gene.b0808"
entity_type: "gene"
name: "ybiO"
source_database: "NCBI RefSeq"
source_id: "gene-b0808"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0808"
  - "ybiO"
---

# ybiO

`gene.b0808`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0808`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybiO (gene.b0808) is a gene entity. It encodes ybiO (protein.P75783). Encoded protein function: FUNCTION: Mechanosensitive channel that protects cells against hypoosmotic stress when highly overexpressed. {ECO:0000269|PubMed:22874652}. EcoCyc product frame: G6417-MONOMER. Genomic coordinates: 843255-845480.

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75783|protein.P75783]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002760,ECOCYC:G6417,GeneID:945935`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:843255-845480:-; feature_type=gene
