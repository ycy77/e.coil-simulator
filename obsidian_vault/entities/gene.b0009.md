---
entity_id: "gene.b0009"
entity_type: "gene"
name: "mog"
source_database: "NCBI RefSeq"
source_id: "gene-b0009"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0009"
  - "mog"
---

# mog

`gene.b0009`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0009`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mog (gene.b0009) is a gene entity. It encodes mog (protein.P0AF03). Encoded protein function: FUNCTION: Catalyzes the adenylation of molybdopterin as part of the biosynthesis of the molybdenum-cofactor. {ECO:0000269|PubMed:15632135}. EcoCyc product frame: EG11511-MONOMER. EcoCyc synonyms: yaaG, bisD, chlG, mog. Genomic coordinates: 9306-9893.

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF03|protein.P0AF03]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000030,ECOCYC:EG11511,GeneID:944760`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:9306-9893:+; feature_type=gene
