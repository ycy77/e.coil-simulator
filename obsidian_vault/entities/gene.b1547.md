---
entity_id: "gene.b1547"
entity_type: "gene"
name: "stfQ"
source_database: "NCBI RefSeq"
source_id: "gene-b1547"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1547"
  - "stfQ"
---

# stfQ

`gene.b1547`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1547`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

stfQ (gene.b1547) is a gene entity. It encodes stfQ (protein.P77515). Encoded protein function: Prophage side tail fiber protein homolog StfQ (Side tail fiber protein homolog from lambdoid prophage Qin) EcoCyc product frame: G6821-MONOMER. EcoCyc synonyms: ydfN. Genomic coordinates: 1634885-1635847. EcoCyc protein note: No information about this protein was found by a literature search conducted on August 26, 2019.

## Biological Role

Repressed by fur (protein.P0A9A9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77515|protein.P77515]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=stfQ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005168,ECOCYC:G6821,GeneID:946098`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1634885-1635847:-; feature_type=gene
