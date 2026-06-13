---
entity_id: "gene.b0818"
entity_type: "gene"
name: "ybiR"
source_database: "NCBI RefSeq"
source_id: "gene-b0818"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0818"
  - "ybiR"
---

# ybiR

`gene.b0818`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0818`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybiR (gene.b0818) is a gene entity. It encodes ybiR (protein.P75788). Encoded protein function: Inner membrane protein YbiR EcoCyc product frame: G6421-MONOMER. Genomic coordinates: 853647-854765. EcoCyc protein note: In the Transporter Classification Database YbiR is an unharacterized member of the Arsenite-Antimonite (ArsB) Efflux Family within the Ion Transporter (IT) superfamily.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75788|protein.P75788]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002795,ECOCYC:G6421,GeneID:945438`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:853647-854765:+; feature_type=gene
