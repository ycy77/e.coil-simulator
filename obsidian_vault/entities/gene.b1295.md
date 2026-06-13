---
entity_id: "gene.b1295"
entity_type: "gene"
name: "ymjA"
source_database: "NCBI RefSeq"
source_id: "gene-b1295"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1295"
  - "ymjA"
---

# ymjA

`gene.b1295`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1295`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ymjA (gene.b1295) is a gene entity. It encodes ymjA (protein.P0ACV8). Encoded protein function: Uncharacterized protein YmjA EcoCyc product frame: G6642-MONOMER. Genomic coordinates: 1357423-1357668. EcoCyc protein note: No information about this protein was found by a literature search conducted on February 23, 2017.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACV8|protein.P0ACV8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ymjA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004359,ECOCYC:G6642,GeneID:945874`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1357423-1357668:-; feature_type=gene
