---
entity_id: "gene.b0104"
entity_type: "gene"
name: "guaC"
source_database: "NCBI RefSeq"
source_id: "gene-b0104"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0104"
  - "guaC"
---

# guaC

`gene.b0104`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0104`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

guaC (gene.b0104) is a gene entity. It encodes guaC (protein.P60560). Encoded protein function: FUNCTION: Catalyzes the irreversible NADPH-dependent deamination of GMP to IMP. It functions in the conversion of nucleobase, nucleoside and nucleotide derivatives of G to A nucleotides, and in maintaining the intracellular balance of A and G nucleotides. EcoCyc product frame: GMP-REDUCT-MONOMER. Genomic coordinates: 113444-114487.

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P60560|protein.P60560]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000362,ECOCYC:EG10422,GeneID:948986`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:113444-114487:+; feature_type=gene
