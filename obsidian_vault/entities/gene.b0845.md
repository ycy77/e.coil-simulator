---
entity_id: "gene.b0845"
entity_type: "gene"
name: "ybjJ"
source_database: "NCBI RefSeq"
source_id: "gene-b0845"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0845"
  - "ybjJ"
---

# ybjJ

`gene.b0845`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0845`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybjJ (gene.b0845) is a gene entity. It encodes ybjJ (protein.P75810). Encoded protein function: Inner membrane protein YbjJ EcoCyc product frame: G6443-MONOMER. Genomic coordinates: 886131-887339. EcoCyc protein note: YbjJ is predicted to be an inner membrane protein with 12 transmembrane domains; experimental topology analysis suggest the C-terminus is located in the cytoplasm . In the Transporter Classification Database, YbjJ is an uncharacterized member of the Major Facilitator Superfamily (MFS) of transport proteins .

## Biological Role

Repressed by rcdA (protein.P75811).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75810|protein.P75810]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P75811|protein.P75811]] `RegulonDB` `C` - regulator=RcdA; target=ybjJ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002880,ECOCYC:G6443,GeneID:945471`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:886131-887339:-; feature_type=gene
