---
entity_id: "gene.b1161"
entity_type: "gene"
name: "ycgX"
source_database: "NCBI RefSeq"
source_id: "gene-b1161"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1161"
  - "ycgX"
---

# ycgX

`gene.b1161`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1161`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycgX (gene.b1161) is a gene entity. It encodes ycgX (protein.P75988). Encoded protein function: Uncharacterized protein YcgX EcoCyc product frame: G6601-MONOMER. Genomic coordinates: 1212703-1213107. EcoCyc protein note: No information about this protein was found by a literature search conducted on September 20, 2018.

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75988|protein.P75988]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ycgX; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003897,ECOCYC:G6601,GeneID:945733`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1212703-1213107:-; feature_type=gene
