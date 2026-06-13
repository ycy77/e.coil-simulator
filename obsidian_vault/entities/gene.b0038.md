---
entity_id: "gene.b0038"
entity_type: "gene"
name: "caiB"
source_database: "NCBI RefSeq"
source_id: "gene-b0038"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0038"
  - "caiB"
---

# caiB

`gene.b0038`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0038`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

caiB (gene.b0038) is a gene entity. It encodes caiB (protein.P31572). Encoded protein function: FUNCTION: Catalyzes the reversible transfer of the CoA moiety from gamma-butyrobetainyl-CoA to L-carnitine to generate L-carnitinyl-CoA and gamma-butyrobetaine. Is also able to catalyze the reversible transfer of the CoA moiety from gamma-butyrobetainyl-CoA or L-carnitinyl-CoA to crotonobetaine to generate crotonobetainyl-CoA. {ECO:0000255|HAMAP-Rule:MF_01050, ECO:0000269|PubMed:11551212}. EcoCyc product frame: CARNDEHYDRA-MONOMER. EcoCyc synonyms: yaaN. Genomic coordinates: 37898-39115.

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), caiF (protein.P0AE58).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31572|protein.P31572]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=caiB; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=caiB; function=+
- `activates` <-- [[protein.P0AE58|protein.P0AE58]] `RegulonDB` `S` - regulator=CaiF; target=caiB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000136,ECOCYC:EG11559,GeneID:948997`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:37898-39115:-; feature_type=gene
