---
entity_id: "gene.b3143"
entity_type: "gene"
name: "yraI"
source_database: "NCBI RefSeq"
source_id: "gene-b3143"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3143"
  - "yraI"
---

# yraI

`gene.b3143`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3143`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yraI (gene.b3143) is a gene entity. It encodes yraI (protein.P42914). Encoded protein function: FUNCTION: Part of the yraHIJK fimbrial operon. Could contribute to adhesion to various surfaces in specific environmental niches. Increases adhesion to eukaryotic T24 bladder epithelial cells in the absence of fim operon. {ECO:0000269|PubMed:20345943}. EcoCyc product frame: G7638-MONOMER. Genomic coordinates: 3288090-3288785. EcoCyc protein note: yraHIJK is a putative chaperone-usher fimbrial operon in E.coli K-12 . The operon is cryptic under normal laboratory conditions but when constitutive expression is induced in a strain that lacks the type 1 fimbrial complex the yra operon promotes adhesion to eukaryotic epithelial cells (T4 bladder cells) . Expression of the yra operon is regulated by the global regulators PD00288 "H-NS" and CPLX0-226 "CRP cAMP" . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including yraHIJK; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised .

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P42914|protein.P42914]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010331,ECOCYC:G7638,GeneID:947657`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3288090-3288785:+; feature_type=gene
