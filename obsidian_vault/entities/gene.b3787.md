---
entity_id: "gene.b3787"
entity_type: "gene"
name: "wecC"
source_database: "NCBI RefSeq"
source_id: "gene-b3787"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3787"
  - "wecC"
---

# wecC

`gene.b3787`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3787`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

wecC (gene.b3787) is a gene entity. It encodes wecC (protein.P27829). Encoded protein function: FUNCTION: Catalyzes the four-electron oxidation of UDP-N-acetyl-D-mannosamine (UDP-ManNAc), reducing NAD(+) and releasing UDP-N-acetylmannosaminuronic acid (UDP-ManNAcA). {ECO:0000255|HAMAP-Rule:MF_02029, ECO:0000269|PubMed:381306}. EcoCyc product frame: UDPMANNACADEHYDROG-MONOMER. EcoCyc synonyms: rff, rffD, mnaB. Genomic coordinates: 3971260-3972522.

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27829|protein.P27829]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012374,ECOCYC:EG11452,GeneID:948977`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3971260-3972522:+; feature_type=gene
