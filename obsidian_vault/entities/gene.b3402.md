---
entity_id: "gene.b3402"
entity_type: "gene"
name: "yhgE"
source_database: "NCBI RefSeq"
source_id: "gene-b3402"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3402"
  - "yhgE"
---

# yhgE

`gene.b3402`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3402`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhgE (gene.b3402) is a gene entity. It encodes yhgE (protein.P45804). Encoded protein function: Uncharacterized protein YhgE EcoCyc product frame: G7745-MONOMER. Genomic coordinates: 3530715-3532439. EcoCyc protein note: YhgE is the sole member of the Putative Transporter (YhgE) Family

## Biological Role

Activated by arcA (protein.P0A9Q1).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45804|protein.P45804]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=yhgE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011098,ECOCYC:G7745,GeneID:947651`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3530715-3532439:-; feature_type=gene
