---
entity_id: "gene.b4487"
entity_type: "gene"
name: "yjdP"
source_database: "NCBI RefSeq"
source_id: "gene-b4487"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4487"
  - "yjdP"
---

# yjdP

`gene.b4487`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4487`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjdP (gene.b4487) is a gene entity. It encodes yjdP (protein.Q6BEX5). Encoded protein function: Uncharacterized protein YjdP EcoCyc product frame: MONOMER0-1541. Genomic coordinates: 4313868-4314197. EcoCyc protein note: A hypothetical protein, PhnQ, encoded on the opposite strand was originally thought to be part of the phn operon . The phnQ gene (b4091) has been deaccessioned. No information about the YjdP protein has been found by a database search conducted on February 24, 2017.

## Biological Role

Repressed by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q6BEX5|protein.Q6BEX5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yjdP; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0174120,ECOCYC:G0-9541,GeneID:2847754`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4313868-4314197:+; feature_type=gene
