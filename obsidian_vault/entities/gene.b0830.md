---
entity_id: "gene.b0830"
entity_type: "gene"
name: "gsiB"
source_database: "NCBI RefSeq"
source_id: "gene-b0830"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0830"
  - "gsiB"
---

# gsiB

`gene.b0830`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0830`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gsiB (gene.b0830) is a gene entity. It encodes gsiB (protein.P75797). Encoded protein function: FUNCTION: Part of the ABC transporter complex GsiABCD involved in glutathione import (PubMed:16109926). Binds glutathione (PubMed:30515393). {ECO:0000269|PubMed:16109926, ECO:0000269|PubMed:30515393}. EcoCyc product frame: YLIB-MONOMER. EcoCyc synonyms: yliB. Genomic coordinates: 869411-870949. EcoCyc protein note: gsiB encodes the periplasmic binding protein of a glutathione ABC importer . GsiB has been used to develop a biosensor specific for the detection of reduced glutathione

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75797|protein.P75797]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002832,ECOCYC:G6430,GeneID:945459`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:869411-870949:+; feature_type=gene
