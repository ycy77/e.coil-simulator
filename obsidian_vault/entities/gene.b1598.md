---
entity_id: "gene.b1598"
entity_type: "gene"
name: "ydgD"
source_database: "NCBI RefSeq"
source_id: "gene-b1598"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1598"
  - "ydgD"
---

# ydgD

`gene.b1598`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1598`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydgD (gene.b1598) is a gene entity. It encodes ydgD (protein.P76176). Encoded protein function: Uncharacterized serine protease YdgD (EC 3.4.21.-) EcoCyc product frame: G6856-MONOMER. Genomic coordinates: 1671960-1672781. EcoCyc protein note: YdgD is a predicted periplasmic serine protease that may be involved in cell envelope protein quality control . Sequence similarity suggests that it may contain β-barrel structure(s) . A ydgD single mutant does not have a phenotype under the tested conditions; however, a EG10760 tsp ydgD double mutant does not grow in the presence of SDS/EDTA at either 37 or 42°C and shows increased membrane permeability. Expression of rpoE is induced 2.3-fold, and expression of spy is induced 4.3-fold in the tsp ydgD double mutant .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76176|protein.P76176]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005340,ECOCYC:G6856,GeneID:946436`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1671960-1672781:+; feature_type=gene
