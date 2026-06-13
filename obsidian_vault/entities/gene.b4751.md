---
entity_id: "gene.b4751"
entity_type: "gene"
name: "yoaL"
source_database: "NCBI RefSeq"
source_id: "gene-b4751"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4751"
  - "yoaL"
---

# yoaL

`gene.b4751`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4751`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yoaL (gene.b4751) is a gene entity. It encodes yoaL (protein.P0DPP2). Encoded protein function: FUNCTION: May serve a regulatory role in expression of downstream gene yoaE; in a yoaL-yoaE-lacZ fusion mutation of the start codon to a stop codon in yoaL decreases expression of beta-galactosidase, suggesting translation of the 2 genes is coupled. {ECO:0000269|PubMed:30837344}. EcoCyc product frame: MONOMER0-4429. Genomic coordinates: 1901573-1901731. EcoCyc protein note: YoaL was identified as a previously unannotated small protein; it is expressed at approximately equal levels during exponential growth and stationary phase in rich growth medium . Introduction of a stop codon into the yoaL ORF leads to decreased expression of the downstream yoaE gene, suggesting translational coupling .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DPP2|protein.P0DPP2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ECOCYC:G0-16745,GeneID:38094965`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1901573-1901731:-; feature_type=gene
