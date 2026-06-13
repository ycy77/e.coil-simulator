---
entity_id: "gene.b0941"
entity_type: "gene"
name: "elfG"
source_database: "NCBI RefSeq"
source_id: "gene-b0941"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0941"
  - "elfG"
---

# elfG

`gene.b0941`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0941`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

elfG (gene.b0941) is a gene entity. It encodes elfG (protein.P75858). Encoded protein function: FUNCTION: Part of the elfADCG-ycbUVF fimbrial operon, which promotes adhesion of bacteria to different abiotic surfaces. {ECO:0000269|PubMed:20345943}. EcoCyc product frame: G6483-MONOMER. EcoCyc synonyms: ycbT. Genomic coordinates: 1001807-1002877. EcoCyc protein note: ycbQRSTUVF is a putative chaperone-usher fimbrial operon in E.coli K-12 . The operon is cryptic under normal laboratory conditions but when constitutive expression is induced in a strain that lacks the type 1 fimbrial complex the ycb operon promotes biofilm formation in minimal media on a variety of abiotic surfaces and produces numerous surface fimbrial structures that can be observed microscopically . Expression of the ycb operon is regulated by the global regulators PD00288 "H-NS" and CPLX0-226 "CRP cAMP" . Deletion of each gene (with the exception of ycbF) in the 7 gene ycbQRSTUVF operon (in a K-12 BW25113 background) decreases invasion into a human ileocecal epithelial cell line compared to wild type . The ycbQRST gene cluster has been renamed elfADCG (E. coli YcbQ laminin-binding fimbriae) based on characterization in Shiga-toxigenic E...

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75858|protein.P75858]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=elfG; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003191,ECOCYC:G6483,GeneID:947185`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1001807-1002877:+; feature_type=gene
