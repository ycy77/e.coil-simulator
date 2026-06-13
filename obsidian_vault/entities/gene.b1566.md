---
entity_id: "gene.b1566"
entity_type: "gene"
name: "flxA"
source_database: "NCBI RefSeq"
source_id: "gene-b1566"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1566"
  - "flxA"
---

# flxA

`gene.b1566`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1566`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

flxA (gene.b1566) is a gene entity. It encodes flxA (protein.P77609). Encoded protein function: Protein FlxA EcoCyc product frame: G6833-MONOMER. Genomic coordinates: 1646405-1646737. EcoCyc protein note: An flxA mutant does not exhibit a defect in flagellar motility . Transcription of flxA is regulated by the flagellar sigma factor, FliA . FlxA: "FliA-dependent expression"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77609|protein.P77609]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005234,ECOCYC:G6833,GeneID:947392`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1646405-1646737:+; feature_type=gene
