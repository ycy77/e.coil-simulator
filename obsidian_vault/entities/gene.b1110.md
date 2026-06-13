---
entity_id: "gene.b1110"
entity_type: "gene"
name: "ycfJ"
source_database: "NCBI RefSeq"
source_id: "gene-b1110"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1110"
  - "ycfJ"
---

# ycfJ

`gene.b1110`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1110`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycfJ (gene.b1110) is a gene entity. It encodes ycfJ (protein.P0AB35). Encoded protein function: Uncharacterized protein YcfJ EcoCyc product frame: EG12444-MONOMER. Genomic coordinates: 1167599-1168138. EcoCyc protein note: YcfJ has similarity to Proteus mirabilis UmoD, which is involved in in flagellar synthesis, swarming, and cell elongation . YcfJ is predicted to be a bitopic inner membrane protein . Transcription of ycfJ is induced upon biofilm formation compared to planktonic growth in exponential phase. Induction of expression was found to be independent of the presence of the F plasmid . A ycfJ mutant is impaired in biofilm formation . ycfJ was in the top 20 genes with increased translation in response to extreme acid stress (pH 4.4 and 5.8 compared to pH 7.6) and shown to have increased transcription in response to low pH, H2O oxidative stress and ethanol stress as measured by mRNA levels by RT-qPCR .

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB35|protein.P0AB35]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003752,ECOCYC:EG12444,GeneID:945977`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1167599-1168138:+; feature_type=gene
