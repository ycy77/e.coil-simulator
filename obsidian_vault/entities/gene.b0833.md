---
entity_id: "gene.b0833"
entity_type: "gene"
name: "pdeI"
source_database: "NCBI RefSeq"
source_id: "gene-b0833"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0833"
  - "pdeI"
---

# pdeI

`gene.b0833`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0833`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pdeI (gene.b0833) is a gene entity. It encodes pdeI (protein.P75800). Encoded protein function: FUNCTION: May act as a diguanylate cyclase (DGC) that catalyzes the synthesis of cyclic di-GMP (c-di-GMP) (PubMed:39689163). Probably functions as a membrane-associated sensor that integrates environmental signals with c-di-GMP production under complex regulatory mechanisms (PubMed:39689163). It increases c-di-GMP levels, promoting persister cell formation (PubMed:39689163). It is involved in biofilm formation, and may be especially crucial in the initial stages of biofilm formation, potentially responding to surface-associated cues to modulate c-di-GMP levels and promote attachment (PubMed:39689163). Overexpression reduces biofilm formation (PubMed:19460094). {ECO:0000269|PubMed:19460094, ECO:0000269|PubMed:39689163}. EcoCyc product frame: G6433-MONOMER. EcoCyc synonyms: yliE. Genomic coordinates: 872979-875327. EcoCyc protein note: PdeI was initially predicted to be a c-di-GMP-specific phosphodiesterase but has since been shown to increase c-di-GMP and referred to as a c-di-GMP synthase . Overexpression of pdeI reduces biofilm formation...

## Biological Role

Repressed by hns (protein.P0ACF8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75800|protein.P75800]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002839,ECOCYC:G6433,GeneID:945462`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:872979-875327:+; feature_type=gene
