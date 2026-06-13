---
entity_id: "gene.b3029"
entity_type: "gene"
name: "ygiN"
source_database: "NCBI RefSeq"
source_id: "gene-b3029"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3029"
  - "ygiN"
---

# ygiN

`gene.b3029`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3029`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygiN (gene.b3029) is a gene entity. It encodes ygiN (protein.P0ADU2). Encoded protein function: FUNCTION: Can oxidize menadiol to menadione (PubMed:15613473). May work in concert with MdaB to form a quinone redox cycle (PubMed:15613473). {ECO:0000269|PubMed:15613473}. EcoCyc product frame: EG12657-MONOMER. Genomic coordinates: 3173142-3173456.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADU2|protein.P0ADU2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ygiN; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009948,ECOCYC:EG12657,GeneID:947506`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3173142-3173456:+; feature_type=gene
