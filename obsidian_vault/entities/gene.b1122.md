---
entity_id: "gene.b1122"
entity_type: "gene"
name: "ymfA"
source_database: "NCBI RefSeq"
source_id: "gene-b1122"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1122"
  - "ymfA"
---

# ymfA

`gene.b1122`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1122`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ymfA (gene.b1122) is a gene entity. It encodes ymfA (protein.P75962). Encoded protein function: Inner membrane protein YmfA EcoCyc product frame: G6579-MONOMER. Genomic coordinates: 1181264-1181725. EcoCyc protein note: YmfA is an inner membrane protein with two predicted transmembrane domains. The C terminus is located in the cytoplasm . A ymfA mutation causes a defect in swarming, but not swimming motility .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75962|protein.P75962]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003786,ECOCYC:G6579,GeneID:945684`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1181264-1181725:-; feature_type=gene
