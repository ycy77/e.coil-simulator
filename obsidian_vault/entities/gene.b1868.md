---
entity_id: "gene.b1868"
entity_type: "gene"
name: "yecE"
source_database: "NCBI RefSeq"
source_id: "gene-b1868"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1868"
  - "yecE"
---

# yecE

`gene.b1868`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1868`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yecE (gene.b1868) is a gene entity. It encodes yecE (protein.P37348). Encoded protein function: UPF0759 protein YecE EcoCyc product frame: EG12379-MONOMER. Genomic coordinates: 1951395-1952213. EcoCyc protein note: The yecE gene is the site of integration for the lysogenic prophage φ297 as well as for a prophage found in isolates of the sorbitol-fermenting enterohemorrhagic E. coli strain O157:NM .

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37348|protein.P37348]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yecE; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006233,ECOCYC:EG12379,GeneID:946382`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1951395-1952213:+; feature_type=gene
