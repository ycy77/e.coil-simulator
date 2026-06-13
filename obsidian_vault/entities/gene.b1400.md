---
entity_id: "gene.b1400"
entity_type: "gene"
name: "paaY"
source_database: "NCBI RefSeq"
source_id: "gene-b1400"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1400"
  - "paaY"
---

# paaY

`gene.b1400`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1400`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

paaY (gene.b1400) is a gene entity. It encodes paaY (protein.P77181). Encoded protein function: Phenylacetic acid degradation protein PaaY EcoCyc product frame: G6721-MONOMER. EcoCyc synonyms: ydbZ. Genomic coordinates: 1464471-1465061.

## Biological Role

Repressed by paaX (protein.P76086). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77181|protein.P77181]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=paaY; function=+
- `represses` <-- [[protein.P76086|protein.P76086]] `RegulonDB` `S` - regulator=PaaX; target=paaY; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004676,ECOCYC:G6721,GeneID:945965`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1464471-1465061:+; feature_type=gene
