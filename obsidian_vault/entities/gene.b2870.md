---
entity_id: "gene.b2870"
entity_type: "gene"
name: "ygeW"
source_database: "NCBI RefSeq"
source_id: "gene-b2870"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2870"
  - "ygeW"
---

# ygeW

`gene.b2870`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2870`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygeW (gene.b2870) is a gene entity. It encodes ygeW (protein.Q46803). Encoded protein function: FUNCTION: Putative carbamoyltransferase. No activity can be detected with allantoin or 25 other related compounds, including 20 naturally occurring amino acids, N-acetyl-L-ornithine, N-succinyl-L-ornithine, L-ornithine, oxamate, beta-alanine and putrescine. {ECO:0000269|PubMed:21557323}. EcoCyc product frame: G7489-MONOMER. Genomic coordinates: 3006262-3007452.

## Biological Role

Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46803|protein.Q46803]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ygeW; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009425,ECOCYC:G7489,GeneID:945826`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3006262-3007452:+; feature_type=gene
