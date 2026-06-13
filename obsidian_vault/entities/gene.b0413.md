---
entity_id: "gene.b0413"
entity_type: "gene"
name: "nrdR"
source_database: "NCBI RefSeq"
source_id: "gene-b0413"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0413"
  - "nrdR"
---

# nrdR

`gene.b0413`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0413`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nrdR (gene.b0413) is a gene entity. It encodes nrdR (protein.P0A8D0). Encoded protein function: FUNCTION: Represses transcription of the class Ib RNR genes nrdHIEF but has much smaller effect on transcription of the class Ia RNR genes nrdAB and class III RNR genes nrdDG. By binding to nrdR boxes in the promoter regions to alter promoter activity, nrdR differentially regulates nrdAB, nrdHIEF and nrdD transcription in aerobic growth. {ECO:0000269|PubMed:17496099}. EcoCyc product frame: EG11320-MONOMER. EcoCyc synonyms: ybaD. Genomic coordinates: 433002-433451.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8D0|protein.P0A8D0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001437,ECOCYC:EG11320,GeneID:947437`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:433002-433451:+; feature_type=gene
