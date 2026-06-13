---
entity_id: "gene.b3145"
entity_type: "gene"
name: "yraK"
source_database: "NCBI RefSeq"
source_id: "gene-b3145"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3145"
  - "yraK"
---

# yraK

`gene.b3145`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3145`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yraK (gene.b3145) is a gene entity. It encodes yraK (protein.P43319). Encoded protein function: FUNCTION: Part of the yraHIJK fimbrial operon. Could contribute to adhesion to various surfaces in specific environmental niches. Increases adhesion to eukaryotic T24 bladder epithelial cells in the absence of fim operon. {ECO:0000269|PubMed:20345943}. EcoCyc product frame: G7640-MONOMER. Genomic coordinates: 3291341-3292432. EcoCyc protein note: yraHIJK is a putative chaperone-usher fimbrial operon in E.coli K-12 . The operon is cryptic under normal laboratory conditions but when constitutive expression is induced in a strain that lacks the type 1 fimbrial complex the yra operon promotes adhesion to eukaryotic epithelial cells (T4 bladder cells) . Expression of the yra operon is regulated by the global regulators PD00288 "H-NS" and CPLX0-226 "CRP cAMP" . Sequence similarity suggests that YraK may contain β-barrel structure(s) . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including yraHIJK; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P43319|protein.P43319]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010335,ECOCYC:G7640,GeneID:947654`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3291341-3292432:+; feature_type=gene
