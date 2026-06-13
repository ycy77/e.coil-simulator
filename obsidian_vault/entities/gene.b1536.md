---
entity_id: "gene.b1536"
entity_type: "gene"
name: "ydeI"
source_database: "NCBI RefSeq"
source_id: "gene-b1536"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1536"
  - "ydeI"
---

# ydeI

`gene.b1536`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1536`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydeI (gene.b1536) is a gene entity. It encodes ydeI (protein.P31130). Encoded protein function: Uncharacterized protein YdeI EcoCyc product frame: EG11644-MONOMER. Genomic coordinates: 1624105-1624497. EcoCyc protein note: YdeI is involved in the cellular response to hydrogen peroxide stress . A ydeI mutant is more sensitive to hydrogen peroxide stress than wild type and shows increased biofilm formation .

## Biological Role

Activated by rcdA (protein.P75811).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31130|protein.P31130]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P75811|protein.P75811]] `RegulonDB` `S` - regulator=RcdA; target=ydeI; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005127,ECOCYC:EG11644,GeneID:946068`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1624105-1624497:-; feature_type=gene
