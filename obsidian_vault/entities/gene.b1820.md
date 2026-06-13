---
entity_id: "gene.b1820"
entity_type: "gene"
name: "yobD"
source_database: "NCBI RefSeq"
source_id: "gene-b1820"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1820"
  - "yobD"
---

# yobD

`gene.b1820`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1820`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yobD (gene.b1820) is a gene entity. It encodes yobD (protein.P67601). Encoded protein function: UPF0266 membrane protein YobD EcoCyc product frame: G6998-MONOMER. Genomic coordinates: 1904801-1905259. EcoCyc protein note: YobD is an inner membrane protein with two predicted transmembrane domains. The C terminus is located in the cytoplasm .

## Biological Role

Repressed by glaR (protein.P37338). Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P67601|protein.P67601]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yobD; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006062,ECOCYC:G6998,GeneID:946343`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1904801-1905259:+; feature_type=gene
