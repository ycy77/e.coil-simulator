---
entity_id: "gene.b3614"
entity_type: "gene"
name: "yibQ"
source_database: "NCBI RefSeq"
source_id: "gene-b3614"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3614"
  - "yibQ"
---

# yibQ

`gene.b3614`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3614`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yibQ (gene.b3614) is a gene entity. It encodes yibQ (protein.P37691). Encoded protein function: Uncharacterized protein YibQ EcoCyc product frame: EG12298-MONOMER. Genomic coordinates: 3788101-3789060. EcoCyc protein note: Based on sequence similarity, YibQ was predicted to be a nucleoside (IDP) diphosphatase .

## Biological Role

Repressed by cra (protein.P0ACP1), yeiE (protein.P0ACR4).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37691|protein.P37691]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=yibQ; function=-
- `represses` <-- [[protein.P0ACR4|protein.P0ACR4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011824,ECOCYC:EG12298,GeneID:948128`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3788101-3789060:+; feature_type=gene
