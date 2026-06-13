---
entity_id: "gene.b0846"
entity_type: "gene"
name: "rcdA"
source_database: "NCBI RefSeq"
source_id: "gene-b0846"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0846"
  - "rcdA"
---

# rcdA

`gene.b0846`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0846`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rcdA (gene.b0846) is a gene entity. It encodes rcdA (protein.P75811). Encoded protein function: FUNCTION: Regulates the expression of a number of genes involved in biofilm formation and stress response. Target genes include six stress-response transcriptional regulators: csgD, which is a master regulator of biofilm formation, appY, sxy, ycgF, fimB and rcdA itself. This indicates that a large number of genes must be regulated indirectly via these transcriptional regulators. Acts by binding to the upstream region of its target genes. {ECO:0000269|PubMed:23233451}. EcoCyc product frame: G6444-MONOMER. EcoCyc synonyms: ybjK. Genomic coordinates: 887423-887959.

## Biological Role

Activated by rcdA (protein.P75811).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75811|protein.P75811]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P75811|protein.P75811]] `RegulonDB` `C` - regulator=RcdA; target=rcdA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002885,ECOCYC:G6444,GeneID:945473`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:887423-887959:+; feature_type=gene
