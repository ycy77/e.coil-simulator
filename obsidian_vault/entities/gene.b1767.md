---
entity_id: "gene.b1767"
entity_type: "gene"
name: "ansA"
source_database: "NCBI RefSeq"
source_id: "gene-b1767"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1767"
  - "ansA"
---

# ansA

`gene.b1767`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1767`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ansA (gene.b1767) is a gene entity. It encodes ansA (protein.P0A962). Encoded protein function: L-asparaginase 1 (EC 3.5.1.1) (L-asparaginase I) (L-ASNase I) (L-asparagine amidohydrolase I) EcoCyc product frame: ANSA-MONOMER. Genomic coordinates: 1850860-1851876.

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A962|protein.P0A962]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005886,ECOCYC:EG10045,GeneID:946278`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1850860-1851876:+; feature_type=gene
