---
entity_id: "gene.b0652"
entity_type: "gene"
name: "gltL"
source_database: "NCBI RefSeq"
source_id: "gene-b0652"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0652"
  - "gltL"
---

# gltL

`gene.b0652`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0652`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gltL (gene.b0652) is a gene entity. It encodes gltL (protein.P0AAG3). Encoded protein function: FUNCTION: Part of the ABC transporter complex GltIJKL involved in glutamate and aspartate uptake. Probably responsible for energy coupling to the transport system. {ECO:0000305|PubMed:9593292}. EcoCyc product frame: GLTL-MONOMER. Genomic coordinates: 684530-685255. EcoCyc protein note: GltL is the predicted ATP binding subunit of a glutamate/aspartate ABC transporter complex; GltL contains signature motifs conserved in ATP-binding cassette (ABC) proteins .

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAG3|protein.P0AAG3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002232,ECOCYC:EG12663,GeneID:945254`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:684530-685255:-; feature_type=gene
