---
entity_id: "gene.b3028"
entity_type: "gene"
name: "mdaB"
source_database: "NCBI RefSeq"
source_id: "gene-b3028"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3028"
  - "mdaB"
---

# mdaB

`gene.b3028`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3028`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mdaB (gene.b3028) is a gene entity. It encodes mdaB (protein.P0AEY5). Encoded protein function: FUNCTION: NADPH-specific quinone reductase (PubMed:8611590). Is most active with quinone derivatives and ferricyanide as electron acceptors (PubMed:8611590). Can use menadione, 1,4-naphthoquinone and 1,4-benzoquinone (PubMed:8611590). May work in concert with YgiN to form a quinone redox cycle (PubMed:15613473). {ECO:0000269|PubMed:15613473, ECO:0000269|PubMed:8611590}. EcoCyc product frame: EG12656-MONOMER. EcoCyc synonyms: mda66. Genomic coordinates: 3172530-3173111.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEY5|protein.P0AEY5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009946,ECOCYC:EG12656,GeneID:947512`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3172530-3173111:+; feature_type=gene
