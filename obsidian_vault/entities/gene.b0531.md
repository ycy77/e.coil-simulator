---
entity_id: "gene.b0531"
entity_type: "gene"
name: "sfmC"
source_database: "NCBI RefSeq"
source_id: "gene-b0531"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0531"
  - "sfmC"
---

# sfmC

`gene.b0531`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0531`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sfmC (gene.b0531) is a gene entity. It encodes sfmC (protein.P77249). Encoded protein function: FUNCTION: Part of the sfmACDHF fimbrial operon. Could contribute to adhesion to various surfaces in specific environmental niches. Increases adhesion to eukaryotic T24 bladder epithelial cells in the absence of fim genes. {ECO:0000269|PubMed:20345943}. EcoCyc product frame: G6291-MONOMER. Genomic coordinates: 558974-559666. EcoCyc protein note: sfmACDHF is a putative chaperone-usher fimbrial operon in E.coli K-12 . The operon is cryptic under normal laboratory conditions but when constitutive expression is induced in a strain that lacks the type 1 fimbrial complex the sfm operon promotes adhesion to eukaryotic epithelial cells (T4 bladder cells) . Expression of the sfm operon is regulated by the global regulators PD00288 "H-NS" and CPLX0-226 "CRP cAMP" and by the transcription factor EG11103-MONOMER FimZ . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including sfmACDHF; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77249|protein.P77249]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001828,ECOCYC:G6291,GeneID:945367`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:558974-559666:+; feature_type=gene
