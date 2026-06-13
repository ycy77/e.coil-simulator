---
entity_id: "gene.b0495"
entity_type: "gene"
name: "ybbA"
source_database: "NCBI RefSeq"
source_id: "gene-b0495"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0495"
  - "ybbA"
---

# ybbA

`gene.b0495`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0495`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybbA (gene.b0495) is a gene entity. It encodes ybbA (protein.P0A9T8). Encoded protein function: Uncharacterized ABC transporter ATP-binding protein YbbA EcoCyc product frame: YBBA-MONOMER. Genomic coordinates: 519733-520419. EcoCyc protein note: YbbA is the predicted ATP-binding subunit of a putative ATP-binding cassette (ABC) exporter complex . YbbA contains sequence motifs conserved in ATP-binding cassette proteins . YbbA is upregulated in response to exogenous L-threonine; expression of ybbA from a multicopy plasmid increases the resistance of wild-type E. coli to high concentrations of L-threonine .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9T8|protein.P0A9T8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001717,ECOCYC:EG11657,GeneID:945122`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:519733-520419:+; feature_type=gene
