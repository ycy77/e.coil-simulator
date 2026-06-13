---
entity_id: "gene.b1386"
entity_type: "gene"
name: "tynA"
source_database: "NCBI RefSeq"
source_id: "gene-b1386"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1386"
  - "tynA"
---

# tynA

`gene.b1386`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1386`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tynA (gene.b1386) is a gene entity. It encodes tynA (protein.P46883). Encoded protein function: FUNCTION: The enzyme prefers aromatic over aliphatic amines. EcoCyc product frame: AMINEOXID-MONOMER. EcoCyc synonyms: feaA, maoA. Genomic coordinates: 1449076-1451349.

## Biological Role

Activated by feaR (protein.Q47129).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P46883|protein.P46883]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47129|protein.Q47129]] `RegulonDB` `C` - regulator=FeaR; target=tynA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004639,ECOCYC:EG13139,GeneID:945939`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1449076-1451349:-; feature_type=gene
