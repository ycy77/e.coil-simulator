---
entity_id: "gene.b0943"
entity_type: "gene"
name: "ycbV"
source_database: "NCBI RefSeq"
source_id: "gene-b0943"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0943"
  - "ycbV"
---

# ycbV

`gene.b0943`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0943`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycbV (gene.b0943) is a gene entity. It encodes ycbV (protein.P75860). Encoded protein function: FUNCTION: Part of the elfADCG-ycbUVF fimbrial operon, which promotes adhesion of bacteria to different abiotic surfaces. {ECO:0000269|PubMed:20345943}. EcoCyc product frame: G6485-MONOMER. Genomic coordinates: 1003439-1003954. EcoCyc protein note: ycbQRSTUVF is a putative chaperone-usher fimbrial operon in E.coli K-12 . The operon is cryptic under normal laboratory conditions but when constitutive expression is induced in a strain that lacks the type 1 fimbrial complex the ycb operon promotes biofilm formation in minimal media on a variety of abiotic surfaces and produces numerous surface fimbrial structures that can be observed microscopically . Expression of the ycb operon is regulated by the global regulators PD00288 "H-NS" and CPLX0-226 "CRP cAMP" . Deletion of each gene (with the exception of ycbF) in the 7 gene ycbQRSTUVF operon (in a K-12 BW25113 background) decreases invasion into a human ileocecal epithelial cell line compared to wild type . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including ycbQRSTUVF; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised .

## Biological Role

Repressed by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75860|protein.P75860]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ycbV; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003195,ECOCYC:G6485,GeneID:945562`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1003439-1003954:+; feature_type=gene
