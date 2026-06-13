---
entity_id: "gene.b3104"
entity_type: "gene"
name: "yhaI"
source_database: "NCBI RefSeq"
source_id: "gene-b3104"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3104"
  - "yhaI"
---

# yhaI

`gene.b3104`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3104`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhaI (gene.b3104) is a gene entity. It encodes yhaI (protein.P64592). Encoded protein function: Inner membrane protein YhaI EcoCyc product frame: G7618-MONOMER. Genomic coordinates: 3252911-3253267. EcoCyc protein note: YhaI is an inner membrane protein with three predicted transmembrane domains. The C terminus is located in the cytoplasm .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64592|protein.P64592]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yhaI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010211,ECOCYC:G7618,GeneID:947612`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3252911-3253267:+; feature_type=gene
