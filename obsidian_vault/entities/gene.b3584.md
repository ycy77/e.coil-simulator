---
entity_id: "gene.b3584"
entity_type: "gene"
name: "yiaT"
source_database: "NCBI RefSeq"
source_id: "gene-b3584"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3584"
  - "yiaT"
---

# yiaT

`gene.b3584`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3584`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yiaT (gene.b3584) is a gene entity. It encodes yiaT (protein.P37681). Encoded protein function: Putative outer membrane protein YiaT EcoCyc product frame: EG12288-MONOMER. Genomic coordinates: 3751128-3751868. EcoCyc protein note: YiaT is a putative outer membrane protein . YiaT is predicted to contain 10 transmembrane β strands and 5 outer-exposed loops. C-terminal truncated YiaT has been used as a membrane anchor for the surface display of selected proteins . A ΔyiaT mutant has aggravating genetic interactions with genes involved in mismatch repair .

## Biological Role

Activated by yiaU (protein.P37682).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37681|protein.P37681]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P37682|protein.P37682]] `RegulonDB|EcoCyc` `C` - regulator=YiaU; target=yiaT; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011704,ECOCYC:EG12288,GeneID:948097`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3751128-3751868:-; feature_type=gene
