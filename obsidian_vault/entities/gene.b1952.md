---
entity_id: "gene.b1952"
entity_type: "gene"
name: "dsrB"
source_database: "NCBI RefSeq"
source_id: "gene-b1952"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1952"
  - "dsrB"
---

# dsrB

`gene.b1952`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1952`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dsrB (gene.b1952) is a gene entity. It encodes dsrB (protein.P0AEG8). Encoded protein function: Protein DsrB EcoCyc product frame: G7045-MONOMER. Genomic coordinates: 2024635-2024823. EcoCyc protein note: Expression of dsrB is RpoS-dependent, although the effect is not at the level of transcription initiation . DsrB: "downstream (from rcsA) region B"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEG8|protein.P0AEG8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006484,ECOCYC:G7045,GeneID:946468`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2024635-2024823:-; feature_type=gene
