---
entity_id: "gene.b0380"
entity_type: "gene"
name: "yaiZ"
source_database: "NCBI RefSeq"
source_id: "gene-b0380"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0380"
  - "yaiZ"
---

# yaiZ

`gene.b0380`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0380`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yaiZ (gene.b0380) is a gene entity. It encodes yaiZ (protein.P0AAQ0). Encoded protein function: Uncharacterized protein YaiZ EcoCyc product frame: G6229-MONOMER. Genomic coordinates: 399593-399805. EcoCyc protein note: Deuterated YaiZ protein suitable for NMR has been prepared .

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAQ0|protein.P0AAQ0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yaiZ; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001307,ECOCYC:G6229,GeneID:947355`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:399593-399805:+; feature_type=gene
