---
entity_id: "gene.b1194"
entity_type: "gene"
name: "ycgR"
source_database: "NCBI RefSeq"
source_id: "gene-b1194"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1194"
  - "ycgR"
---

# ycgR

`gene.b1194`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1194`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycgR (gene.b1194) is a gene entity. It encodes ycgR (protein.P76010). Encoded protein function: FUNCTION: Acts as a flagellar brake, regulating swimming and swarming in a bis-(3'-5') cyclic diguanylic acid (c-di-GMP)-dependent manner. When bound to c-di-GMP it binds to elements of the flagellar motor (MotA (PubMed:20303158) and/or FliG and FliM (PubMed:20346719), binding to FliM also occurs in the absence of c-di-GMP), causing the motor to slow down. Thus, increasing levels of c-di-GMP lead to decreased motility. Probably binds 1 c-di-GMP dimer per subunit. {ECO:0000269|PubMed:11031114, ECO:0000269|PubMed:16920715, ECO:0000269|PubMed:20303158, ECO:0000269|PubMed:20346719}. EcoCyc product frame: G6623-MONOMER. Genomic coordinates: 1243793-1244527. EcoCyc protein note: YcgR regulates flagellar motility in a C-DI-GMP (c-di-GMP)-dependent manner in vivo . Entry into stationary phase initiates production of increased levels of c-di-GMP, which binds to YcgR and thereby leads to slower flagellar motor speeds and increased counter-clockwise flagellar rotation bias . YcgR first biases the flagellar motor towards counter-clockwise rotation and subsequently decreases motor speed . c-di-GMP-bound YcgR acts as a molecular brake that interacts directly with the MOTA-FLAGELLAR-MOTOR-STATOR-PROTEIN MotA flagellar stator element at a 1:4 ratio...

## Biological Role

Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76010|protein.P76010]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=ycgR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004009,ECOCYC:G6623,GeneID:947609`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1243793-1244527:-; feature_type=gene
