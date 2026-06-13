---
entity_id: "gene.b1880"
entity_type: "gene"
name: "flhB"
source_database: "NCBI RefSeq"
source_id: "gene-b1880"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1880"
  - "flhB"
---

# flhB

`gene.b1880`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1880`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

flhB (gene.b1880) is a gene entity. It encodes flhB (protein.P76299). Encoded protein function: FUNCTION: Required for formation of the rod structure in the basal body of the flagellar apparatus. Together with FliI and FliH, may constitute the export apparatus of flagellin. EcoCyc product frame: G7028-MONOMER. EcoCyc synonyms: yecQ, flaG. Genomic coordinates: 1965043-1966191. EcoCyc protein note: FlhB is one of six integral membrane components of the flagellar export apparatus. FlhB has two regions: the hydrophobic N-terminal domain which, according to hydophobicity studies, crosses the cytoplasmic membrane four times and the C-terminal cytoplasmic domain .

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76299|protein.P76299]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006275,ECOCYC:G7028,GeneID:946391`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1965043-1966191:-; feature_type=gene
