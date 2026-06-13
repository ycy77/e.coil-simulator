---
entity_id: "gene.b2053"
entity_type: "gene"
name: "gmd"
source_database: "NCBI RefSeq"
source_id: "gene-b2053"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2053"
  - "gmd"
---

# gmd

`gene.b2053`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2053`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gmd (gene.b2053) is a gene entity. It encodes gmd (protein.P0AC88). Encoded protein function: FUNCTION: Catalyzes the conversion of GDP-D-mannose to GDP-4-dehydro-6-deoxy-D-mannose. {ECO:0000255|HAMAP-Rule:MF_00955, ECO:0000269|PubMed:9257704}. EcoCyc product frame: GDPMANDEHYDRA-MONOMER. EcoCyc synonyms: yefN, yefA. Genomic coordinates: 2127193-2128314.

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC88|protein.P0AC88]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006803,ECOCYC:EG11787,GeneID:946562`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2127193-2128314:-; feature_type=gene
