---
entity_id: "gene.b1377"
entity_type: "gene"
name: "ompN"
source_database: "NCBI RefSeq"
source_id: "gene-b1377"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1377"
  - "ompN"
---

# ompN

`gene.b1377`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1377`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ompN (gene.b1377) is a gene entity. It encodes ompN (protein.P77747). Encoded protein function: FUNCTION: Forms pores that allow passive diffusion of small molecules across the outer membrane (By similarity). Non-specific porin. {ECO:0000250}. EcoCyc product frame: G6700-MONOMER. EcoCyc synonyms: ynaG. Genomic coordinates: 1435760-1436893. EcoCyc protein note: Though under typical laboratory growth conditions OmpN is not highly expressed, when overexpressed it operates as a porin with single-channel conductance properties similar to those of OmpC . OmpN abundance is regulated by TKE8-RNA. ompN exhibits mosaic evolution patterns in E. coli .

## Biological Role

Repressed by nac (protein.Q47005). Activated by soxS (protein.P0A9E2).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77747|protein.P77747]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `C` - regulator=SoxS; target=ompN; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ompN; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004608,ECOCYC:G6700,GeneID:946313`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1435760-1436893:-; feature_type=gene
