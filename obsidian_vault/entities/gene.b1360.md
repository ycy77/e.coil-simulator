---
entity_id: "gene.b1360"
entity_type: "gene"
name: "ydaV"
source_database: "NCBI RefSeq"
source_id: "gene-b1360"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1360"
  - "ydaV"
---

# ydaV

`gene.b1360`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1360`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydaV (gene.b1360) is a gene entity. It encodes ydaV (protein.P77546). Encoded protein function: Uncharacterized protein YdaV EcoCyc product frame: G6684-MONOMER. Genomic coordinates: 1421983-1422729. EcoCyc protein note: ydaV was identified in a screen for genes affecting Fe-S cluster biogenesis and/or iron homeostasis .

## Biological Role

Repressed by racR (protein.P76062).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77546|protein.P77546]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P76062|protein.P76062]] `RegulonDB` `S` - regulator=RacR; target=ydaV; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004560,ECOCYC:G6684,GeneID:945926`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1421983-1422729:+; feature_type=gene
