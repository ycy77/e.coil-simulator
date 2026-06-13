---
entity_id: "gene.b2021"
entity_type: "gene"
name: "hisC"
source_database: "NCBI RefSeq"
source_id: "gene-b2021"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2021"
  - "hisC"
---

# hisC

`gene.b2021`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2021`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hisC (gene.b2021) is a gene entity. It encodes hisC (protein.P06986). Encoded protein function: Histidinol-phosphate aminotransferase (EC 2.6.1.9) (Imidazole acetol-phosphate transaminase) (HPAT) (HspAT) EcoCyc product frame: HISTPHOSTRANS-MONOMER. Genomic coordinates: 2092398-2093468.

## Enriched Pathways

- `eco00340` Histidine metabolism (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00401` Novobiocin biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06986|protein.P06986]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006717,ECOCYC:EG10446,GeneID:946551`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2092398-2093468:+; feature_type=gene
