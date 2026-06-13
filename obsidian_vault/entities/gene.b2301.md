---
entity_id: "gene.b2301"
entity_type: "gene"
name: "yfcF"
source_database: "NCBI RefSeq"
source_id: "gene-b2301"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2301"
  - "yfcF"
---

# yfcF

`gene.b2301`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2301`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfcF (gene.b2301) is a gene entity. It encodes yfcF (protein.P77544). Encoded protein function: FUNCTION: Exhibits glutathione (GSH) S-transferase activity toward 1-chloro-2,4-dinitrobenzene (CDNB); however this activity is as low as 1% of that of GstA. Also displays a GSH-dependent peroxidase activity toward cumene hydroperoxide. Is involved in defense against oxidative stress, probably via its peroxidase activity. {ECO:0000269|PubMed:17018556}. EcoCyc product frame: G7193-MONOMER. Genomic coordinates: 2419841-2420485.

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77544|protein.P77544]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007593,ECOCYC:G7193,GeneID:946749`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2419841-2420485:-; feature_type=gene
