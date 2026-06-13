---
entity_id: "gene.b1382"
entity_type: "gene"
name: "ynbE"
source_database: "NCBI RefSeq"
source_id: "gene-b1382"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1382"
  - "ynbE"
---

# ynbE

`gene.b1382`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1382`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ynbE (gene.b1382) is a gene entity. It encodes ynbE (protein.P64448). Encoded protein function: FUNCTION: Involved in outer membrane lipid homeostasis (PubMed:38748582). Interacts with the inner membrane protein YdbH to form a functional protein bridge connecting the inner and outer membranes of the cell (PubMed:38748582). Is required for YdbH's function and may facilitate phospholipid transport through the periplasm (PubMed:38748582). {ECO:0000269|PubMed:38748582}. EcoCyc product frame: G6704-MONOMER. Genomic coordinates: 1445687-1445872. EcoCyc protein note: YnbE interacts with the inner membrane protein G6703-MONOMER YbdH to form a periplasmic protein bridge that connects the inner and outer membranes; ynbE forms an operon with ybdH and G6705, and ydbL is implicated in formation of the YdbH-YnbE complex . YnbE is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64448|protein.P64448]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004625,ECOCYC:G6704,GeneID:945946`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1445687-1445872:+; feature_type=gene
