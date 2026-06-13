---
entity_id: "gene.b4054"
entity_type: "gene"
name: "tyrB"
source_database: "NCBI RefSeq"
source_id: "gene-b4054"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4054"
  - "tyrB"
---

# tyrB

`gene.b4054`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4054`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tyrB (gene.b4054) is a gene entity. It encodes tyrB (protein.P04693). Encoded protein function: FUNCTION: Broad-specificity enzyme that catalyzes the transamination of 2-ketoisocaproate, p-hydroxyphenylpyruvate, and phenylpyruvate to yield leucine, tyrosine, and phenylalanine, respectively. In vitro, is able to catalyze the conversion of beta-methyl phenylpyruvate to the nonproteinogenic amino acid (2S,3S)-beta-methyl-phenylalanine, a building block of the antibiotic mannopeptimycin produced by Streptomyces hygroscopicus NRRL3085. {ECO:0000269|PubMed:19731276}. EcoCyc product frame: TYRB-MONOMER. Genomic coordinates: 4267114-4268307.

## Biological Role

Repressed by tyrR (protein.P07604). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
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

- `encodes` --> [[protein.P04693|protein.P04693]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=tyrB; function=+
- `represses` <-- [[protein.P07604|protein.P07604]] `RegulonDB` `C` - regulator=TyrR; target=tyrB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013278,ECOCYC:EG11040,GeneID:948563`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4267114-4268307:+; feature_type=gene
