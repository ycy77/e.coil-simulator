---
entity_id: "gene.b2111"
entity_type: "gene"
name: "yehD"
source_database: "NCBI RefSeq"
source_id: "gene-b2111"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2111"
  - "yehD"
---

# yehD

`gene.b2111`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2111`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yehD (gene.b2111) is a gene entity. It encodes yehD (protein.P33343). Encoded protein function: FUNCTION: Part of the yehABCD fimbrial operon. Could contribute to adhesion to various surfaces in specific environmental niches. {ECO:0000269|PubMed:20345943}. EcoCyc product frame: EG11990-MONOMER. Genomic coordinates: 2191680-2192222. EcoCyc protein note: yehDCBA is a putative chaperone-usher fimbrial operon in E.coli K-12 . The operon is cryptic under normal laboratory conditions but when constitutive expression is induced in a strain that lacks the type 1 fimbrial complex the yeh operon promotes biofilm formation in minimal media on a variety of abiotic surfaces . Although no surface fimbrial structures could be observed microscopically the YehD protein was extracted and purifed from the surface protein mileau. Expression of the yeh operon is regulated by the global regulators PD00288 "H-NS" and CPLX0-226 "CRP cAMP" . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including yehDCBA; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised .

## Biological Role

Activated by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33343|protein.P33343]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yehD; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006980,ECOCYC:EG11990,GeneID:946619`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2191680-2192222:-; feature_type=gene
