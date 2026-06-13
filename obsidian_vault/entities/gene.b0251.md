---
entity_id: "gene.b0251"
entity_type: "gene"
name: "yafY"
source_database: "NCBI RefSeq"
source_id: "gene-b0251"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0251"
  - "yafY"
---

# yafY

`gene.b0251`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0251`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yafY (gene.b0251) is a gene entity. It encodes yafY (protein.P77365). Encoded protein function: FUNCTION: When overproduced strongly induces degP through the activation of the two-component envelope stress response system CpxA/CpxR (PubMed:15252048). {ECO:0000269|PubMed:15252048}. EcoCyc product frame: G6126-MONOMER. Genomic coordinates: 266110-266553. EcoCyc protein note: YafY is an inner membrane lipoprotein; overexpression of YafY strongly induces expression of degP, which encodes a periplasmic protease; the effect is dependent on the Cpx two-component system .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77365|protein.P77365]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000853,ECOCYC:G6126,GeneID:944934`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:266110-266553:-; feature_type=gene
