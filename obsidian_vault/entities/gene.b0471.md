---
entity_id: "gene.b0471"
entity_type: "gene"
name: "ybaB"
source_database: "NCBI RefSeq"
source_id: "gene-b0471"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0471"
  - "ybaB"
---

# ybaB

`gene.b0471`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0471`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybaB (gene.b0471) is a gene entity. It encodes ybaB (protein.P0A8B5). Encoded protein function: FUNCTION: Binds to DNA and alters its conformation. May be involved in regulation of gene expression, nucleoid organization and DNA protection. {ECO:0000255|HAMAP-Rule:MF_00274}. EcoCyc product frame: EG11100-MONOMER. Genomic coordinates: 494076-494405.

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8B5|protein.P0A8B5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=ybaB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001636,ECOCYC:EG11100,GeneID:945104`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:494076-494405:+; feature_type=gene
