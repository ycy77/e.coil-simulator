---
entity_id: "gene.b2164"
entity_type: "gene"
name: "psuT"
source_database: "NCBI RefSeq"
source_id: "gene-b2164"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2164"
  - "psuT"
---

# psuT

`gene.b2164`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2164`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

psuT (gene.b2164) is a gene entity. It encodes psuT (protein.P33024). Encoded protein function: FUNCTION: Could be involved in pseudouridine transport. EcoCyc product frame: YEIM-MONOMER. EcoCyc synonyms: pscT, yeiM. Genomic coordinates: 2256085-2257335. EcoCyc protein note: PsuT is a member of the Concentrative Nucleoside Transport (CNT) family and is a predicted pseudouridine transport protein in E. coli K-12. psuT is located directly downstream from psuG and psuK which encode proteins involved in pseudouridine degradation. These proteins have been experimentally characterised in uropathogenic E. coli . Additionally pyrimidine auxotrophs of E. coli strains B and W are able to grow with pseudouridine as a sole pyrimidine source . The three proteins have not been characterised in E. coli K-12.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33024|protein.P33024]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007163,ECOCYC:EG12032,GeneID:946671`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2256085-2257335:-; feature_type=gene
