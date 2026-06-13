---
entity_id: "gene.b2354"
entity_type: "gene"
name: "yfdK"
source_database: "NCBI RefSeq"
source_id: "gene-b2354"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2354"
  - "yfdK"
---

# yfdK

`gene.b2354`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2354`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfdK (gene.b2354) is a gene entity. It encodes yfdK (protein.P77656). Encoded protein function: Uncharacterized protein YfdK EcoCyc product frame: G7223-MONOMER. Genomic coordinates: 2471077-2471517. EcoCyc protein note: Deletion of yfdK, yfdO or yfdS genes or the entire CPS-53 prophage reduces viability under conditions of oxidative stress .

## Biological Role

Activated by ygfI (protein.P52044).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77656|protein.P77656]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `C` - regulator=SrsR; target=yfdK; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007770,ECOCYC:G7223,GeneID:948822`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2471077-2471517:-; feature_type=gene
