---
entity_id: "gene.b2774"
entity_type: "gene"
name: "ygcW"
source_database: "NCBI RefSeq"
source_id: "gene-b2774"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2774"
  - "ygcW"
---

# ygcW

`gene.b2774`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2774`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygcW (gene.b2774) is a gene entity. It encodes ygcW (protein.P76633). Encoded protein function: Uncharacterized oxidoreductase YgcW (EC 1.-.-.-) EcoCyc product frame: G7440-MONOMER. Genomic coordinates: 2899488-2900273. EcoCyc protein note: No information about this protein was found by a literature search conducted on February 13, 2006.

## Biological Role

Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76633|protein.P76633]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ygcW; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009088,ECOCYC:G7440,GeneID:947232`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2899488-2900273:-; feature_type=gene
