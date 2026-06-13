---
entity_id: "gene.b3074"
entity_type: "gene"
name: "ygjH"
source_database: "NCBI RefSeq"
source_id: "gene-b3074"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3074"
  - "ygjH"
---

# ygjH

`gene.b3074`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3074`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygjH (gene.b3074) is a gene entity. It encodes ygjH (protein.P42589). Encoded protein function: tRNA-binding protein YgjH EcoCyc product frame: G7597-MONOMER. Genomic coordinates: 3220915-3221247.

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P42589|protein.P42589]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ygjH; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010094,ECOCYC:G7597,GeneID:946251`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3220915-3221247:-; feature_type=gene
