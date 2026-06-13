---
entity_id: "gene.b2812"
entity_type: "gene"
name: "tcdA"
source_database: "NCBI RefSeq"
source_id: "gene-b2812"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2812"
  - "tcdA"
---

# tcdA

`gene.b2812`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2812`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tcdA (gene.b2812) is a gene entity. It encodes tcdA (protein.Q46927). Encoded protein function: FUNCTION: Catalyzes the ATP-dependent dehydration of threonylcarbamoyladenosine at position 37 (t(6)A37) to form cyclic t(6)A37 (ct(6)A37) in tRNAs that read codons beginning with adenine. TcdA is also part of a sulfur transfer pathway; is able to accept sulfur from CsdA directly in vitro, but CsdE might act as the sulfur donor in vivo. {ECO:0000269|PubMed:20054882, ECO:0000269|PubMed:23242255}. EcoCyc product frame: G7456-MONOMER. EcoCyc synonyms: ygdL, csdL. Genomic coordinates: 2945036-2945842.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46927|protein.Q46927]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009223,ECOCYC:G7456,GeneID:947291`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2945036-2945842:-; feature_type=gene
