---
entity_id: "gene.b0787"
entity_type: "gene"
name: "ybhM"
source_database: "NCBI RefSeq"
source_id: "gene-b0787"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0787"
  - "ybhM"
---

# ybhM

`gene.b0787`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0787`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybhM (gene.b0787) is a gene entity. It encodes ybhM (protein.P75769). Encoded protein function: Uncharacterized protein YbhM EcoCyc product frame: G6404-MONOMER. Genomic coordinates: 820793-821506. EcoCyc protein note: No information about this protein was found by a literature search conducted on May 26, 2021.

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75769|protein.P75769]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ybhM; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002688,ECOCYC:G6404,GeneID:949001`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:820793-821506:+; feature_type=gene
