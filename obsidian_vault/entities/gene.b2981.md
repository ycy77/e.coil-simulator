---
entity_id: "gene.b2981"
entity_type: "gene"
name: "yghO"
source_database: "NCBI RefSeq"
source_id: "gene-b2981"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2981"
  - "yghO"
---

# yghO

`gene.b2981`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2981`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yghO (gene.b2981) is a gene entity. It encodes yghO (protein.Q46840). Encoded protein function: Protein YghO EcoCyc product frame: G7547-MONOMER. Genomic coordinates: 3129043-3130215. EcoCyc protein note: Transcription of yghO is induced upon biofilm formation compared to planktonic growth in exponential phase. Induction of expression was found to be dependent on the presence of the F plasmid . A yghO mutant is impaired in biofilm formation . YghO was transcriptionally upregulated in iron excess over iron limitation at 21% and 63% of dissolved oxygen as determined by RNA-seq .

## Enriched Pathways

- `eco00600` Sphingolipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco00600` Sphingolipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46840|protein.Q46840]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009779,ECOCYC:G7547,GeneID:947701`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3129043-3130215:-; feature_type=gene
