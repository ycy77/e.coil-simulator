---
entity_id: "gene.b2880"
entity_type: "gene"
name: "ygfM"
source_database: "NCBI RefSeq"
source_id: "gene-b2880"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2880"
  - "ygfM"
---

# ygfM

`gene.b2880`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2880`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygfM (gene.b2880) is a gene entity. It encodes ygfM (protein.P64557). Encoded protein function: Uncharacterized protein YgfM EcoCyc product frame: G7499-MONOMER. Genomic coordinates: 3020540-3021319. EcoCyc protein note: YgfM is consistently found in the same location as XdhD in MIRAGE experiments. Thus the two proteins may form a complex, as has been proposed previously .

## Enriched Pathways

- `eco00450` Selenocompound metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64557|protein.P64557]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009456,ECOCYC:G7499,GeneID:949071`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3020540-3021319:+; feature_type=gene
