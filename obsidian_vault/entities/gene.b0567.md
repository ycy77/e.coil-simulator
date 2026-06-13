---
entity_id: "gene.b0567"
entity_type: "gene"
name: "ybcH"
source_database: "NCBI RefSeq"
source_id: "gene-b0567"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0567"
  - "ybcH"
---

# ybcH

`gene.b0567`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0567`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybcH (gene.b0567) is a gene entity. It encodes ybcH (protein.P37325). Encoded protein function: Uncharacterized protein YbcH EcoCyc product frame: EG12448-MONOMER. Genomic coordinates: 587091-587981. EcoCyc protein note: YbcH is predicted to be a periplasmic protein that is anchored to the inner membrane; the protein may be an auxiliary component of a secretion system for an uncharacteized exopolysaccharide that impedes flagellar activity and serves as the primary receptor for lytic bacteriophage N4 . ybcH is located together with EG11739 nfrB, encoding a C-DI-GMP-activated glycosyltransferase, and EG11740 nfrA encoding an outer membrane protein, and the three proteins likely constitute an exopolysaccharide production/secretion system .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37325|protein.P37325]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001937,ECOCYC:EG12448,GeneID:945186`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:587091-587981:-; feature_type=gene
