---
entity_id: "gene.b2625"
entity_type: "gene"
name: "yfjI"
source_database: "NCBI RefSeq"
source_id: "gene-b2625"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2625"
  - "yfjI"
---

# yfjI

`gene.b2625`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2625`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfjI (gene.b2625) is a gene entity. It encodes yfjI (protein.P52124). Encoded protein function: Protein YfjI EcoCyc product frame: G7360-MONOMER. Genomic coordinates: 2758985-2760394. EcoCyc protein note: No information about this protein was found by a literature search conducted on September 2, 2020.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52124|protein.P52124]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yfjI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008643,ECOCYC:G7360,GeneID:944764`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2758985-2760394:+; feature_type=gene
