---
entity_id: "gene.b0295"
entity_type: "gene"
name: "ykgL"
source_database: "NCBI RefSeq"
source_id: "gene-b0295"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0295"
  - "ykgL"
---

# ykgL

`gene.b0295`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0295`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ykgL (gene.b0295) is a gene entity. It encodes ykgL (protein.P56257). Encoded protein function: Uncharacterized protein YkgL EcoCyc product frame: G6166-MONOMER. Genomic coordinates: 312112-312339. EcoCyc protein note: No information about this protein was found by a literature search conducted on July 12, 2017.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P56257|protein.P56257]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ykgL; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001019,ECOCYC:G6166,GeneID:944962`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:312112-312339:+; feature_type=gene
