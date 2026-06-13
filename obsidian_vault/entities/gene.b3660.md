---
entity_id: "gene.b3660"
entity_type: "gene"
name: "yicL"
source_database: "NCBI RefSeq"
source_id: "gene-b3660"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3660"
  - "yicL"
---

# yicL

`gene.b3660`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3660`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yicL (gene.b3660) is a gene entity. It encodes yicL (protein.P31437). Encoded protein function: Uncharacterized inner membrane transporter YicL EcoCyc product frame: EG11688-MONOMER. Genomic coordinates: 3838248-3839171. EcoCyc protein note: YicL is an inner membrane protein with ten predicted transmembrane domains. The C terminus is located in the cytoplasm . Overexpression of YicL or the ORF296 protein from Glycine max (soybean) inhibits growth of E. coli and leads to slightly increased accumulation of 5-AMINO-LEVULINATE δ-aminolevulinic acid (ALA). The authors proposed that YicL may inhibit the biosynthesis of heme, possibly by inhibiting HemB . In the Transporter Classification Database E. coli YicL is a member of the Drug/Metabolite Transporter (DMT) superfamily .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31437|protein.P31437]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011962,ECOCYC:EG11688,GeneID:948176`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3838248-3839171:+; feature_type=gene
