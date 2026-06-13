---
entity_id: "gene.b2365"
entity_type: "gene"
name: "dsdX"
source_database: "NCBI RefSeq"
source_id: "gene-b2365"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2365"
  - "dsdX"
---

# dsdX

`gene.b2365`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2365`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dsdX (gene.b2365) is a gene entity. It encodes dsdX (protein.P08555). Encoded protein function: FUNCTION: A D-serine-specific transporter, may function as a H(+) symporter. {ECO:0000250|UniProtKB:A0A0H2VAP9}. EcoCyc product frame: DSDX-MONOMER. EcoCyc synonyms: yfdD, yfdA, dsdC. Genomic coordinates: 2477847-2479184. EcoCyc protein note: DsdX from E. coli clinical isolate CFT073 has been characterised as a D-serine permease . E. coli CFT073 dsdX has 98% identity with dsdX from E. coli K-12. dsdX is located in a serine-inducible operon with EG10249 "dsdA" encoding D-serine deaminase .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08555|protein.P08555]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007801,ECOCYC:EG10250,GeneID:949103`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2477847-2479184:+; feature_type=gene
