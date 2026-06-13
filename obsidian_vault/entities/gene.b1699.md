---
entity_id: "gene.b1699"
entity_type: "gene"
name: "ydiS"
source_database: "NCBI RefSeq"
source_id: "gene-b1699"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1699"
  - "ydiS"
---

# ydiS

`gene.b1699`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1699`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydiS (gene.b1699) is a gene entity. It encodes ydiS (protein.P77337). Encoded protein function: FUNCTION: Probably accepts electrons from YdiQ/YdiR and reduces a quinone. EcoCyc product frame: G6922-MONOMER. Genomic coordinates: 1781395-1782684. EcoCyc protein note: YdiS is predicted to be a flavoprotein. YdiO, YdiQ, YdiR, YdiS, and YdiT may play a role in electron transport between the anaerobic fatty acid oxidation pathway and the respiratory chain .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77337|protein.P77337]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005671,ECOCYC:G6922,GeneID:946212`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1781395-1782684:+; feature_type=gene
