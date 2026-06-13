---
entity_id: "gene.b0939"
entity_type: "gene"
name: "elfD"
source_database: "NCBI RefSeq"
source_id: "gene-b0939"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0939"
  - "elfD"
---

# elfD

`gene.b0939`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0939`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

elfD (gene.b0939) is a gene entity. It encodes elfD (protein.P75856). Encoded protein function: FUNCTION: Part of the elfADCG-ycbUVF fimbrial operon, which promotes adhesion of bacteria to different abiotic surfaces. Could be required for the biogenesis of the ElfA fimbriae. {ECO:0000269|PubMed:20345943}. EcoCyc product frame: G6481-MONOMER. EcoCyc synonyms: ycbR. Genomic coordinates: 998490-999191. EcoCyc protein note: ycbQRSTUVF is a putative chaperone-usher fimbrial operon in E. coli K-12 . The operon is cryptic under normal laboratory conditions but when constitutive expression is induced in a strain that lacks the type 1 fimbrial complex the ycb operon promotes biofilm formation in minimal media on a variety of abiotic surfaces and produces numerous surface fimbrial structures that can be observed microscopically . Expression of the ycb operon is regulated by the global regulators PD00288 "H-NS" and CPLX0-226 "CRP cAMP" . Deletion of each gene (with the exception of ycbF) in the 7 gene ycbQRSTUVF operon (in a K-12 BW25113 background) decreases invasion into a human ileocecal epithelial cell line compared to wild type . The ycbQRST gene cluster has been renamed elfADCG (E. coli YcbQ laminin-binding fimbriae) based on characterization in Shiga-toxigenic E...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75856|protein.P75856]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003187,ECOCYC:G6481,GeneID:946773`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:998490-999191:+; feature_type=gene
