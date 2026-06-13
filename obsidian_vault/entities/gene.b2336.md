---
entity_id: "gene.b2336"
entity_type: "gene"
name: "yfcS"
source_database: "NCBI RefSeq"
source_id: "gene-b2336"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2336"
  - "yfcS"
---

# yfcS

`gene.b2336`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2336`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfcS (gene.b2336) is a gene entity. It encodes yfcS (protein.P77599). Encoded protein function: FUNCTION: Part of the yfcOPQRSUV fimbrial operon. Could contribute to adhesion to various surfaces in specific environmental niches. Increases adhesion to eukaryotic T24 bladder epithelial cells in the absence of fim genes. {ECO:0000269|PubMed:20345943}. EcoCyc product frame: G7207-MONOMER. Genomic coordinates: 2451584-2452336. EcoCyc protein note: yfcOPQRSTUV is a putative chaperone-usher fimbrial operon; yfcS is predicted to encode a fimbrial chaperone . The operon is cryptic under normal laboratory conditions but when constitutive expression is induced in a strain that lacks the type 1 fimbrial complex the yfc operon promotes adhesion to eukaryotic epithelial cells (T4 bladder cells) . Expression of the yfc operon is regulated by the global regulators PD00288 "H-NS" and CPLX0-226 "CRP cAMP" . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including yfcOPQRSTUV; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77599|protein.P77599]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007709,ECOCYC:G7207,GeneID:946418`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2451584-2452336:-; feature_type=gene
