---
entity_id: "gene.b2643"
entity_type: "gene"
name: "lfgA"
source_database: "NCBI RefSeq"
source_id: "gene-b2643"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2643"
  - "lfgA"
---

# lfgA

`gene.b2643`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2643`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lfgA (gene.b2643) is a gene entity. It encodes yfjX (protein.P52139). Encoded protein function: Uncharacterized protein YfjX EcoCyc product frame: G7378-MONOMER. EcoCyc synonyms: yfjX. Genomic coordinates: 2775919-2776377. EcoCyc protein note: Excision of CP4-57 prophage which includes lfgABCDE operon (formerly the yfjXY ypjJ yfjZF operon) increases biofilm formation primarily early in biofilm development . Single-cell transcriptomic studies revealed that the lfgABCDE operon was transcribed when subjected to oxidative, acid and heat stress in wild-type strain BW25113 compared to an inactivated mqsRA mutant; the results are not detected in population studies. G7571-MONOMER MqsA binds to a putative palindromic sequence upstream of the operon repressing it's transcription. The G7379 protease but not LfgA prevents repression by MgsA under oxidative stress through degradation of MqsA . lfgA, less fatality gene A .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52139|protein.P52139]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008704,ECOCYC:G7378,GeneID:947126`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2775919-2776377:+; feature_type=gene
