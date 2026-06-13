---
entity_id: "gene.b1424"
entity_type: "gene"
name: "opgD"
source_database: "NCBI RefSeq"
source_id: "gene-b1424"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1424"
  - "opgD"
---

# opgD

`gene.b1424`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1424`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

opgD (gene.b1424) is a gene entity. It encodes mdoD (protein.P40120). Encoded protein function: FUNCTION: Probably involved in the control of the structural glucose backbone of osmoregulated periplasmic glucans (OPGs). EcoCyc product frame: EG12859-MONOMER. EcoCyc synonyms: yzzZ, ydcG, mdoD. Genomic coordinates: 1496856-1498511. EcoCyc protein note: The opgD gene was identified in silico as a paralog of EG11885 opgG . The protein was thought to be secreted to the periplasmic space via the twin-arginine translocation (Tat) pathway, but a tatC mutation does not affect its localization to the periplasmic space. OpgD thus can be exported by both the Tat and Sec pathways . A mutation in opgD does not cause gross changes in the synthesis or function of osmoregulated periplasmic glucans (OPGs), but alters the size of the glucose backbone of OPG molecules . opgD: osmoregulated periplasmic glucan mdoD: membrane derived oligosaccharide

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P40120|protein.P40120]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004754,ECOCYC:EG12859,GeneID:945994`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1496856-1498511:+; feature_type=gene
