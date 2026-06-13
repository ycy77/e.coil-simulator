---
entity_id: "gene.b1408"
entity_type: "gene"
name: "ynbA"
source_database: "NCBI RefSeq"
source_id: "gene-b1408"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1408"
  - "ynbA"
---

# ynbA

`gene.b1408`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1408`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ynbA (gene.b1408) is a gene entity. It encodes ynbA (protein.P76090). Encoded protein function: Inner membrane protein YnbA EcoCyc product frame: G6727-MONOMER. Genomic coordinates: 1477621-1478226. EcoCyc protein note: YnbA is an inner membrane protein with five predicted transmembrane domains. The C terminus is located in the cytoplasm . Based on sequence similarity, YnbA was predicted to be a diacylglycerol cholinephosphotransferase ; however, phosphatidylcholine is not a component of E. coli membranes . ynbA was identified in a screen for genes affecting Fe-S cluster biogenesis and/or iron homeostasis . Expression of ynbA is activated by BglJ-RcsB .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76090|protein.P76090]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004704,ECOCYC:G6727,GeneID:945973`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1477621-1478226:+; feature_type=gene
