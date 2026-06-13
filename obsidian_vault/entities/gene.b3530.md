---
entity_id: "gene.b3530"
entity_type: "gene"
name: "bcsC"
source_database: "NCBI RefSeq"
source_id: "gene-b3530"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3530"
  - "bcsC"
---

# bcsC

`gene.b3530`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3530`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bcsC (gene.b3530) is a gene entity. It encodes bcsC (protein.P37650). Encoded protein function: FUNCTION: Required for maximal bacterial cellulose synthesis. {ECO:0000250}. EcoCyc product frame: EG12257-MONOMER. EcoCyc synonyms: yhjL. Genomic coordinates: 3685700-3689173. EcoCyc protein note: BcsC is encoded in a predicted operon together with bcsA, bcsB, and bcsZ. In many E. coli strains, these genes are involved in cellulose biosynthesis, a characteristic of the rdar (red, dry and rough) morphotype. However, the K-12 laboratory strain of E. coli does not show a rdar morphotype and does not produce cellulose . In E. coli K-12 strains such as W3110 and MG1655, a "domesticating SNP" consists of a point mutation that introduces a stop codon after the first 5 amino acids of the wild-type bcsQ ORF. This domesticating SNP lowers expression of both bcsQ and the downstream bcsA gene. After repairing the SNP, the resulting "de-domesticated" W3110 derivative strain produces cellulose and has dramatically altered biofilm morphology...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37650|protein.P37650]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011538,ECOCYC:EG12257,GeneID:948047`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3685700-3689173:-; feature_type=gene
