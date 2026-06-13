---
entity_id: "gene.b4116"
entity_type: "gene"
name: "adiY"
source_database: "NCBI RefSeq"
source_id: "gene-b4116"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4116"
  - "adiY"
---

# adiY

`gene.b4116`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4116`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

adiY (gene.b4116) is a gene entity. It encodes adiY (protein.P33234). Encoded protein function: HTH-type transcriptional regulator AdiY EcoCyc product frame: EG11966-MONOMER. Genomic coordinates: 4337168-4337929.

## Biological Role

Repressed by sgrS (gene.b4577), hns (protein.P0ACF8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33234|protein.P33234]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[gene.b4577|gene.b4577]] `RegulonDB` `S` - regulator=SgrS; target=adiY; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=adiY; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013479,ECOCYC:EG11966,GeneID:948627`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4337168-4337929:-; feature_type=gene
