---
entity_id: "gene.b2052"
entity_type: "gene"
name: "fcl"
source_database: "NCBI RefSeq"
source_id: "gene-b2052"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2052"
  - "fcl"
---

# fcl

`gene.b2052`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2052`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fcl (gene.b2052) is a gene entity. It encodes fcl (protein.P32055). Encoded protein function: FUNCTION: Catalyzes the two-step NADP-dependent conversion of GDP-4-dehydro-6-deoxy-D-mannose to GDP-fucose, involving an epimerase and a reductase reaction. {ECO:0000255|HAMAP-Rule:MF_00956, ECO:0000269|PubMed:10480878, ECO:0000269|PubMed:11021971, ECO:0000269|PubMed:9473059}. EcoCyc product frame: FCL-MONOMER. EcoCyc synonyms: wcaG, yefB. Genomic coordinates: 2126225-2127190.

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32055|protein.P32055]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006801,ECOCYC:EG11788,GeneID:946563`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2126225-2127190:-; feature_type=gene
