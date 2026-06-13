---
entity_id: "gene.b1460"
entity_type: "gene"
name: "ydcC"
source_database: "NCBI RefSeq"
source_id: "gene-b1460"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1460"
  - "ydcC"
---

# ydcC

`gene.b1460`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1460`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydcC (gene.b1460) is a gene entity. It encodes ydcC (protein.P28917). Encoded protein function: H repeat-associated putative transposase YdcC (ORF-H) EcoCyc product frame: EG11526-MONOMER. Genomic coordinates: 1531816-1532952. EcoCyc protein note: No information about this protein was found by a literature search conducted on May 7, 2018.

## Biological Role

Repressed by hns (protein.P0ACF8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P28917|protein.P28917]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004872,ECOCYC:EG11526,GeneID:947435`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1531816-1532952:+; feature_type=gene
