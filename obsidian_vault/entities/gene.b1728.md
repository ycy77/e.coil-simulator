---
entity_id: "gene.b1728"
entity_type: "gene"
name: "ydjM"
source_database: "NCBI RefSeq"
source_id: "gene-b1728"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1728"
  - "ydjM"
---

# ydjM

`gene.b1728`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1728`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydjM (gene.b1728) is a gene entity. It encodes ydjM (protein.P64481). Encoded protein function: Inner membrane protein YdjM EcoCyc product frame: G6933-MONOMER. Genomic coordinates: 1810211-1810801. EcoCyc protein note: YdjM is an inner membrane protein with four predicted transmembrane domains. The C terminus is located in the periplasm . Expression of ydjM appears to be regulated by LexA . Transcription is induced by nalidixic acid .

## Biological Role

Repressed by lexA (protein.P0A7C2).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64481|protein.P64481]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A7C2|protein.P0A7C2]] `RegulonDB` `S` - regulator=LexA; target=ydjM; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005768,ECOCYC:G6933,GeneID:945644`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1810211-1810801:+; feature_type=gene
