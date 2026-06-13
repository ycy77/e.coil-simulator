---
entity_id: "gene.b3003"
entity_type: "gene"
name: "yghA"
source_database: "NCBI RefSeq"
source_id: "gene-b3003"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3003"
  - "yghA"
---

# yghA

`gene.b3003`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3003`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yghA (gene.b3003) is a gene entity. It encodes yghA (protein.P0AG84). Encoded protein function: Uncharacterized oxidoreductase YghA (EC 1.-.-.-) EcoCyc product frame: EG11292-MONOMER. Genomic coordinates: 3149662-3150546. EcoCyc protein note: YghA is an NADP+-dependent aldehyde reductase with activity toward butyraldehyde and decanal . A broad survey of aldehyde reductases showed that YghA was one of several endogenous aldehyde reductases that contribute to the degradation of desired aldehyde end products of metabolic engineering .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG84|protein.P0AG84]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009859,ECOCYC:EG11292,GeneID:947478`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3149662-3150546:+; feature_type=gene
