---
entity_id: "gene.b0364"
entity_type: "gene"
name: "yaiS"
source_database: "NCBI RefSeq"
source_id: "gene-b0364"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0364"
  - "yaiS"
---

# yaiS

`gene.b0364`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0364`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yaiS (gene.b0364) is a gene entity. It encodes yaiS (protein.P71311). Encoded protein function: Uncharacterized deacetylase YaiS (EC 3.-.-.-) EcoCyc product frame: G6216-MONOMER. Genomic coordinates: 384059-384616. EcoCyc protein note: No information about this protein was found by a literature search conducted on May 7, 2018.

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P71311|protein.P71311]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yaiS; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001249,ECOCYC:G6216,GeneID:946967`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:384059-384616:-; feature_type=gene
