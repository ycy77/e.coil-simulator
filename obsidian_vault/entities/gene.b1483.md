---
entity_id: "gene.b1483"
entity_type: "gene"
name: "ddpF"
source_database: "NCBI RefSeq"
source_id: "gene-b1483"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1483"
  - "ddpF"
---

# ddpF

`gene.b1483`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1483`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ddpF (gene.b1483) is a gene entity. It encodes ddpF (protein.P77622). Encoded protein function: FUNCTION: Part of the ABC transporter complex DdpABCDF, which is probably involved in D,D-dipeptide transport (PubMed:9097039). Probably responsible for energy coupling to the transport system. {ECO:0000305|PubMed:9097039}. EcoCyc product frame: YDDO-MONOMER. EcoCyc synonyms: yddO. Genomic coordinates: 1557112-1558038. EcoCyc protein note: DdpF is one of two predicted ATP-binding subunits of a D,D-dipeptide uptake system that may function to import D-alanyl-D-alanine for use as an energy source under starvation conditions . ddp: D,D-dipeptide

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77622|protein.P77622]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004947,ECOCYC:G6777,GeneID:946020`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1557112-1558038:-; feature_type=gene
