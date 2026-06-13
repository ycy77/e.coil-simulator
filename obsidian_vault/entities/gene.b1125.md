---
entity_id: "gene.b1125"
entity_type: "gene"
name: "potB"
source_database: "NCBI RefSeq"
source_id: "gene-b1125"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1125"
  - "potB"
---

# potB

`gene.b1125`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1125`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

potB (gene.b1125) is a gene entity. It encodes potB (protein.P0AFK4). Encoded protein function: FUNCTION: Required for the activity of the bacterial periplasmic transport system of putrescine and spermidine. EcoCyc product frame: POTB-MONOMER. Genomic coordinates: 1183617-1184444. EcoCyc protein note: potB encodes one of two integral membrane subunits of an ATP-dependent spermidine uptake system; PotB is predicted to contain 6 transmembrane regions . An alternative translation initiation codon 27 nt upstream of the annotated translation initiation site appears to be used .

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFK4|protein.P0AFK4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003794,ECOCYC:EG10750,GeneID:945692`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1183617-1184444:-; feature_type=gene
