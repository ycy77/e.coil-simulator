---
entity_id: "gene.b1484"
entity_type: "gene"
name: "ddpD"
source_database: "NCBI RefSeq"
source_id: "gene-b1484"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1484"
  - "ddpD"
---

# ddpD

`gene.b1484`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1484`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ddpD (gene.b1484) is a gene entity. It encodes ddpD (protein.P77268). Encoded protein function: FUNCTION: Part of the ABC transporter complex DdpABCDF, which is probably involved in D,D-dipeptide transport (PubMed:9097039). Probably responsible for energy coupling to the transport system. {ECO:0000305|PubMed:9097039}. EcoCyc product frame: YDDP-MONOMER. EcoCyc synonyms: yddP. Genomic coordinates: 1558031-1559017. EcoCyc protein note: DdpD is one of two predicted ATP-binding subunits of a D,D-dipeptide uptake system that may function to import D-alanyl-D-alanine for use as an energy source under starvation conditions . ddp: D,D-dipeptide

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77268|protein.P77268]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004949,ECOCYC:G6778,GeneID:946002`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1558031-1559017:-; feature_type=gene
