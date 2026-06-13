---
entity_id: "gene.b2358"
entity_type: "gene"
name: "yfdO"
source_database: "NCBI RefSeq"
source_id: "gene-b2358"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2358"
  - "yfdO"
---

# yfdO

`gene.b2358`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2358`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfdO (gene.b2358) is a gene entity. It encodes yfdO (protein.P0AD35). Encoded protein function: Protein YfdO EcoCyc product frame: G7227-MONOMER. EcoCyc synonyms: oweS. Genomic coordinates: 2472878-2473246. EcoCyc protein note: Deletion of yfdK, yfdO or yfdS genes or the entire CPS-53 prophage reduces viability under conditions of oxidative stress . Overexpression of yfdO slightly increases resistance to the antibiotic nalidixic acid .

## Biological Role

Activated by ygfI (protein.P52044).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD35|protein.P0AD35]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `C` - regulator=SrsR; target=yfdO; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007779,ECOCYC:G7227,GeneID:947403`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2472878-2473246:-; feature_type=gene
