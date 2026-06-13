---
entity_id: "gene.b2984"
entity_type: "gene"
name: "yghR"
source_database: "NCBI RefSeq"
source_id: "gene-b2984"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2984"
  - "yghR"
---

# yghR

`gene.b2984`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2984`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yghR (gene.b2984) is a gene entity. It encodes yghR (protein.P64572). Encoded protein function: Uncharacterized ATP-binding protein YghR EcoCyc product frame: G7550-MONOMER. Genomic coordinates: 3132454-3133212. EcoCyc protein note: No information about this protein was found by a literature search conducted on July 20, 2017.

## Biological Role

Repressed by leuO (protein.P10151).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64572|protein.P64572]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P10151|protein.P10151]] `RegulonDB` `S` - regulator=LeuO; target=yghR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009789,ECOCYC:G7550,GeneID:947310`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3132454-3133212:-; feature_type=gene
