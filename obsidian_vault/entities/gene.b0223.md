---
entity_id: "gene.b0223"
entity_type: "gene"
name: "yafJ"
source_database: "NCBI RefSeq"
source_id: "gene-b0223"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0223"
  - "yafJ"
---

# yafJ

`gene.b0223`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0223`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yafJ (gene.b0223) is a gene entity. It encodes yafJ (protein.Q47147). Encoded protein function: Putative glutamine amidotransferase YafJ (EC 2.4.2.-) EcoCyc product frame: G6107-MONOMER. Genomic coordinates: 244327-245094. EcoCyc protein note: YafJ has similarity to proteins of Neisseria gonorrhoeae and Azospirillum brasilense Yu62 .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47147|protein.Q47147]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000755,ECOCYC:G6107,GeneID:944906`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:244327-245094:+; feature_type=gene
