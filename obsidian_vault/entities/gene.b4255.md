---
entity_id: "gene.b4255"
entity_type: "gene"
name: "rraB"
source_database: "NCBI RefSeq"
source_id: "gene-b4255"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4255"
  - "rraB"
---

# rraB

`gene.b4255`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4255`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rraB (gene.b4255) is a gene entity. It encodes rraB (protein.P0AF90). Encoded protein function: FUNCTION: Globally modulates RNA abundance by binding to RNase E (Rne) and regulating its endonucleolytic activity. Can modulate Rne action in a substrate-dependent manner by altering the composition of the degradosome. {ECO:0000255|HAMAP-Rule:MF_01888, ECO:0000269|PubMed:16771842, ECO:0000269|PubMed:18510556}. EcoCyc product frame: G7885-MONOMER. EcoCyc synonyms: yjgD. Genomic coordinates: 4478473-4478889.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF90|protein.P0AF90]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rraB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013936,ECOCYC:G7885,GeneID:948773`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4478473-4478889:+; feature_type=gene
