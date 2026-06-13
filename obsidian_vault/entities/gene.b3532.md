---
entity_id: "gene.b3532"
entity_type: "gene"
name: "bcsB"
source_database: "NCBI RefSeq"
source_id: "gene-b3532"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3532"
  - "bcsB"
---

# bcsB

`gene.b3532`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3532`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bcsB (gene.b3532) is a gene entity. It encodes bcsB (protein.P37652). Encoded protein function: FUNCTION: Binds the cellulose synthase activator, bis-(3'-5') cyclic diguanylic acid (c-di-GMP). {ECO:0000250}. EcoCyc product frame: EG12259-MONOMER. EcoCyc synonyms: yhjN. Genomic coordinates: 3690268-3692607. EcoCyc protein note: BcsB is encoded in a predicted operon together with bcsA, bcsZ and bcsC. In other organisms, these genes are involved in cellulose biosynthesis, a characteristic of the rdar (red, dry and rough) morphotype. However, the K-12 laboratory strain of E. coli does not show a rdar morphotype and does not produce cellulose . In E. coli K-12 strains such as W3110 and MG1655, a "domesticating SNP" consists of a point mutation that introduces a stop codon after the first 5 amino acids of the wild-type bcsQ ORF. This domesticating SNP lowers expression of both bcsQ and the downstream bcsA gene. After repairing the SNP, the resulting "de-domesticated" W3110-derivative strain produces cellulose and has dramatically altered biofilm morphology . In the cellulose-producing strain E. coli 1094, the inner membrane and cytosolic Bcs proteins - BcsA, BcsB, BscQ, BcsG, BcsE, BcsR and BcsF - organize in a multisubunit, stable macrocomplex; two-hybrid assays identified multiple direct interactions between the subunits and a low resolution structure has been obtained (see also )...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37652|protein.P37652]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011545,ECOCYC:EG12259,GeneID:948045`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3690268-3692607:-; feature_type=gene
