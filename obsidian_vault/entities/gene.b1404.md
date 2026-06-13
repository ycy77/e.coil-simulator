---
entity_id: "gene.b1404"
entity_type: "gene"
name: "insI2"
source_database: "NCBI RefSeq"
source_id: "gene-b1404"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1404"
  - "insI2"
---

# insI2

`gene.b1404`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1404`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

insI2 (gene.b1404) is a gene entity. It encodes insI3 (protein.P0CF89). Encoded protein function: FUNCTION: Required for the transposition of the insertion element. {ECO:0000305}. EcoCyc product frame: G6725-MONOMER. EcoCyc synonyms: tra8-2. Genomic coordinates: 1469358-1470509. EcoCyc protein note: This is the transposase for the insertion sequence IS30. The IS30 transposase interacts with the terminal inverted repeats of the IS30 sequence element, using them as targets for transposition . The carboxy-terminus of the transposase is required for formation and dissolution of the dimeric transpositional intermediate .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0CF89|protein.P0CF89]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004691,ECOCYC:G6725,GeneID:945968`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1469358-1470509:+; feature_type=gene
