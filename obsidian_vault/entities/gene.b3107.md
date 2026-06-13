---
entity_id: "gene.b3107"
entity_type: "gene"
name: "yhaL"
source_database: "NCBI RefSeq"
source_id: "gene-b3107"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3107"
  - "yhaL"
---

# yhaL

`gene.b3107`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3107`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhaL (gene.b3107) is a gene entity. It encodes yhaL (protein.P42625). Encoded protein function: Uncharacterized protein YhaL EcoCyc product frame: G7621-MONOMER. Genomic coordinates: 3255043-3255207. EcoCyc protein note: No information about this protein was found by a literature search conducted on June 23, 2017.

## Biological Role

Activated by yhaJ (protein.P67660).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P42625|protein.P42625]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P67660|protein.P67660]] `RegulonDB` `S` - regulator=YhaJ; target=yhaL; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010219,ECOCYC:G7621,GeneID:947618`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3255043-3255207:+; feature_type=gene
