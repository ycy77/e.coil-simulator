---
entity_id: "gene.b2805"
entity_type: "gene"
name: "fucR"
source_database: "NCBI RefSeq"
source_id: "gene-b2805"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2805"
  - "fucR"
---

# fucR

`gene.b2805`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2805`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fucR (gene.b2805) is a gene entity. It encodes fucR (protein.P0ACK8). Encoded protein function: FUNCTION: Transcriptional activator of the fuc operon. EcoCyc product frame: PD00444. Genomic coordinates: 2939368-2940099.

## Biological Role

Activated by crp (protein.P0ACJ8), ygfI (protein.P52044).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACK8|protein.P0ACK8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=fucR; function=+
- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `C` - regulator=SrsR; target=fucR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009195,ECOCYC:EG10353,GeneID:946905`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2939368-2940099:+; feature_type=gene
