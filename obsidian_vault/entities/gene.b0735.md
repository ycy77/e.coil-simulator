---
entity_id: "gene.b0735"
entity_type: "gene"
name: "ybgE"
source_database: "NCBI RefSeq"
source_id: "gene-b0735"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0735"
  - "ybgE"
---

# ybgE

`gene.b0735`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0735`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybgE (gene.b0735) is a gene entity. It encodes ybgE (protein.P0AAV0). Encoded protein function: Uncharacterized protein YbgE EcoCyc product frame: EG12395-MONOMER. Genomic coordinates: 774309-774602. EcoCyc protein note: No information about this protein was found by a literature search conducted on November 16, 2020.

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAV0|protein.P0AAV0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ybgE; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002505,ECOCYC:EG12395,GeneID:945326`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:774309-774602:+; feature_type=gene
