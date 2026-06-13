---
entity_id: "gene.b4812"
entity_type: "gene"
name: "timP"
source_database: "NCBI RefSeq"
source_id: "gene-b4812"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4812"
  - "timP"
---

# timP

`gene.b4812`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4812`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

timP (gene.b4812) is a gene entity. It encodes timP (protein.P0DUM3). Encoded protein function: FUNCTION: Putative toxic component of a potential type I toxin-antitoxin (TA) system. Neutralized by sRNA antitoxin TimR which binds to the 5' UTR of timP mRNA and inhibits translation. The antitoxin gene is encoded immediately upstream and transcribed divergently from the toxin gene; antitoxin RNA is less stable than timP mRNA. {ECO:0000250|UniProtKB:P0DUM2}. EcoCyc product frame: MONOMER0-4540. Genomic coordinates: 2654001-2654126. EcoCyc protein note: In Salmonella Typhimurium SL1344, the homologous protein TimP is a small toxic inner membrane protein within the G0-8879 whose translation is repressed by the small regulatory RNA TimR .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DUM3|protein.P0DUM3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ECOCYC:G0-17087,GeneID:71004570`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2654001-2654126:+; feature_type=gene
