---
entity_id: "gene.b2481"
entity_type: "gene"
name: "hyfA"
source_database: "NCBI RefSeq"
source_id: "gene-b2481"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2481"
  - "hyfA"
---

# hyfA

`gene.b2481`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2481`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hyfA (gene.b2481) is a gene entity. It encodes hyfA (protein.P23481). Encoded protein function: FUNCTION: Probable electron transfer protein for hydrogenase 4. {ECO:0000305|PubMed:9387241}. EcoCyc product frame: MONOMER0-152. EcoCyc synonyms: yffE. Genomic coordinates: 2601201-2601818. EcoCyc protein note: hyfABCDEFGHI encodes a potential nine subunit [Ni-Fe]hydrogenase complex (hydrogenase 4). HyfA resembles the HycB subunit of hydrogenase 3 (50% sequence identity); the protein is predicted to contain four [4Fe-4S] clusters and may function as an electron transferring subunit . HyfA may contain some β-structure elements

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23481|protein.P23481]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008179,ECOCYC:EG11150,GeneID:946959`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2601201-2601818:+; feature_type=gene
