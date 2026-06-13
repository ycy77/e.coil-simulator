---
entity_id: "gene.b0149"
entity_type: "gene"
name: "mrcB"
source_database: "NCBI RefSeq"
source_id: "gene-b0149"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0149"
  - "mrcB"
---

# mrcB

`gene.b0149`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0149`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mrcB (gene.b0149) is a gene entity. It encodes mrcB (protein.P02919). Encoded protein function: FUNCTION: Cell wall formation. Synthesis of cross-linked peptidoglycan from the lipid intermediates. The enzyme has a penicillin-insensitive transglycosylase N-terminal domain (formation of linear glycan strands) and a penicillin-sensitive transpeptidase C-terminal domain (cross-linking of the peptide subunits). EcoCyc product frame: MONOMER0-4521. EcoCyc synonyms: pbpF, ponB. Genomic coordinates: 164730-167264.

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P02919|protein.P02919]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000516,ECOCYC:EG10605,GeneID:944843`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:164730-167264:+; feature_type=gene
