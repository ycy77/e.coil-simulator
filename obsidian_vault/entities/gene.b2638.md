---
entity_id: "gene.b2638"
entity_type: "gene"
name: "yfjU"
source_database: "NCBI RefSeq"
source_id: "gene-b2638"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2638"
  - "yfjU"
---

# yfjU

`gene.b2638`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2638`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfjU (gene.b2638) is a gene entity. It encodes yfjU (protein.P0CF86). Encoded protein function: Putative arsenate reductase-like protein EcoCyc product frame: G7373-MONOMER. Genomic coordinates: 2771840-2772154. EcoCyc protein note: No information about this protein was found by a literature search conducted on January 30, 2020.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R05747|reaction.R05747]] `KEGG` `database` - via EC:1.20.4.1
- `encodes` --> [[protein.P0CF86|protein.P0CF86]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008685,ECOCYC:G7373,GeneID:945062`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2771840-2772154:-; feature_type=gene
