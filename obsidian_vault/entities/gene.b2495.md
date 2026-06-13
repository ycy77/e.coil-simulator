---
entity_id: "gene.b2495"
entity_type: "gene"
name: "yfgD"
source_database: "NCBI RefSeq"
source_id: "gene-b2495"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2495"
  - "yfgD"
---

# yfgD

`gene.b2495`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2495`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfgD (gene.b2495) is a gene entity. It encodes yfgD (protein.P76569). Encoded protein function: Uncharacterized protein YfgD EcoCyc product frame: G7312-MONOMER. Genomic coordinates: 2617578-2617937. EcoCyc protein note: No information about this protein was found by a literature search conducted on March 20, 2017.

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76569|protein.P76569]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=yfgD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008214,ECOCYC:G7312,GeneID:946974`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2617578-2617937:+; feature_type=gene
