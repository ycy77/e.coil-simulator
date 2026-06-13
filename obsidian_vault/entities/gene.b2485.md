---
entity_id: "gene.b2485"
entity_type: "gene"
name: "hyfE"
source_database: "NCBI RefSeq"
source_id: "gene-b2485"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2485"
  - "hyfE"
---

# hyfE

`gene.b2485`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2485`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hyfE (gene.b2485) is a gene entity. It encodes hyfE (protein.P0AEW1). Encoded protein function: FUNCTION: Possible component of hydrogenase 4. {ECO:0000305|PubMed:9387241}. EcoCyc product frame: MONOMER0-142. Genomic coordinates: 2606262-2606912. EcoCyc protein note: hyfABCDEFGHI encodes a potential nine subunit [Ni-Fe]hydrogenase complex (hydrogenase 4). HyfE is predicted to be an integral membrane protein with 7 transmembrane domains

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEW1|protein.P0AEW1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008188,ECOCYC:G7302,GeneID:945298`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2606262-2606912:+; feature_type=gene
