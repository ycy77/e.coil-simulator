---
entity_id: "gene.b3862"
entity_type: "gene"
name: "yihG"
source_database: "NCBI RefSeq"
source_id: "gene-b3862"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3862"
  - "yihG"
---

# yihG

`gene.b3862`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3862`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yihG (gene.b3862) is a gene entity. It encodes yihG (protein.P32129). Encoded protein function: FUNCTION: Acyltransferase involved in the biosynthesis of membrane phospholipids (PubMed:32403425). It introduces a cis-vaccenoyl group (18:1) into the sn-2 position of phospholipids (PubMed:32403425). Overproduction of YihG facilitates the synthesis of phospholipids containing a myristoyl group (14:0) and a cis-vaccenoyl group at the sn-2 position, and a cis-vaccenoyl group at the sn-1 position (PubMed:32403425). May affect flagellar formation through modulation of the fatty acyl composition of membrane phospholipids (PubMed:32403425). {ECO:0000269|PubMed:32403425}. EcoCyc product frame: EG11833-MONOMER. Genomic coordinates: 4045670-4046602. EcoCyc protein note: yihG encodes a membrane-bound 1-acylglycerol-3-phosphate O-acyltransferase (also called lysophosphatidic acid acyltransferase or LPAAT for short) . Analysis of the phospholipid composition of cells overproducing YihG suggests that the enzyme facilitates synthesis of phospholipids containing cis-vaccenoyl (18:1) and myristoyl (14:0) at the sn-2 position and preferably introduces these groups into lysophospholipids containing cis-vaccenoyl (18:1) at the sn-1 position...

## Biological Role

Activated by rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32129|protein.P32129]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=yihG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012611,ECOCYC:EG11833,GeneID:948350`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4045670-4046602:-; feature_type=gene
