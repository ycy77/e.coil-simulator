---
entity_id: "gene.b3262"
entity_type: "gene"
name: "yhdJ"
source_database: "NCBI RefSeq"
source_id: "gene-b3262"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3262"
  - "yhdJ"
---

# yhdJ

`gene.b3262`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3262`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhdJ (gene.b3262) is a gene entity. It encodes yhdJ (protein.P28638). Encoded protein function: FUNCTION: A beta subtype methylase, recognizes the double-stranded sequence 5'-ATGCAT-3' and methylates A-5. {ECO:0000269|PubMed:17400740, ECO:0000303|PubMed:12654995}. EcoCyc product frame: EG11498-MONOMER. Genomic coordinates: 3411653-3412537. EcoCyc protein note: Overexpression of YdhJ leads to methylation of genomic DNA at the NsiI recognition sequence (5'-ATGCAT-3'), and partially purified YdhJ is shown to methylate this sequence to produce N6-methyladenine in the 3' adenine position of ATGCAT in vitro . ydhJ is not an essential gene, and overexpression of ydhJ does not alter cell morphology . Overexpression of yhdJ from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hypochlorous acid . A retracted publication claimed that the "CcrM" protein is a cell cycle-regulated DNA adenine methyltransferase that is essential for viability.

## Biological Role

Repressed by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P28638|protein.P28638]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010706,ECOCYC:EG11498,GeneID:947695`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3411653-3412537:+; feature_type=gene
