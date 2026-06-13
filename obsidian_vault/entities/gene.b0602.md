---
entity_id: "gene.b0602"
entity_type: "gene"
name: "ybdN"
source_database: "NCBI RefSeq"
source_id: "gene-b0602"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0602"
  - "ybdN"
---

# ybdN

`gene.b0602`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0602`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybdN (gene.b0602) is a gene entity. It encodes ybdN (protein.P77216). Encoded protein function: Uncharacterized protein YbdN EcoCyc product frame: G6331-MONOMER. Genomic coordinates: 635349-636569. EcoCyc protein note: No information about this protein was found by a literature search conducted on February 15, 2017.

## Biological Role

Repressed by ybdO (protein.P77746).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77216|protein.P77216]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P77746|protein.P77746]] `RegulonDB` `S` - regulator=CitR; target=ybdN; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002073,ECOCYC:G6331,GeneID:945205`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:635349-636569:-; feature_type=gene
