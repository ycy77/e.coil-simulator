---
entity_id: "gene.b3723"
entity_type: "gene"
name: "bglG"
source_database: "NCBI RefSeq"
source_id: "gene-b3723"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3723"
  - "bglG"
---

# bglG

`gene.b3723`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3723`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bglG (gene.b3723) is a gene entity. It encodes bglG (protein.P11989). Encoded protein function: FUNCTION: Mediates the positive regulation of the beta-glucoside (bgl) operon by functioning as a transcriptional antiterminator. This is an RNA-binding protein that recognizes a specific sequence located just upstream of two termination sites within the operon. EcoCyc product frame: EG10116-MONOMER. EcoCyc synonyms: bglC. Genomic coordinates: 3905731-3906567.

## Biological Role

Repressed by fis (protein.P0A6R3), hns (protein.P0ACF8). Activated by crp (protein.P0ACJ8), leuO (protein.P10151).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P11989|protein.P11989]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=bglG; function=+
- `activates` <-- [[protein.P10151|protein.P10151]] `RegulonDB` `S` - regulator=LeuO; target=bglG; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=bglG; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=bglG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012174,ECOCYC:EG10116,GeneID:948235`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3905731-3906567:-; feature_type=gene
