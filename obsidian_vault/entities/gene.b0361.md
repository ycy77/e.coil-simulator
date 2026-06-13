---
entity_id: "gene.b0361"
entity_type: "gene"
name: "insD1"
source_database: "NCBI RefSeq"
source_id: "gene-b0361"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0361"
  - "insD1"
---

# insD1

`gene.b0361`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0361`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

insD1 (gene.b0361) is a gene entity. It encodes insD1 (protein.P0CF53). Encoded protein function: FUNCTION: Involved in the transposition of the insertion sequence IS2. EcoCyc product frame: G7480-MONOMER. EcoCyc synonyms: yi22-1. Genomic coordinates: 381674-382579. EcoCyc protein note: No specific function has been identified for this protein that is coded for by the IS2 insertion sequence element. IS2 is an insertion sequence present in from 0-12 copies in various strains of E. coli . Though it can cause activation and suppression of adjacent genes, activation appears to be due to generation of novel promoters during the insertion process rather than to the presence of promoters carried within IS2 . In addition to autoregulation by InsA, transcription of IS2 genes is negatively regulated by CPLX0-226 . IS2 locations in the E. coli genome correlate with Hfr origins and F' factor crossover points .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0CF53|protein.P0CF53]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001239,ECOCYC:G6213,GeneID:945203`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:381674-382579:+; feature_type=gene
