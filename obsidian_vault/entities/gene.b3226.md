---
entity_id: "gene.b3226"
entity_type: "gene"
name: "nanR"
source_database: "NCBI RefSeq"
source_id: "gene-b3226"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3226"
  - "nanR"
---

# nanR

`gene.b3226`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3226`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nanR (gene.b3226) is a gene entity. It encodes nanR (protein.P0A8W0). Encoded protein function: FUNCTION: Transcriptional repressor that controls expression of the genes required for the catabolism of sialic acids (PubMed:12897000, PubMed:23935044, PubMed:9864311). Represses expression of the nanATEK-yhcH, nanCMS and yjhBC operons. Acts by binding directly to the Nan box, a region of approximately 30 bp covering the promoter region (PubMed:23935044). {ECO:0000269|PubMed:12897000, ECO:0000269|PubMed:23935044, ECO:0000269|PubMed:9864311}. EcoCyc product frame: G7678-MONOMER. EcoCyc synonyms: yhcK. Genomic coordinates: 3373698-3374489.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8W0|protein.P0A8W0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010584,ECOCYC:G7678,GeneID:945468`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3373698-3374489:-; feature_type=gene
