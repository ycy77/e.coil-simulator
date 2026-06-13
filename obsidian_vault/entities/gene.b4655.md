---
entity_id: "gene.b4655"
entity_type: "gene"
name: "ythA"
source_database: "NCBI RefSeq"
source_id: "gene-b4655"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4655"
  - "ythA"
---

# ythA

`gene.b4655`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4655`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ythA (gene.b4655) is a gene entity. It encodes ythA (protein.A8DYQ1). Encoded protein function: Uncharacterized protein YthA EcoCyc product frame: MONOMER0-2840. Genomic coordinates: 4506448-4506573. EcoCyc protein note: The YthA open reading frame was predicted based on the presence of a ribosome binding site in an intergenic region. YthA contains a predicted transmembrane segment. YthA is highly expressed during both exponential growth and stationary phase .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.A8DYQ1|protein.A8DYQ1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ECOCYC:G0-10616,GeneID:5625581`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4506448-4506573:+; feature_type=gene
