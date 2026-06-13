---
entity_id: "gene.b2483"
entity_type: "gene"
name: "hyfC"
source_database: "NCBI RefSeq"
source_id: "gene-b2483"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2483"
  - "hyfC"
---

# hyfC

`gene.b2483`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2483`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hyfC (gene.b2483) is a gene entity. It encodes hyfC (protein.P77858). Encoded protein function: FUNCTION: Possible component of hydrogenase 4. {ECO:0000305|PubMed:9387241}. EcoCyc product frame: MONOMER0-154. Genomic coordinates: 2603847-2604794. EcoCyc protein note: hyfABCDEFGHI encodes a potential nine subunit [Ni-Fe]hydrogenase complex (hydrogenase 4). HyfC is predicted to be an integral membrane protein with 8 transmembrane domains; the protein has sequence similarity to the HycD subunit of hydrogenase 3

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77858|protein.P77858]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008183,ECOCYC:G7300,GeneID:947492`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2603847-2604794:+; feature_type=gene
