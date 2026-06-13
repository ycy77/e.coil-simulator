---
entity_id: "gene.b2333"
entity_type: "gene"
name: "yfcP"
source_database: "NCBI RefSeq"
source_id: "gene-b2333"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2333"
  - "yfcP"
---

# yfcP

`gene.b2333`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2333`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfcP (gene.b2333) is a gene entity. It encodes yfcP (protein.P76499). Encoded protein function: FUNCTION: Part of the yfcOPQRSUV fimbrial operon. Could contribute to adhesion to various surfaces in specific environmental niches. Increases adhesion to eukaryotic T24 bladder epithelial cells in the absence of fim genes. {ECO:0000269|PubMed:20345943}. EcoCyc product frame: G7204-MONOMER. Genomic coordinates: 2450051-2450590. EcoCyc protein note: yfcOPQRSTUV is a putative chaperone-usher fimbrial operon . The operon is cryptic under normal laboratory conditions but when constitutive expression is induced in a strain that lacks the type 1 fimbrial complex the yfc operon promotes adhesion to eukaryotic epithelial cells (T4 bladder cells) . Expression of the yfc operon is regulated by the global regulators PD00288 "H-NS" and CPLX0-226 "CRP cAMP" . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including yfcOPQRSTUV; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76499|protein.P76499]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yfcP; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007702,ECOCYC:G7204,GeneID:946788`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2450051-2450590:-; feature_type=gene
