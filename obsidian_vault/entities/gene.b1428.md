---
entity_id: "gene.b1428"
entity_type: "gene"
name: "ydcK"
source_database: "NCBI RefSeq"
source_id: "gene-b1428"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1428"
  - "ydcK"
---

# ydcK

`gene.b1428`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1428`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydcK (gene.b1428) is a gene entity. It encodes ydcK (protein.P76100). Encoded protein function: Uncharacterized acetyltransferase YdcK (EC 2.3.1.-) EcoCyc product frame: G6741-MONOMER. Genomic coordinates: 1499469-1500449. EcoCyc protein note: YdcK shows a low sequence similarity to PMP6 from Chlamydophila pneumoniae . A ΔydcK mutant has aggravating genetic interactions with genes involved in DNA recombination .

## Biological Role

Repressed by glaR (protein.P37338). Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76100|protein.P76100]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=ydcK; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004765,ECOCYC:G6741,GeneID:944932`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1499469-1500449:-; feature_type=gene
