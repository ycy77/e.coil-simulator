---
entity_id: "gene.b2458"
entity_type: "gene"
name: "eutD"
source_database: "NCBI RefSeq"
source_id: "gene-b2458"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2458"
  - "eutD"
---

# eutD

`gene.b2458`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2458`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

eutD (gene.b2458) is a gene entity. It encodes eutD (protein.P77218). Encoded protein function: FUNCTION: When expressed independently of the eut operon it can restore growth to a double pta-acs deletion mutant. {ECO:0000269|PubMed:21046341}. EcoCyc product frame: G7288-MONOMER. EcoCyc synonyms: ypfA, eutI. Genomic coordinates: 2572489-2573505.

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77218|protein.P77218]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008097,ECOCYC:G7288,GeneID:946940`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2572489-2573505:-; feature_type=gene
