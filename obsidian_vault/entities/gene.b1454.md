---
entity_id: "gene.b1454"
entity_type: "gene"
name: "yncG"
source_database: "NCBI RefSeq"
source_id: "gene-b1454"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1454"
  - "yncG"
---

# yncG

`gene.b1454`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1454`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yncG (gene.b1454) is a gene entity. It encodes yncG (protein.P76117). Encoded protein function: Uncharacterized GST-like protein YncG EcoCyc product frame: G6765-MONOMER. Genomic coordinates: 1526247-1526864. EcoCyc protein note: YncG expressed in a cell-free system did not exhibit GSH-conjugating activities toward 1-chloro-2,4-dinitrobenzene (CDNB) . Overexpression of yncG from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hydrogen peroxide .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76117|protein.P76117]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004851,ECOCYC:G6765,GeneID:946023`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1526247-1526864:+; feature_type=gene
