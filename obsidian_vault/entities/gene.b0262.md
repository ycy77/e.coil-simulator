---
entity_id: "gene.b0262"
entity_type: "gene"
name: "afuC"
source_database: "NCBI RefSeq"
source_id: "gene-b0262"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0262"
  - "afuC"
---

# afuC

`gene.b0262`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0262`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

afuC (gene.b0262) is a gene entity. It encodes fbpC (protein.P37009). Encoded protein function: FUNCTION: Part of the ABC transporter complex FbpABC involved in Fe(3+) ions import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01706}. EcoCyc product frame: YAGC-MONOMER. EcoCyc synonyms: fbpC, yagC. Genomic coordinates: 277756-278802. EcoCyc protein note: AfuC is the ATP-binding component of a predicted ABC superfamily ferric cation transporter . afuBC is a remnant operon in E. coli K-12; a complete afuABC gene cluster is present in a wide range of bacteria and encodes a binding protein-dependent transport system initially implicated in Fe3+ uptake (afu: Actinobacillus ferric uptake) , but now believed to transport sugar phosphates . E. coli K-12 does not contain an afuA ortholog.

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37009|protein.P37009]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000898,ECOCYC:EG12340,GeneID:947676`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:277756-278802:-; feature_type=gene
