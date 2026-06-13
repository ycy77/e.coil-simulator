---
entity_id: "gene.b0965"
entity_type: "gene"
name: "yccU"
source_database: "NCBI RefSeq"
source_id: "gene-b0965"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0965"
  - "yccU"
---

# yccU

`gene.b0965`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0965`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yccU (gene.b0965) is a gene entity. It encodes yccU (protein.P75874). Encoded protein function: Uncharacterized protein YccU EcoCyc product frame: G6499-MONOMER. Genomic coordinates: 1027946-1028359. EcoCyc protein note: The YccU protein is newly produced when cells are grown on oleic acid as the source of carbon . In Salmonella enterica, the Qad (YccU) protein serves as an acetyl donor for acetylation of HspQ .

## Biological Role

Repressed by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75874|protein.P75874]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=yccU; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003267,ECOCYC:G6499,GeneID:949008`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1027946-1028359:+; feature_type=gene
