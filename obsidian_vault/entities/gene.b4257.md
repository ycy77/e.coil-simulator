---
entity_id: "gene.b4257"
entity_type: "gene"
name: "yjgN"
source_database: "NCBI RefSeq"
source_id: "gene-b4257"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4257"
  - "yjgN"
---

# yjgN

`gene.b4257`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4257`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjgN (gene.b4257) is a gene entity. It encodes yjgN (protein.P39338). Encoded protein function: Inner membrane protein YjgN EcoCyc product frame: G7887-MONOMER. Genomic coordinates: 4479730-4480926. EcoCyc protein note: YjgN is an inner membrane protein with eight predicted transmembrane domains. The C terminus is located in the cytoplasm .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39338|protein.P39338]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yjgN; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013944,ECOCYC:G7887,GeneID:948784`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4479730-4480926:+; feature_type=gene
