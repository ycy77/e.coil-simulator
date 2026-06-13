---
entity_id: "gene.b0533"
entity_type: "gene"
name: "sfmH"
source_database: "NCBI RefSeq"
source_id: "gene-b0533"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0533"
  - "sfmH"
---

# sfmH

`gene.b0533`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0533`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sfmH (gene.b0533) is a gene entity. It encodes sfmH (protein.P75715). Encoded protein function: FUNCTION: Part of the sfmACDHF fimbrial operon. Could contribute to adhesion to various surfaces in specific environmental niches. Increases adhesion to eukaryotic T24 bladder epithelial cells in the absence of fim genes. {ECO:0000269|PubMed:20345943}. EcoCyc product frame: G6293-MONOMER. Genomic coordinates: 562336-563319. EcoCyc protein note: sfmACDHF is a putative chaperone-usher fimbrial operon in E. coli K-12 . The operon is cryptic under normal laboratory conditions but when constitutive expression is induced in a strain that lacks the type 1 fimbrial complex the sfm operon promotes adhesion to eukaryotic epithelial cells (T4 bladder cells) . Expression of the sfm operon is regulated by the global regulators PD00288 "H-NS" and CPLX0-226 "CRP cAMP" and by the transcription factor EG11103-MONOMER FimZ . SfmH is expressed by Escherichia coli O157 during human infection . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including sfmACDHF; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75715|protein.P75715]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001832,ECOCYC:G6293,GeneID:945407`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:562336-563319:+; feature_type=gene
