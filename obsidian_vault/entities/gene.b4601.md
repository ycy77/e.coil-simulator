---
entity_id: "gene.b4601"
entity_type: "gene"
name: "ydgU"
source_database: "NCBI RefSeq"
source_id: "gene-b4601"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4601"
  - "ydgU"
---

# ydgU

`gene.b4601`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4601`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydgU (gene.b4601) is a gene entity. It encodes ydgU (protein.A5A617). Encoded protein function: Uncharacterized protein YdgU EcoCyc product frame: MONOMER0-2821. Genomic coordinates: 1671777-1671860. EcoCyc protein note: The YdgU open reading frame was predicted based on the presence of a ribosome binding site in an intergenic region. YdgU contains a predicted transmembrane segment. YdgU is expressed during stationary phase . ydgU was in the top 20 genes with increased translation in response to extreme acid stress (pH 4.4 compared to pH 7.6) as measured by ribosome coverage of its transcripts using RNA-Seq .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.A5A617|protein.A5A617]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0285184,ECOCYC:G0-10593,GeneID:5061510`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1671777-1671860:+; feature_type=gene
