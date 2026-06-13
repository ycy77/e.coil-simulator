---
entity_id: "gene.b1365"
entity_type: "gene"
name: "ynaK"
source_database: "NCBI RefSeq"
source_id: "gene-b1365"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1365"
  - "ynaK"
---

# ynaK

`gene.b1365`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1365`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ynaK (gene.b1365) is a gene entity. It encodes ynaK (protein.P76068). Encoded protein function: ParB-like nuclease domain-containing protein YnaK EcoCyc product frame: G6688-MONOMER. Genomic coordinates: 1425377-1425640. EcoCyc protein note: No information about this protein was found by a literature search conducted on March 21, 2017.

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76068|protein.P76068]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ynaK; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004571,ECOCYC:G6688,GeneID:947417`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1425377-1425640:+; feature_type=gene
