---
entity_id: "gene.b1580"
entity_type: "gene"
name: "rspB"
source_database: "NCBI RefSeq"
source_id: "gene-b1580"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1580"
  - "rspB"
---

# rspB

`gene.b1580`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1580`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rspB (gene.b1580) is a gene entity. It encodes rspB (protein.P38105). Encoded protein function: FUNCTION: Not known; probable catabolic enzyme. EcoCyc product frame: G6838-MONOMER. Genomic coordinates: 1652896-1653915. EcoCyc protein note: rspA and rspB are encoded in an operon . RspB: "regulatory in stationary phase"

## Biological Role

Repressed by rspR (protein.P0ACM2). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P38105|protein.P38105]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=rspB; function=+
- `represses` <-- [[protein.P0ACM2|protein.P0ACM2]] `RegulonDB` `S` - regulator=YdfH; target=rspB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005272,ECOCYC:G6838,GeneID:946127`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1652896-1653915:-; feature_type=gene
