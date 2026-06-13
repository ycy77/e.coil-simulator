---
entity_id: "gene.b2555"
entity_type: "gene"
name: "qseG"
source_database: "NCBI RefSeq"
source_id: "gene-b2555"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2555"
  - "qseG"
---

# qseG

`gene.b2555`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2555`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

qseG (gene.b2555) is a gene entity. It encodes yfhG (protein.P0AD44). Encoded protein function: Uncharacterized protein YfhG EcoCyc product frame: EG12139-MONOMER. EcoCyc synonyms: yfhG. Genomic coordinates: 2688793-2689506. EcoCyc protein note: QseG is a periplasmic facing outer membrane lipoprotein which physically interacts with the G7345-MONOMER "GlrK histidine kinase" and activates the PWY0-1503. qseG is a multicopy inducer of RPOE-MONOMER "rpoE"; transcription is significantly pronounced from the RpoN regulated P2 promoter (rpoEP2) and is abrogated in a ΔglrR strain . QseG activates the PWY0-1503 (also known as QseEF) which regulates transcription of rpoE - it is one of the multiple systems which regulate transcription of rpoE in response to a variety of stress conditions . QseG is present in the cell envelope of E. coli K-12; levels of the TKE1-RNA are significantly reduced in a ΔqseG strain and QseG is required for efficient transcription from the σ54-dependent promoter of glmY; it has no role in transcription from the σ70-dependent promoter of glmY...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD44|protein.P0AD44]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008405,ECOCYC:EG12139,GeneID:947010`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2688793-2689506:-; feature_type=gene
