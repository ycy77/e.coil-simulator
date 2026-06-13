---
entity_id: "gene.b4542"
entity_type: "gene"
name: "yohO"
source_database: "NCBI RefSeq"
source_id: "gene-b4542"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4542"
  - "yohO"
---

# yohO

`gene.b4542`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4542`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yohO (gene.b4542) is a gene entity. It encodes yohO (protein.Q2EES6). Encoded protein function: UPF0387 membrane protein YohO EcoCyc product frame: MONOMER0-2681. Genomic coordinates: 2215657-2215764. EcoCyc protein note: The YohO open reading frame contains a predicted transmembrane segment; the protein is expressed during both exponential and stationary phase .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q2EES6|protein.Q2EES6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yohO; function=-

## External IDs

- `Dbxref:ASAP:ABE-0285063,ECOCYC:G0-10459,GeneID:1450279`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2215657-2215764:+; feature_type=gene
