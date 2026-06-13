---
entity_id: "gene.b0917"
entity_type: "gene"
name: "ycaR"
source_database: "NCBI RefSeq"
source_id: "gene-b0917"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0917"
  - "ycaR"
---

# ycaR

`gene.b0917`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0917`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycaR (gene.b0917) is a gene entity. It encodes ycaR (protein.P0AAZ7). Encoded protein function: FUNCTION: May act as a general partner for methyltransferases. {ECO:0000255|HAMAP-Rule:MF_01187}. EcoCyc product frame: G6472-MONOMER. Genomic coordinates: 970673-970855. EcoCyc protein note: No information about this protein was found by a literature search conducted on November 16, 2020.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAZ7|protein.P0AAZ7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ycaR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003120,ECOCYC:G6472,GeneID:945537`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:970673-970855:+; feature_type=gene
