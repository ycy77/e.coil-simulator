---
entity_id: "gene.b1556"
entity_type: "gene"
name: "essQ"
source_database: "NCBI RefSeq"
source_id: "gene-b1556"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1556"
  - "essQ"
---

# essQ

`gene.b1556`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1556`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

essQ (gene.b1556) is a gene entity. It encodes essQ (protein.P77237). Encoded protein function: Prophage lysis protein S homolog EssQ (Lysis protein S homolog from lambdoid prophage Qin) EcoCyc product frame: G6829-MONOMER. EcoCyc synonyms: ydfS. Genomic coordinates: 1640370-1640585. EcoCyc protein note: EssQ is predicted to be a bitopic inner membrane protein .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77237|protein.P77237]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005197,ECOCYC:G6829,GeneID:946093`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1640370-1640585:-; feature_type=gene
