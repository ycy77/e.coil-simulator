---
entity_id: "gene.b4522"
entity_type: "gene"
name: "ymiA"
source_database: "NCBI RefSeq"
source_id: "gene-b4522"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4522"
  - "ymiA"
---

# ymiA

`gene.b4522`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4522`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ymiA (gene.b4522) is a gene entity. It encodes ymiA (protein.P0CB62). Encoded protein function: Protein YmiA EcoCyc product frame: MONOMER0-2885. EcoCyc synonyms: yciX_1. Genomic coordinates: 1335148-1335288. EcoCyc protein note: The YmiA open reading frame contains a predicted transmembrane segment. YmiA is expressed during both exponential and stationary phase .

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0CB62|protein.P0CB62]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ymiA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0285043,ECOCYC:G0-10512,GeneID:1450256`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1335148-1335288:+; feature_type=gene
