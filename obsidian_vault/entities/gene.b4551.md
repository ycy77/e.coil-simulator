---
entity_id: "gene.b4551"
entity_type: "gene"
name: "yheV"
source_database: "NCBI RefSeq"
source_id: "gene-b4551"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4551"
  - "yheV"
---

# yheV

`gene.b4551`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4551`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yheV (gene.b4551) is a gene entity. It encodes yheV (protein.P0ADW8). Encoded protein function: Uncharacterized protein YheV EcoCyc product frame: MONOMER0-2688. Genomic coordinates: 3478592-3478792. EcoCyc protein note: YheV was found in a genome-wide CRISPRi screen for genes that enable decoupling of growth and GFP accumulation. Depletion of YheV by CRISPRi leads to elevated density of heterologously expressed GFP in the cells while not affecting growth .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADW8|protein.P0ADW8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0285072,ECOCYC:G0-10466,GeneID:1450290`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3478592-3478792:-; feature_type=gene
