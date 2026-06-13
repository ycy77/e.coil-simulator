---
entity_id: "gene.b4159"
entity_type: "gene"
name: "mscM"
source_database: "NCBI RefSeq"
source_id: "gene-b4159"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4159"
  - "mscM"
---

# mscM

`gene.b4159`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4159`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mscM (gene.b4159) is a gene entity. It encodes mscM (protein.P39285). Encoded protein function: FUNCTION: Mechanosensitive channel that protects cells against hypoosmotic stress when highly overexpressed. Gates spontaneously in response to increased membrane tension. {ECO:0000269|PubMed:22874652}. EcoCyc product frame: G7840-MONOMER. EcoCyc synonyms: yjeP. Genomic coordinates: 4386047-4389370.

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39285|protein.P39285]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=mscM; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013621,ECOCYC:G7840,GeneID:948676`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4386047-4389370:-; feature_type=gene
