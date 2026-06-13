---
entity_id: "gene.b2878"
entity_type: "gene"
name: "ygfK"
source_database: "NCBI RefSeq"
source_id: "gene-b2878"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2878"
  - "ygfK"
---

# ygfK

`gene.b2878`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2878`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygfK (gene.b2878) is a gene entity. It encodes ygfK (protein.Q46811). Encoded protein function: FUNCTION: Could be an iron-sulfur flavoprotein with NADPH:O(2) oxidoreductase activity. {ECO:0000305|PubMed:22094925}. EcoCyc product frame: G7497-MONOMER. Genomic coordinates: 3016060-3019158. EcoCyc protein note: Preliminary biochemical characterization has shown that YgfK is an iron-sulfur flavoprotein with NADPH:O2 oxidoreductase activity . Based on sequence similarity, YgfK was predicted to be a dihydrothymine dehydrogenase . A transposon insertion mutant in ygfK was unable to reduce selenate to selenium .

## Enriched Pathways

- `eco00450` Selenocompound metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46811|protein.Q46811]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009450,ECOCYC:G7497,GeneID:949068`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3016060-3019158:+; feature_type=gene
