---
entity_id: "gene.b4204"
entity_type: "gene"
name: "yjfZ"
source_database: "NCBI RefSeq"
source_id: "gene-b4204"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4204"
  - "yjfZ"
---

# yjfZ

`gene.b4204`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4204`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjfZ (gene.b4204) is a gene entity. It encodes yjfZ (protein.P39308). Encoded protein function: Uncharacterized protein YjfZ EcoCyc product frame: G7862-MONOMER. Genomic coordinates: 4426628-4427422. EcoCyc protein note: No information about this protein was found by a literature search conducted on May 17, 2021.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39308|protein.P39308]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yjfZ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013748,ECOCYC:G7862,GeneID:948719`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4426628-4427422:-; feature_type=gene
