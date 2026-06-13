---
entity_id: "gene.b0546"
entity_type: "gene"
name: "ybcM"
source_database: "NCBI RefSeq"
source_id: "gene-b0546"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0546"
  - "ybcM"
---

# ybcM

`gene.b0546`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0546`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybcM (gene.b0546) is a gene entity. It encodes ybcM (protein.P77634). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YbcM EcoCyc product frame: G6302-MONOMER. Genomic coordinates: 571454-572251. EcoCyc protein note: YbcM was predicted to be an AraC-type transcription factor , and it contains a helix-turn-helix motif to bind DNA in its C-terminal domain . DNA binding of YbcM was probed in vivo, in glucose M9 minimal medium under oxidative conditions, through chromatin immunoprecipitation assays (ChIP-exo) . Some binding target genes were found to be related to the stress response, but the effect of YbcM on transcription still needs to be studied . On the other hand, it was predicted to regulate genes related to metabolism and processes related to phages . Upstream of the ybcM gene, a sequence was found that could work as a transcriptional promoter, and the transcription of the ybcM gene is affected by amino acid starvation . ybcM was identified in a screen for genes that reduce the lethal effects of stress. A ybcM insertion mutant was more sensitive than wild type to mitomycin C and other stresses . A knockout mutant for the ybcM gene was more susceptible to H2O2 than the wild-type strain, which showed a survival rate 8-fold higher than the ybcM deletion strain after treatment with 60 mM H2O2 in glucose M9 minimal medium...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77634|protein.P77634]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001871,ECOCYC:G6302,GeneID:945163`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:571454-572251:+; feature_type=gene
