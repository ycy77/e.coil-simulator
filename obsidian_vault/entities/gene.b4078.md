---
entity_id: "gene.b4078"
entity_type: "gene"
name: "yjcO"
source_database: "NCBI RefSeq"
source_id: "gene-b4078"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4078"
  - "yjcO"
---

# yjcO

`gene.b4078`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4078`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjcO (gene.b4078) is a gene entity. It encodes yjcO (protein.P0AF56). Encoded protein function: Sel1-repeat-containing protein YjcO EcoCyc product frame: EG11951-MONOMER. Genomic coordinates: 4296436-4297125. EcoCyc protein note: No information about this protein was found by a literature search conducted on March 17, 2017.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF56|protein.P0AF56]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yjcO; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013360,ECOCYC:EG11951,GeneID:948586`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4296436-4297125:-; feature_type=gene
