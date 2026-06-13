---
entity_id: "gene.b2413"
entity_type: "gene"
name: "cysZ"
source_database: "NCBI RefSeq"
source_id: "gene-b2413"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2413"
  - "cysZ"
---

# cysZ

`gene.b2413`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2413`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cysZ (gene.b2413) is a gene entity. It encodes cysZ (protein.P0A6J3). Encoded protein function: FUNCTION: High affinity, high specificity proton-dependent sulfate transporter, which mediates sulfate uptake. Provides the sulfur source for the cysteine synthesis pathway. Does not transport thiosulfate. {ECO:0000269|PubMed:24657232}. EcoCyc product frame: EG10003-MONOMER. Genomic coordinates: 2531463-2532224. EcoCyc protein note: CysZ is a high affinity, high specificity sulfate transporter which mediates sulfate uptake for the purpose of cysteine synthesis . CysZ interacts with sulfate, sulfite, sulfide and cysteine but does not interact with thiosulfate. CysZ mediates sulfate uptake into whole cells and proteoliposomes. CysZ mediated sulfate uptake is inhibited by sulfite. CysZ is a sulfate:proton symporter but the exact stoichiometry of the transport reaction is not known . A cysZ mutant is deficient in sulfate assimilation .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6J3|protein.P0A6J3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007953,ECOCYC:EG10003,GeneID:946875`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2531463-2532224:+; feature_type=gene
