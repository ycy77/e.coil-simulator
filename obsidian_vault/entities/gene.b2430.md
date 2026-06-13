---
entity_id: "gene.b2430"
entity_type: "gene"
name: "yfeW"
source_database: "NCBI RefSeq"
source_id: "gene-b2430"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2430"
  - "yfeW"
---

# yfeW

`gene.b2430`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2430`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfeW (gene.b2430) is a gene entity. It encodes yfeW (protein.P77619). Encoded protein function: FUNCTION: Penicillin-binding protein. Has low DD-carboxypeptidase activity. {ECO:0000269|PubMed:16402224}. EcoCyc product frame: G7265-MONOMER. Genomic coordinates: 2548102-2549406. EcoCyc protein note: Purified YfeW can bind penicillin and displays a low level of DD-carboxypeptidase activity . yfeW is non-essential . MurQP-yfeW may constitute an operon in E. coli K-12 . Deleting yfeW does not affect growth on N-acetylmuramic acid .

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77619|protein.P77619]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008012,ECOCYC:G7265,GeneID:946907`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2548102-2549406:+; feature_type=gene
