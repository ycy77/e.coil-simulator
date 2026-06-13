---
entity_id: "gene.b0817"
entity_type: "gene"
name: "mntR"
source_database: "NCBI RefSeq"
source_id: "gene-b0817"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0817"
  - "mntR"
---

# mntR

`gene.b0817`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0817`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mntR (gene.b0817) is a gene entity. It encodes mntR (protein.P0A9F1). Encoded protein function: FUNCTION: In the presence of manganese, represses expression of mntH and mntS. Up-regulates expression of mntP. {ECO:0000269|PubMed:11466284, ECO:0000269|PubMed:21908668}. EcoCyc product frame: G6420-MONOMER. EcoCyc synonyms: ybiQ. Genomic coordinates: 853183-853650.

## Biological Role

Activated by ATP-dependent RNA helicase DeaD (complex.ecocyc.CPLX0-8557).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9F1|protein.P0A9F1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[complex.ecocyc.CPLX0-8557|complex.ecocyc.CPLX0-8557]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation

## External IDs

- `Dbxref:ASAP:ABE-0002793,ECOCYC:G6420,GeneID:945437`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:853183-853650:+; feature_type=gene
