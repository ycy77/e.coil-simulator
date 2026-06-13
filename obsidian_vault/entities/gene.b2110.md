---
entity_id: "gene.b2110"
entity_type: "gene"
name: "yehC"
source_database: "NCBI RefSeq"
source_id: "gene-b2110"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2110"
  - "yehC"
---

# yehC

`gene.b2110`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2110`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yehC (gene.b2110) is a gene entity. It encodes yehC (protein.P33342). Encoded protein function: FUNCTION: Part of the yehABCD fimbrial operon. Could contribute to adhesion to various surfaces in specific environmental niches. {ECO:0000269|PubMed:20345943}. EcoCyc product frame: EG11989-MONOMER. Genomic coordinates: 2190926-2191645. EcoCyc protein note: YehC is a putative fimbrial chaperone . yehDCBA is a putative chaperone-usher fimbrial operon in E.coli K-12 . The operon is cryptic under normal laboratory conditions but when constitutive expression is induced in a strain that lacks the type 1 fimbrial complex the yeh operon promotes biofilm formation in minimal media on a variety of abiotic surfaces . Expression of the yeh operon is regulated by the global regulators PD00288 "H-NS" and CPLX0-226 "CRP cAMP" . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including yehDCBA; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33342|protein.P33342]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006978,ECOCYC:EG11989,GeneID:946621`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2190926-2191645:-; feature_type=gene
