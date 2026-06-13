---
entity_id: "gene.b1332"
entity_type: "gene"
name: "ynaJ"
source_database: "NCBI RefSeq"
source_id: "gene-b1332"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1332"
  - "ynaJ"
---

# ynaJ

`gene.b1332`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1332`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ynaJ (gene.b1332) is a gene entity. It encodes ynaJ (protein.P64445). Encoded protein function: Uncharacterized protein YnaJ EcoCyc product frame: G6668-MONOMER. Genomic coordinates: 1397365-1397622. EcoCyc protein note: No information about this protein was found by a literature search conducted on February 23, 2017.

## Biological Role

Repressed by arcA (protein.P0A9Q1).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64445|protein.P64445]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=ynaJ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004470,ECOCYC:G6668,GeneID:945901`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1397365-1397622:+; feature_type=gene
