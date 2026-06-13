---
entity_id: "gene.b1705"
entity_type: "gene"
name: "ydiE"
source_database: "NCBI RefSeq"
source_id: "gene-b1705"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1705"
  - "ydiE"
---

# ydiE

`gene.b1705`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1705`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydiE (gene.b1705) is a gene entity. It encodes ydiE (protein.P0ACX9). Encoded protein function: Uncharacterized protein YdiE EcoCyc product frame: EG12391-MONOMER. Genomic coordinates: 1789613-1789804.

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACX9|protein.P0ACX9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=ydiE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005692,ECOCYC:EG12391,GeneID:946205`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1789613-1789804:+; feature_type=gene
