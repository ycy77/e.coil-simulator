---
entity_id: "gene.b4688"
entity_type: "gene"
name: "ykgS"
source_database: "NCBI RefSeq"
source_id: "gene-b4688"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4688"
  - "ykgS"
---

# ykgS

`gene.b4688`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4688`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ykgS (gene.b4688) is a gene entity. It encodes ykgS (protein.P0DPM8). Encoded protein function: Protein YkgS EcoCyc product frame: MONOMER0-4436. Genomic coordinates: 290510-290638. EcoCyc protein note: YkgS was identified as an expressed small protein; expression is higher during stationary phase than during exponential phase . The sequence identity of YkgS with G7360-MONOMER YfjI extends upstream of the open reading frame used here. Comment in EcoGene: "Pseudogene internal fragment; CP4-6 putative prophage remnant. Upstream of argF, at the insertion point of IS1C, ykgR' is a pseudogene copy of amino acids 300-367 of YfjI, a protein of unknown function in the CP4-57 prophage."

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DPM8|protein.P0DPM8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0285250,ECOCYC:G0-16674,GeneID:7751632`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:290510-290638:+; feature_type=gene
