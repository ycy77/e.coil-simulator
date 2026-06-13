---
entity_id: "gene.b3090"
entity_type: "gene"
name: "ygjV"
source_database: "NCBI RefSeq"
source_id: "gene-b3090"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3090"
  - "ygjV"
---

# ygjV

`gene.b3090`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3090`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygjV (gene.b3090) is a gene entity. It encodes ygjV (protein.P42603). Encoded protein function: Inner membrane protein YgjV EcoCyc product frame: G7608-MONOMER. Genomic coordinates: 3241193-3241744. EcoCyc protein note: Protein topology in the inner membrane has been determined .

## Biological Role

Repressed by plaR (protein.P37671).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P42603|protein.P42603]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37671|protein.P37671]] `RegulonDB|EcoCyc` `C` - regulator=PlaR; target=ygjV; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010161,ECOCYC:G7608,GeneID:947604`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3241193-3241744:-; feature_type=gene
