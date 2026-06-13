---
entity_id: "gene.b3780"
entity_type: "gene"
name: "rhlB"
source_database: "NCBI RefSeq"
source_id: "gene-b3780"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3780"
  - "rhlB"
---

# rhlB

`gene.b3780`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3780`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rhlB (gene.b3780) is a gene entity. It encodes rhlB (protein.P0A8J8). Encoded protein function: FUNCTION: DEAD-box RNA helicase involved in RNA degradation. Has RNA-dependent ATPase activity and unwinds double-stranded RNA. {ECO:0000255|HAMAP-Rule:MF_00661, ECO:0000269|PubMed:12181321, ECO:0000269|PubMed:8610017, ECO:0000269|PubMed:9732274}. EcoCyc product frame: EG10844-MONOMER. EcoCyc synonyms: mmrA. Genomic coordinates: 3964365-3965630.

## Enriched Pathways

- `eco03018` RNA degradation (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8J8|protein.P0A8J8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012351,ECOCYC:EG10844,GeneID:948290`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3964365-3965630:-; feature_type=gene
