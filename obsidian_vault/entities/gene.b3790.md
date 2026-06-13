---
entity_id: "gene.b3790"
entity_type: "gene"
name: "rffC"
source_database: "NCBI RefSeq"
source_id: "gene-b3790"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3790"
  - "rffC"
---

# rffC

`gene.b3790`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3790`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rffC (gene.b3790) is a gene entity. It encodes wecD (protein.P27832). Encoded protein function: FUNCTION: Catalyzes the acetylation of dTDP-fucosamine (dTDP-4-amino-4,6-dideoxy-D-galactose) to dTDP-Fuc4NAc, which is utilized in the biosynthesis of the enterobacterial common antigen (ECA). {ECO:0000255|HAMAP-Rule:MF_02027}. EcoCyc product frame: TDPFUCACTRANS-MONOMER. EcoCyc synonyms: rff, wecD, yifH. Genomic coordinates: 3974467-3975141.

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27832|protein.P27832]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012382,ECOCYC:EG11455,GeneID:948298`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3974467-3975141:+; feature_type=gene
