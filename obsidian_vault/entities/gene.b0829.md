---
entity_id: "gene.b0829"
entity_type: "gene"
name: "gsiA"
source_database: "NCBI RefSeq"
source_id: "gene-b0829"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0829"
  - "gsiA"
---

# gsiA

`gene.b0829`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0829`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gsiA (gene.b0829) is a gene entity. It encodes gsiA (protein.P75796). Encoded protein function: FUNCTION: Part of the ABC transporter complex GsiABCD involved in glutathione import. Responsible for energy coupling to the transport system. {ECO:0000269|PubMed:16109926}. EcoCyc product frame: YLIA-MONOMER. EcoCyc synonyms: yliA. Genomic coordinates: 867520-869391. EcoCyc protein note: GsiA is the predicted ATP binding subunit of a glutathione ABC importer; GsiA contains an ABC-ABC domain

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75796|protein.P75796]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002830,ECOCYC:G6429,GeneID:945457`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:867520-869391:+; feature_type=gene
