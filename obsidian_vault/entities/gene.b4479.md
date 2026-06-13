---
entity_id: "gene.b4479"
entity_type: "gene"
name: "dgoR"
source_database: "NCBI RefSeq"
source_id: "gene-b4479"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4479"
  - "dgoR"
---

# dgoR

`gene.b4479`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4479`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dgoR (gene.b4479) is a gene entity. It encodes dgoR (protein.P31460). Encoded protein function: FUNCTION: Involved in the regulation of D-galactonate metabolism (PubMed:211976, PubMed:30455279). Represses the expression of the dgoRKADT operon by binding to two closely spaced inverted repeats in the cis-acting element, which overlap with the D-galactonate responsive dgo promoter (PubMed:30455279). Employs a derepression mechanism using D-galactonate as a specific effector molecule (PubMed:30455279, PubMed:33068046, PubMed:33224125). {ECO:0000269|PubMed:211976, ECO:0000269|PubMed:30455279, ECO:0000269|PubMed:33068046, ECO:0000269|PubMed:33224125}. EcoCyc product frame: G7790-MONOMER. EcoCyc synonyms: yidW, b3695, b3694. Genomic coordinates: 3874471-3875160.

## Biological Role

Repressed by dgoR (protein.P31460). Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31460|protein.P31460]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=dgoR; function=+
- `represses` <-- [[protein.P31460|protein.P31460]] `RegulonDB` `C` - regulator=DgoR; target=dgoR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0174108,ECOCYC:G7789,GeneID:2847767`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3874471-3875160:-; feature_type=gene
