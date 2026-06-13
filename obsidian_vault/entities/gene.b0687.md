---
entity_id: "gene.b0687"
entity_type: "gene"
name: "seqA"
source_database: "NCBI RefSeq"
source_id: "gene-b0687"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0687"
  - "seqA"
---

# seqA

`gene.b0687`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0687`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

seqA (gene.b0687) is a gene entity. It encodes seqA (protein.P0AFY8). Encoded protein function: FUNCTION: Negative regulator of replication initiation, which contributes to regulation of DNA replication and ensures that replication initiation occurs exactly once per chromosome per cell cycle. Binds to pairs of hemimethylated GATC sequences in the oriC region, thus preventing assembly of replication proteins and re-initiation at newly replicated origins. Repression is relieved when the region becomes fully methylated. Can also bind to hemimethylated GATC sequences outside of oriC region. Binds, with less affinity, to fully methylated GATC sites and affects timing of replication. May play a role in chromosome organization and gene regulation. {ECO:0000255|HAMAP-Rule:MF_00908, ECO:0000269|PubMed:10931282, ECO:0000269|PubMed:11080170, ECO:0000269|PubMed:20689753, ECO:0000269|PubMed:7553853, ECO:0000269|PubMed:7891562, ECO:0000269|PubMed:8011018}. EcoCyc product frame: EG12197-MONOMER. EcoCyc synonyms: hsm-1. Genomic coordinates: 712987-713532. EcoCyc protein note: The SeqA protein is a negative modulator of the initiation of chromosome replication and is involved in sequestration of G0-10506 oriC, ensuring a single round of chromosome replication per cell cycle...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFY8|protein.P0AFY8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002343,ECOCYC:EG12197,GeneID:945272`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:712987-713532:+; feature_type=gene
