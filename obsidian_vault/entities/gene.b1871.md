---
entity_id: "gene.b1871"
entity_type: "gene"
name: "cmoB"
source_database: "NCBI RefSeq"
source_id: "gene-b1871"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1871"
  - "cmoB"
---

# cmoB

`gene.b1871`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1871`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cmoB (gene.b1871) is a gene entity. It encodes cmoB (protein.P76291). Encoded protein function: FUNCTION: Catalyzes carboxymethyl transfer from carboxy-S-adenosyl-L-methionine (Cx-SAM) to 5-hydroxyuridine (ho5U) to form 5-carboxymethoxyuridine (cmo5U) at position 34 in tRNAs. Can also catalyze the SAM-dependent methylation of ho5U, with much lower efficiency. {ECO:0000269|PubMed:23676670, ECO:0000269|PubMed:25855808}. EcoCyc product frame: G7021-MONOMER. EcoCyc synonyms: yecP. Genomic coordinates: 1953442-1954413.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76291|protein.P76291]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006241,ECOCYC:G7021,GeneID:946387`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1953442-1954413:+; feature_type=gene
