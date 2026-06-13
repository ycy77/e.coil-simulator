---
entity_id: "gene.b0130"
entity_type: "gene"
name: "yadE"
source_database: "NCBI RefSeq"
source_id: "gene-b0130"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0130"
  - "yadE"
---

# yadE

`gene.b0130`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0130`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yadE (gene.b0130) is a gene entity. It encodes yadE (protein.P31666). Encoded protein function: Putative polysaccharide deacetylase YadE (EC 3.-.-.-) EcoCyc product frame: EG11749-MONOMER. Genomic coordinates: 145081-146310. EcoCyc protein note: Sequence similarity suggests that YadE may contain β-barrel structure(s) . An insertion mutation in yadE does not affect the ability to grow on glucose minimal medium .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31666|protein.P31666]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000457,ECOCYC:EG11749,GeneID:946536`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:145081-146310:+; feature_type=gene
