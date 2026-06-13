---
entity_id: "gene.b2869"
entity_type: "gene"
name: "ygeV"
source_database: "NCBI RefSeq"
source_id: "gene-b2869"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2869"
  - "ygeV"
---

# ygeV

`gene.b2869`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2869`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygeV (gene.b2869) is a gene entity. It encodes uacR (protein.Q46802). Encoded protein function: FUNCTION: Essential for both formate-dependent and formate-independent uric acid degradation. May be directly involved in the transcription of uacF in response to hypoxanthine, xanthine, and uric acid. {ECO:0000269|PubMed:30885932}. EcoCyc product frame: G7488-MONOMER. Genomic coordinates: 3004008-3005786. EcoCyc protein note: YgeV is required for both formate-dependent and formate-independent degradation of urate . Expression of ygeV is induced by the quorum-sensing signal autoinducer 2 (AI-2) . YgeV was transcriptionally upregulated in iron excess over iron limitation at 63% dissolved oxygen as determined by RNA-seq .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46802|protein.Q46802]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009420,ECOCYC:G7488,GeneID:947320`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3004008-3005786:-; feature_type=gene
