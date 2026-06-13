---
entity_id: "gene.b3142"
entity_type: "gene"
name: "yraH"
source_database: "NCBI RefSeq"
source_id: "gene-b3142"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3142"
  - "yraH"
---

# yraH

`gene.b3142`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3142`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yraH (gene.b3142) is a gene entity. It encodes yraH (protein.P42913). Encoded protein function: FUNCTION: Part of the yraHIJK fimbrial operon. Could contribute to adhesion to various surfaces in specific environmental niches. Increases adhesion to eukaryotic T24 bladder epithelial cells in the absence of fim operon. {ECO:0000269|PubMed:20345943}. EcoCyc product frame: G7637-MONOMER. Genomic coordinates: 3287426-3288010. EcoCyc protein note: yraHIJK is a putative chaperone-usher fimbrial operon in E.coli K-12 . The operon is cryptic under normal laboratory conditions but when constitutive expression is induced in a strain that lacks the type 1 fimbrial complex the yra operon promotes adhesion to eukaryotic epithelial cells (T4 bladder cells) . Expression of the yra operon is regulated by the global regulators PD00288 "H-NS" and CPLX0-226 "CRP cAMP" . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including yraHIJK; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised .

## Biological Role

Repressed by hns (protein.P0ACF8), nac (protein.Q47005). Activated by CRP-cyclic-AMP DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-226).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P42913|protein.P42913]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.CPLX0-226|complex.ecocyc.CPLX0-226]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yraH; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010325,ECOCYC:G7637,GeneID:947658`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3287426-3288010:+; feature_type=gene
