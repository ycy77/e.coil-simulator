---
entity_id: "gene.b1431"
entity_type: "gene"
name: "ydcL"
source_database: "NCBI RefSeq"
source_id: "gene-b1431"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1431"
  - "ydcL"
---

# ydcL

`gene.b1431`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1431`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydcL (gene.b1431) is a gene entity. It encodes ydcL (protein.P64451). Encoded protein function: Uncharacterized lipoprotein YdcL EcoCyc product frame: G6742-MONOMER. Genomic coordinates: 1502457-1503125. EcoCyc protein note: YdcL is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ).

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64451|protein.P64451]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004775,ECOCYC:G6742,GeneID:948203`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1502457-1503125:+; feature_type=gene
