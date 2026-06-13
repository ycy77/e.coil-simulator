---
entity_id: "gene.b3573"
entity_type: "gene"
name: "ysaA"
source_database: "NCBI RefSeq"
source_id: "gene-b3573"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3573"
  - "ysaA"
---

# ysaA

`gene.b3573`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3573`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ysaA (gene.b3573) is a gene entity. It encodes ysaA (protein.P56256). Encoded protein function: Putative electron transport protein YsaA EcoCyc product frame: EG12277-MONOMER. EcoCyc synonyms: yiaI. Genomic coordinates: 3741109-3741582. EcoCyc protein note: YsaA is a ferredoxin-like protein containing cysteine-rich motifs that indicate the presence of iron-sulfur clusters. The EG11552-MONOMER HydN protein is the most closely related paralog within the E. coli K-12 genome . Bacterial two-hybrid assays were used to build an interaction network for the ferredoxin-like family of proteins; YsaA was shown to interact with itself as well as AegA, HycB, HycF, HydN . A ΔysaA mutation reduces FORMATEDEHYDROGH-MONOMER (FDH-H) activity to 57% of wild-type. Mutant strains containing a hydN ysaA double deletion or a hydN ysaA hycB triple deletion show reduced FDH-H activity to 28% and 1% of wild type levels, respectively .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P56256|protein.P56256]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011674,ECOCYC:EG12277,GeneID:948085`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3741109-3741582:-; feature_type=gene
