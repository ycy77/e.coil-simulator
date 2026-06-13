---
entity_id: "gene.b0277"
entity_type: "gene"
name: "yagK"
source_database: "NCBI RefSeq"
source_id: "gene-b0277"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0277"
  - "yagK"
---

# yagK

`gene.b0277`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0277`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yagK (gene.b0277) is a gene entity. It encodes yagK (protein.P77657). Encoded protein function: Uncharacterized protein YagK EcoCyc product frame: G6148-MONOMER. Genomic coordinates: 292322-292948. EcoCyc protein note: No information about this protein was found by a literature search conducted on December 20, 2017.

## Biological Role

Repressed by rcdA (protein.P75811).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77657|protein.P77657]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P75811|protein.P75811]] `RegulonDB` `S` - regulator=RcdA; target=yagK; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000965,ECOCYC:G6148,GeneID:945847`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:292322-292948:-; feature_type=gene
