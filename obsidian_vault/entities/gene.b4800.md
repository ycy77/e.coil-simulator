---
entity_id: "gene.b4800"
entity_type: "gene"
name: "ytgA"
source_database: "NCBI RefSeq"
source_id: "gene-b4800"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4800"
  - "ytgA"
---

# ytgA

`gene.b4800`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4800`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ytgA (gene.b4800) is a gene entity. It encodes ytgA (protein.P0DSH8). Encoded protein function: Protein YtgA EcoCyc product frame: MONOMER0-4514. Genomic coordinates: 4486105-4486155. EcoCyc protein note: YtgA was identified as a previously unannotated small protein; it is expressed in both exponential and stationary phase in rich media .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DSH8|protein.P0DSH8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ECOCYC:G0-17046,GeneID:63925665`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4486105-4486155:+; feature_type=gene
