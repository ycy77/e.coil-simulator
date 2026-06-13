---
entity_id: "gene.b1953"
entity_type: "gene"
name: "yodD"
source_database: "NCBI RefSeq"
source_id: "gene-b1953"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1953"
  - "yodD"
---

# yodD

`gene.b1953`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1953`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yodD (gene.b1953) is a gene entity. It encodes yodD (protein.P64519). Encoded protein function: Uncharacterized protein YodD EcoCyc product frame: G7046-MONOMER. Genomic coordinates: 2024986-2025213. EcoCyc protein note: YodD is involved in the cellular response to hydrogen peroxide and acid stress . A yodD mutant is much more sensitive to hydrogen peroxide and acid stress than wild type and shows somewhat increased biofilm formation. In a metabolically engineered strain that expresses genes required for the degradation of cis-dichloroethylene (cis-DCE), yodD expression is induced .

## Biological Role

Activated by DNA-binding transcriptional dual regulator Fis (complex.ecocyc.CPLX0-7705).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64519|protein.P64519]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[complex.ecocyc.CPLX0-7705|complex.ecocyc.CPLX0-7705]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006488,ECOCYC:G7046,GeneID:946469`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2024986-2025213:+; feature_type=gene
