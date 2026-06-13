---
entity_id: "gene.b2488"
entity_type: "gene"
name: "hyfH"
source_database: "NCBI RefSeq"
source_id: "gene-b2488"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2488"
  - "hyfH"
---

# hyfH

`gene.b2488`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2488`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hyfH (gene.b2488) is a gene entity. It encodes hyfH (protein.P77423). Encoded protein function: FUNCTION: Probable electron transfer protein for hydrogenase 4. {ECO:0000305|PubMed:9387241}. EcoCyc product frame: MONOMER0-144. Genomic coordinates: 2610164-2610709. EcoCyc protein note: hyfABCDEFGHI encodes a potential nine subunit [Ni-Fe]hydrogenase complex (hydrogenase 4). HyfH resembles the HycF subunit of hydrogenase 3 (44% sequence identity); the protein is predicted to contain three Fe-S redox sites (two [4Fe-4S] clusters and one mononuclear site) (see also ).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77423|protein.P77423]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008196,ECOCYC:G7305,GeneID:946965`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2610164-2610709:+; feature_type=gene
