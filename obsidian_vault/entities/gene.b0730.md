---
entity_id: "gene.b0730"
entity_type: "gene"
name: "mngR"
source_database: "NCBI RefSeq"
source_id: "gene-b0730"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0730"
  - "mngR"
---

# mngR

`gene.b0730`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0730`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mngR (gene.b0730) is a gene entity. It encodes mngR (protein.P13669). Encoded protein function: FUNCTION: Represses mngA and mngB. Regulates its own expression. {ECO:0000269|PubMed:14645248, ECO:0000269|PubMed:7805834}. EcoCyc product frame: PD01103. EcoCyc synonyms: ybgB, farR. Genomic coordinates: 765153-765875.

## Biological Role

Repressed by mngR (protein.P13669).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P13669|protein.P13669]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P13669|protein.P13669]] `RegulonDB` `S` - regulator=MngR; target=mngR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002487,ECOCYC:EG11109,GeneID:945371`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:765153-765875:-; feature_type=gene
