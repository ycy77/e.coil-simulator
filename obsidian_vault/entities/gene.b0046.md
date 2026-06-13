---
entity_id: "gene.b0046"
entity_type: "gene"
name: "kefF"
source_database: "NCBI RefSeq"
source_id: "gene-b0046"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0046"
  - "kefF"
---

# kefF

`gene.b0046`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0046`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

kefF (gene.b0046) is a gene entity. It encodes kefF (protein.P0A754). Encoded protein function: FUNCTION: Regulatory subunit of a potassium efflux system that confers protection against electrophiles. Required for full activity of KefC. Shows redox enzymatic activity, but this enzymatic activity is not required for activation of KefC. Can use a wide range of substrates, including electrophilic quinones, and its function could be to reduce the redox toxicity of electrophilic quinones in parallel with acting as triggers for the KefC efflux system. {ECO:0000255|HAMAP-Rule:MF_01414, ECO:0000269|PubMed:11053405, ECO:0000269|PubMed:19523906, ECO:0000269|PubMed:21742892}. EcoCyc product frame: EG11568-MONOMER. EcoCyc synonyms: yabF. Genomic coordinates: 47246-47776.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A754|protein.P0A754]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000159,ECOCYC:EG11568,GeneID:944767`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:47246-47776:+; feature_type=gene
