---
entity_id: "gene.b2036"
entity_type: "gene"
name: "glf"
source_database: "NCBI RefSeq"
source_id: "gene-b2036"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2036"
  - "glf"
---

# glf

`gene.b2036`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2036`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glf (gene.b2036) is a gene entity. It encodes glf (protein.P37747). Encoded protein function: FUNCTION: Catalyzes the interconversion through a 2-keto intermediate of uridine diphosphogalactopyranose (UDP-GalP) into uridine diphosphogalactofuranose (UDP-GalF). {ECO:0000250, ECO:0000269|PubMed:11448178, ECO:0000269|PubMed:8576037}. EcoCyc product frame: GALPMUT-MONOMER. EcoCyc synonyms: yefE. Genomic coordinates: 2107226-2108329.

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37747|protein.P37747]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006755,ECOCYC:EG11981,GeneID:945235`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2107226-2108329:-; feature_type=gene
