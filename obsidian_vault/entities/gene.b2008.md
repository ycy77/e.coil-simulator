---
entity_id: "gene.b2008"
entity_type: "gene"
name: "yeeA"
source_database: "NCBI RefSeq"
source_id: "gene-b2008"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2008"
  - "yeeA"
---

# yeeA

`gene.b2008`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2008`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yeeA (gene.b2008) is a gene entity. It encodes yeeA (protein.P33011). Encoded protein function: Inner membrane protein YeeA EcoCyc product frame: EG11891-MONOMER. Genomic coordinates: 2079533-2080591. EcoCyc protein note: YeeA is predicted to be an inner membrane protein with six transmembrane domains; topology analysis suggests the C-terminus is located in the cytoplasm . In the Transporter Classification Database, YeeA has been renamed FusC (fusaric acid resistance protein) and is a member of the aromatic acid exporter (AaAE) family .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33011|protein.P33011]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006667,ECOCYC:EG11891,GeneID:946545`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2079533-2080591:-; feature_type=gene
