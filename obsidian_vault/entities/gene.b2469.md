---
entity_id: "gene.b2469"
entity_type: "gene"
name: "narQ"
source_database: "NCBI RefSeq"
source_id: "gene-b2469"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2469"
  - "narQ"
---

# narQ

`gene.b2469`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2469`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

narQ (gene.b2469) is a gene entity. It encodes narQ (protein.P27896). Encoded protein function: FUNCTION: Acts as a sensor for nitrate/nitrite and transduces signal of nitrate/nitrite availability to the NarL/NarP proteins. NarQ probably activates NarL and NarP by phosphorylation. NarQ probably negatively regulates the NarL protein by dephosphorylation. EcoCyc product frame: NARQ-MONOMER. Genomic coordinates: 2585731-2587431.

## Biological Role

Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27896|protein.P27896]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008132,ECOCYC:EG11460,GeneID:946948`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2585731-2587431:+; feature_type=gene
