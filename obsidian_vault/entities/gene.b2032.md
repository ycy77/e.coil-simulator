---
entity_id: "gene.b2032"
entity_type: "gene"
name: "wbbK"
source_database: "NCBI RefSeq"
source_id: "gene-b2032"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2032"
  - "wbbK"
---

# wbbK

`gene.b2032`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2032`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

wbbK (gene.b2032) is a gene entity. It encodes wbbK (protein.P37751). Encoded protein function: FUNCTION: May be a glycosyltransferase involved in the transfer of UDP-GalF and UDP-glucose. EcoCyc product frame: EG11985-MONOMER. EcoCyc synonyms: yefI. Genomic coordinates: 2103391-2104509. EcoCyc protein note: wbbK is predicted to encode a glycosyltransferase involved in the biosynthesis of O-antigen repeat units (see ). E. coli K-12 is phenotypically rough and does not express O-antigen due to mutations in the rfb region; E. coli K-12 MG1655 contains the rfb-50 mutation - an IS5 element which disrupts EG11986 wbbL encoding rhamnose transferase; an engineered strain of E. coli K-12 with all rfb genes intact synthesizes CPD0-2249 O16 antigen . For information on bacterial polysaccharide gene nomenclature see .

## Enriched Pathways

- `eco00542` O-Antigen repeat unit biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37751|protein.P37751]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006747,ECOCYC:EG11985,GeneID:946555`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2103391-2104509:-; feature_type=gene
