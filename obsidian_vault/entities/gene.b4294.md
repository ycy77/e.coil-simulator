---
entity_id: "gene.b4294"
entity_type: "gene"
name: "insA7"
source_database: "NCBI RefSeq"
source_id: "gene-b4294"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4294"
  - "insA7"
---

# insA7

`gene.b4294`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4294`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

insA7 (gene.b4294) is a gene entity. It encodes insA7 (protein.P19767). Encoded protein function: FUNCTION: Absolutely required for transposition of IS1. EcoCyc product frame: G7908-MONOMER. Genomic coordinates: 4518527-4518802. EcoCyc protein note: insA-7 is a fragment of the IS1 insertion sequence coding for the transcriptional repressor protein InsA . Normally, IS1 codes for three proteins, but the IS1 sequence that codes for insA-7 contains a nonsense mutation that prevents the translation of the InsB and InsAB' proteins .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P19767|protein.P19767]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0014077,ECOCYC:G7908,GeneID:948830`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4518527-4518802:+; feature_type=gene
