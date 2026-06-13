---
entity_id: "gene.b4667"
entity_type: "gene"
name: "ibsA"
source_database: "NCBI RefSeq"
source_id: "gene-b4667"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4667"
  - "ibsA"
---

# ibsA

`gene.b4667`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4667`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ibsA (gene.b4667) is a gene entity. It encodes ibsA (protein.C1P607). Encoded protein function: FUNCTION: Toxic component of a type I toxin-antitoxin (TA) system. Overexpression causes cessation of growth. {ECO:0000269|PubMed:18710431}. EcoCyc product frame: MONOMER0-2859. Genomic coordinates: 2153349-2153408. EcoCyc protein note: The small open reading frame IbsA was detected by similarity to the open reading frames encoded on the opposite strand of the sib small RNAs . Overexpression of IbsA is toxic to the cell . IbsA: "induction brings stasis"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.C1P607|protein.C1P607]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ECOCYC:G0-10633,GeneID:7751625`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2153349-2153408:-; feature_type=gene
