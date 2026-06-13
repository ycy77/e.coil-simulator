---
entity_id: "gene.b0938"
entity_type: "gene"
name: "elfA"
source_database: "NCBI RefSeq"
source_id: "gene-b0938"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0938"
  - "elfA"
---

# elfA

`gene.b0938`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0938`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

elfA (gene.b0938) is a gene entity. It encodes elfA (protein.P75855). Encoded protein function: FUNCTION: Part of the elfADCG-ycbUVF fimbrial operon, which promotes adhesion of bacteria to different abiotic surfaces. ElfA is the major fimbrial subunit produced by this operon. {ECO:0000269|PubMed:20345943}. EcoCyc product frame: G6480-MONOMER. EcoCyc synonyms: ycbQ. Genomic coordinates: 997868-998407. EcoCyc protein note: ycbQRSTUVF is a putative chaperone-usher fimbrial operon in E.coli K-12 . The operon is cryptic under normal laboratory conditions but when constitutive expression is induced in a strain that lacks the type 1 fimbrial complex the ycb operon promotes biofilm formation in minimal media on a variety of abiotic surfaces and produces numerous surface fimbrial structures that can be observed microscopically . Extraction and purification of these fimbriae revealed the presence of the YcbQ protein . Expression of the ycb operon is regulated by the global regulators PD00288 "H-NS" and CPLX0-226 "CRP cAMP" . Deletion of each gene (with the exception of ycbF) in the 7 gene ycbQRSTUVF operon (in a K-12 BW25113 background) decreases invasion into a human ileocecal epithelial cell line compared to wild type...

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by CRP-cyclic-AMP DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-226), slyA (protein.P0A8W2), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75855|protein.P75855]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[complex.ecocyc.CPLX0-226|complex.ecocyc.CPLX0-226]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=elfA; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=elfA; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003185,ECOCYC:G6480,GeneID:948306`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:997868-998407:+; feature_type=gene
