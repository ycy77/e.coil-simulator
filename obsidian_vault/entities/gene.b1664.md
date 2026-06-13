---
entity_id: "gene.b1664"
entity_type: "gene"
name: "ydhQ"
source_database: "NCBI RefSeq"
source_id: "gene-b1664"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1664"
  - "ydhQ"
---

# ydhQ

`gene.b1664`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1664`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydhQ (gene.b1664) is a gene entity. It encodes ydhQ (protein.P77552). Encoded protein function: Protein YdhQ EcoCyc product frame: G6894-MONOMER. Genomic coordinates: 1744871-1746127. EcoCyc protein note: ydhQ is part of a functional interaction network that includes proteins involved in bacterial adhesion and biofilm formation. A ydhQ mutant shows increased biofilm formation .

## Biological Role

Activated by lrp (protein.P0ACJ0), rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77552|protein.P77552]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=ydhQ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005563,ECOCYC:G6894,GeneID:944851`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1744871-1746127:-; feature_type=gene
