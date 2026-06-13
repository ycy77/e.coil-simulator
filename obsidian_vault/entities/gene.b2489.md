---
entity_id: "gene.b2489"
entity_type: "gene"
name: "hyfI"
source_database: "NCBI RefSeq"
source_id: "gene-b2489"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2489"
  - "hyfI"
---

# hyfI

`gene.b2489`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2489`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hyfI (gene.b2489) is a gene entity. It encodes hyfI (protein.P77668). Encoded protein function: FUNCTION: Possible component of hydrogenase 4. {ECO:0000305|PubMed:9387241}. EcoCyc product frame: MONOMER0-151. Genomic coordinates: 2610706-2611464. EcoCyc protein note: hyfABCDEFGHI encodes a predicted nine subunit Ni-Fe hydrogenase complex (hydrogenase 4). HyfI resembles the small subunit (HycG) of hydrogenase 3 (63% sequence identity) and the NuoB subunit of NADH oxidoreductase (27% sequence identity); the protein contains a predicted [4Fe-4S] cluster (see also ).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77668|protein.P77668]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008198,ECOCYC:G7306,GeneID:946966`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2610706-2611464:+; feature_type=gene
