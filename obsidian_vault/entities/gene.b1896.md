---
entity_id: "gene.b1896"
entity_type: "gene"
name: "otsA"
source_database: "NCBI RefSeq"
source_id: "gene-b1896"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1896"
  - "otsA"
---

# otsA

`gene.b1896`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1896`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

otsA (gene.b1896) is a gene entity. It encodes otsA (protein.P31677). Encoded protein function: FUNCTION: Catalyzes the transfer of glucose from UDP-alpha-D-glucose (UDP-Glc) to D-glucose 6-phosphate (Glc-6-P) to form trehalose-6-phosphate. Acts with retention of the anomeric configuration of the UDP-sugar donor. Essential for viability of the cells at low temperatures and at elevated osmotic strength. {ECO:0000269|PubMed:12105274, ECO:0000269|PubMed:1310094, ECO:0000269|PubMed:20077550, ECO:0000269|PubMed:3131312}. EcoCyc product frame: TREHALOSE6PSYN-MONOMER. Genomic coordinates: 1980188-1981612.

## Biological Role

Activated by rpoS (protein.P13445).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31677|protein.P31677]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=otsA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006318,ECOCYC:EG11751,GeneID:946405`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1980188-1981612:-; feature_type=gene
