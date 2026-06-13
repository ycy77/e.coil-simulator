---
entity_id: "gene.b1486"
entity_type: "gene"
name: "ddpB"
source_database: "NCBI RefSeq"
source_id: "gene-b1486"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1486"
  - "ddpB"
---

# ddpB

`gene.b1486`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1486`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ddpB (gene.b1486) is a gene entity. It encodes ddpB (protein.P77308). Encoded protein function: FUNCTION: Part of the ABC transporter complex DdpABCDF, which is probably involved in D,D-dipeptide transport. Probably responsible for the translocation of the substrate across the membrane. EcoCyc product frame: YDDR-MONOMER. EcoCyc synonyms: yddR. Genomic coordinates: 1559907-1560929. EcoCyc protein note: DdpB is one of two predicted inner membrane subunits of a putative ATP-dependent D,D-dipeptide uptake system that may function to import D-alanyl-D-alanine for use as an energy source under starvation conditions . DdpB is predicted to be an inner membrane protein with 6 transmembrane domains; topology analysis suggests the C-terminus is located in the cytoplasm . ddp: D,D-dipeptide

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77308|protein.P77308]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004955,ECOCYC:G6780,GeneID:946044`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1559907-1560929:-; feature_type=gene
