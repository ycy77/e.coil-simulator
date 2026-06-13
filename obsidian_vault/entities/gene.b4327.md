---
entity_id: "gene.b4327"
entity_type: "gene"
name: "hypT"
source_database: "NCBI RefSeq"
source_id: "gene-b4327"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4327"
  - "hypT"
---

# hypT

`gene.b4327`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4327`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hypT (gene.b4327) is a gene entity. It encodes yjiE (protein.P39376). Encoded protein function: FUNCTION: Protects cells from HOCl (hypochlorite) stress but not peroxide or diamide stress. Decreases the intracellular load of reactive oxygen species by up-regulating genes involved in methionine and cysteine biosynthesis and down-regulating Fur-regulated genes involved in iron acquisition. Has also been suggested to down-regulate expression of the flagellar regulon, decreasing motility, but this activity was not confirmed in a second study (PubMed:22223481). {ECO:0000269|PubMed:22223481}. EcoCyc product frame: G7924-MONOMER. EcoCyc synonyms: qseD, yjiE. Genomic coordinates: 4557378-4558289.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39376|protein.P39376]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0014192,ECOCYC:G7924,GeneID:948852`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4557378-4558289:-; feature_type=gene
