---
entity_id: "gene.b1339"
entity_type: "gene"
name: "abgR"
source_database: "NCBI RefSeq"
source_id: "gene-b1339"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1339"
  - "abgR"
---

# abgR

`gene.b1339`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1339`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

abgR (gene.b1339) is a gene entity. It encodes abgR (protein.P77744). Encoded protein function: FUNCTION: Could be the regulator of the abg operon. EcoCyc product frame: G6671-MONOMER. Genomic coordinates: 1404741-1405649. EcoCyc protein note: AbgR may transcriptionally regulate expression of the divergently transcribed predicted abg operon . The deletion of abgR severely reduces long-term viability (<1%) .

## Biological Role

Repressed by nac (protein.Q47005). Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77744|protein.P77744]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=abgR; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=abgR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004496,ECOCYC:G6671,GeneID:945831`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1404741-1405649:+; feature_type=gene
