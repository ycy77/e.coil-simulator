---
entity_id: "gene.b1523"
entity_type: "gene"
name: "yneG"
source_database: "NCBI RefSeq"
source_id: "gene-b1523"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1523"
  - "yneG"
---

# yneG

`gene.b1523`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1523`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yneG (gene.b1523) is a gene entity. It encodes yneG (protein.P76148). Encoded protein function: Uncharacterized protein YneG EcoCyc product frame: G6809-MONOMER. Genomic coordinates: 1611966-1612325. EcoCyc protein note: No information about this protein was found by a literature search conducted on November 14, 2018.

## Biological Role

Activated by yneJ (protein.P77309).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76148|protein.P76148]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P77309|protein.P77309]] `RegulonDB` `S` - regulator=PtrR; target=yneG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005084,ECOCYC:G6809,GeneID:946171`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1611966-1612325:-; feature_type=gene
