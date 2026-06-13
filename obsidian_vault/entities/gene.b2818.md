---
entity_id: "gene.b2818"
entity_type: "gene"
name: "argA"
source_database: "NCBI RefSeq"
source_id: "gene-b2818"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2818"
  - "argA"
---

# argA

`gene.b2818`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2818`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

argA (gene.b2818) is a gene entity. It encodes argA (protein.P0A6C5). Encoded protein function: Amino-acid acetyltransferase (EC 2.3.1.1) (N-acetylglutamate synthase) (AGS) (NAGS) EcoCyc product frame: N-ACETYLTRANSFER-MONOMER. EcoCyc synonyms: Arg2, Arg1. Genomic coordinates: 2949242-2950573.

## Biological Role

Repressed by argR (protein.P0A6D0), lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6C5|protein.P0A6C5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `C` - regulator=ArgR; target=argA; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009245,ECOCYC:EG10063,GeneID:947289`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2949242-2950573:+; feature_type=gene
