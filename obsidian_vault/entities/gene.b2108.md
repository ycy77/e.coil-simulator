---
entity_id: "gene.b2108"
entity_type: "gene"
name: "yehA"
source_database: "NCBI RefSeq"
source_id: "gene-b2108"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2108"
  - "yehA"
---

# yehA

`gene.b2108`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2108`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yehA (gene.b2108) is a gene entity. It encodes yehA (protein.P33340). Encoded protein function: FUNCTION: Part of the yehABCD fimbrial operon. Could contribute to adhesion to various surfaces in specific environmental niches. {ECO:0000269|PubMed:20345943}. EcoCyc product frame: EG11987-MONOMER. Genomic coordinates: 2187380-2188414. EcoCyc protein note: yehDCBA is a putative chaperone-usher fimbrial operon in E.coli K-12 . The operon is cryptic under normal laboratory conditions but when constitutive expression is induced in a strain that lacks the type 1 fimbrial complex the yeh operon promotes biofilm formation in minimal media on a variety of abiotic surfaces . Expression of the yeh operon is regulated by the global regulators PD00288 "H-NS" and CPLX0-226 "CRP cAMP" . YehA shares a low sequence similarity to members of the Autotransporter (AT) Family . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including yehDCBA; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33340|protein.P33340]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006972,ECOCYC:EG11987,GeneID:946642`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2187380-2188414:-; feature_type=gene
