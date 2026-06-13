---
entity_id: "gene.b0530"
entity_type: "gene"
name: "sfmA"
source_database: "NCBI RefSeq"
source_id: "gene-b0530"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0530"
  - "sfmA"
---

# sfmA

`gene.b0530`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0530`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sfmA (gene.b0530) is a gene entity. It encodes sfmA (protein.P0ABW5). Encoded protein function: FUNCTION: Part of the sfmACDHF fimbrial operon. Could contribute to adhesion to various surfaces in specific environmental niches. Increases adhesion to eukaryotic T24 bladder epithelial cells in the absence of fim genes. {ECO:0000269|PubMed:20345943}. EcoCyc product frame: G6290-MONOMER. Genomic coordinates: 558212-558754. EcoCyc protein note: sfmACDHF is a putative chaperone-usher fimbrial operon in E.coli K-12 . The operon is cryptic under normal laboratory conditions but when constitutive expression is induced in a strain that lacks the type 1 fimbrial complex the sfm operon promotes adhesion to eukaryotic epithelial cells (T4 bladder cells) . Expression of the sfm operon is regulated by the global regulators PD00288 "H-NS" and CPLX0-226 "CRP cAMP" and by the transcription factor EG11103-MONOMER FimZ . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including sfmACDHF; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised .

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by CRP-cyclic-AMP DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-226).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABW5|protein.P0ABW5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-226|complex.ecocyc.CPLX0-226]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001825,ECOCYC:G6290,GeneID:945522`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:558212-558754:+; feature_type=gene
