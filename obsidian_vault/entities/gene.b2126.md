---
entity_id: "gene.b2126"
entity_type: "gene"
name: "btsS"
source_database: "NCBI RefSeq"
source_id: "gene-b2126"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2126"
  - "btsS"
---

# btsS

`gene.b2126`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2126`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

btsS (gene.b2126) is a gene entity. It encodes btsS (protein.P0AD14). Encoded protein function: FUNCTION: Member of the two-component regulatory system BtsS/BtsR, which is part of a nutrient-sensing regulatory network composed of BtsS/BtsR, the low-affinity pyruvate signaling system YpdA/YpdB and their respective target proteins, BtsT and YhjX. Responds to depletion of nutrients, specifically serine, and the concomitant presence of extracellular pyruvate. BtsS is a high-affinity receptor for extracellular pyruvate that activates BtsR by phosphorylation. Activation of the BtsS/BtsR signaling cascade also suppresses YpdA/YpdB-mediated yhjX induction. {ECO:0000269|PubMed:15522865, ECO:0000269|PubMed:22685278, ECO:0000269|PubMed:24659770, ECO:0000269|PubMed:28469239}. EcoCyc product frame: MONOMER0-4457. EcoCyc synonyms: yehU. Genomic coordinates: 2212959-2214644.

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD14|protein.P0AD14]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007027,ECOCYC:EG12007,GeneID:949027`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2212959-2214644:-; feature_type=gene
