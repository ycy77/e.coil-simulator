---
entity_id: "gene.b0866"
entity_type: "gene"
name: "ybjQ"
source_database: "NCBI RefSeq"
source_id: "gene-b0866"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0866"
  - "ybjQ"
---

# ybjQ

`gene.b0866`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0866`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybjQ (gene.b0866) is a gene entity. It encodes ybjQ (protein.P0A8C1). Encoded protein function: UPF0145 protein YbjQ EcoCyc product frame: G6451-MONOMER. Genomic coordinates: 904593-904916. EcoCyc protein note: No information about this protein was found by a literature search conducted on April 7, 2017.

## Biological Role

Repressed by nac (protein.Q47005). Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8C1|protein.P0A8C1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ybjQ; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ybjQ; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002945,ECOCYC:G6451,GeneID:945493`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:904593-904916:+; feature_type=gene
