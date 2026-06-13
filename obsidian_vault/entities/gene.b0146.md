---
entity_id: "gene.b0146"
entity_type: "gene"
name: "sfsA"
source_database: "NCBI RefSeq"
source_id: "gene-b0146"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0146"
  - "sfsA"
---

# sfsA

`gene.b0146`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0146`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sfsA (gene.b0146) is a gene entity. It encodes sfsA (protein.P0A823). Encoded protein function: FUNCTION: Binds to DNA non-specifically. Could be a regulatory factor involved in maltose metabolism. {ECO:0000255|HAMAP-Rule:MF_00095, ECO:0000269|PubMed:11272834, ECO:0000269|PubMed:2013578}. EcoCyc product frame: EG10949-MONOMER. EcoCyc synonyms: sfs, sfs1. Genomic coordinates: 160782-161486. EcoCyc protein note: SfsA may be a transcription factor involved in regulation of maltose metabolism. Overexpression of SfsA yields a 10-fold increase in amylomaltose (MalQ) activity as well as an increase in maltose-binding protein (MalE) levels . This MalT-dependent increase occurs at the level of transcription . In vitro, SfsA binds DNA nonspecifically . It contains a PD-(D/E)XK domain, which is found in a number of DNA-related proteins . There is no apparent phenotypic consequence of disrupting sfsA . The sfsA ORF contains an out-of-frame internal translation initiation site that is able to direct translation initiation in vivo . SfsA: "sugar fermentation stimulation"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A823|protein.P0A823]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000503,ECOCYC:EG10949,GeneID:944855`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:160782-161486:-; feature_type=gene
