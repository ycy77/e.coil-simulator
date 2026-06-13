---
entity_id: "gene.b0579"
entity_type: "gene"
name: "ybdF"
source_database: "NCBI RefSeq"
source_id: "gene-b0579"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0579"
  - "ybdF"
---

# ybdF

`gene.b0579`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0579`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybdF (gene.b0579) is a gene entity. It encodes ybdF (protein.P0AAT2). Encoded protein function: Uncharacterized protein YbdF EcoCyc product frame: G6324-MONOMER. Genomic coordinates: 605518-605886. EcoCyc protein note: No information about this protein was found by a literature search conducted on November 16, 2020.

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAT2|protein.P0AAT2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001986,ECOCYC:G6324,GeneID:948302`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:605518-605886:-; feature_type=gene
