---
entity_id: "gene.b0256"
entity_type: "gene"
name: "insI1"
source_database: "NCBI RefSeq"
source_id: "gene-b0256"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0256"
  - "insI1"
---

# insI1

`gene.b0256`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0256`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

insI1 (gene.b0256) is a gene entity. It encodes insI1 (protein.P0CF88). Encoded protein function: FUNCTION: Required for the transposition of the insertion element. {ECO:0000305}. EcoCyc product frame: G6131-MONOMER. EcoCyc synonyms: tra8-1. Genomic coordinates: 270603-271754. EcoCyc protein note: This is the transposase for the insertion sequence IS30. The IS30 transposase interacts with the terminal inverted repeats of the IS30 sequence element, using them as targets for transposition . The carboxy-terminus of the transposase is required for formation and dissolution of the dimeric transpositional intermediate .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0CF88|protein.P0CF88]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000871,ECOCYC:G6131,GeneID:949005`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:270603-271754:+; feature_type=gene
