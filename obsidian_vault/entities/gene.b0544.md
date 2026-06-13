---
entity_id: "gene.b0544"
entity_type: "gene"
name: "ybcK"
source_database: "NCBI RefSeq"
source_id: "gene-b0544"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0544"
  - "ybcK"
---

# ybcK

`gene.b0544`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0544`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybcK (gene.b0544) is a gene entity. It encodes ybcK (protein.P77698). Encoded protein function: Uncharacterized protein YbcK EcoCyc product frame: G6300-MONOMER. Genomic coordinates: 568902-570428. EcoCyc protein note: No information about this protein was found by a literature search conducted on February 12, 2020.

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77698|protein.P77698]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ybcK; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001866,ECOCYC:G6300,GeneID:945166`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:568902-570428:+; feature_type=gene
