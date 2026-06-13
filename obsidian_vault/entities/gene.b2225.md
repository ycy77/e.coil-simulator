---
entity_id: "gene.b2225"
entity_type: "gene"
name: "yfaP"
source_database: "NCBI RefSeq"
source_id: "gene-b2225"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2225"
  - "yfaP"
---

# yfaP

`gene.b2225`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2225`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfaP (gene.b2225) is a gene entity. It encodes yfaP (protein.P76462). Encoded protein function: Uncharacterized protein YfaP EcoCyc product frame: G7152-MONOMER. Genomic coordinates: 2327367-2328143. EcoCyc protein note: Sequence similarity suggests that YfaP may contain β-barrel structure(s) .

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76462|protein.P76462]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007357,ECOCYC:G7152,GeneID:946728`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2327367-2328143:-; feature_type=gene
