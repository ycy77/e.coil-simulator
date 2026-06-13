---
entity_id: "gene.b0992"
entity_type: "gene"
name: "yccM"
source_database: "NCBI RefSeq"
source_id: "gene-b0992"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0992"
  - "yccM"
---

# yccM

`gene.b0992`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0992`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yccM (gene.b0992) is a gene entity. It encodes yccM (protein.P52636). Encoded protein function: Putative electron transport protein YccM EcoCyc product frame: G6513-MONOMER. Genomic coordinates: 1052289-1053362. EcoCyc protein note: YccM is predicted to be an inner membrane protein with five predicted transmembrane domains; experimental topology analysis suggests the C terminus is located in the periplasm .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52636|protein.P52636]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yccM; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003351,ECOCYC:G6513,GeneID:946295`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1052289-1053362:-; feature_type=gene
