---
entity_id: "gene.b0867"
entity_type: "gene"
name: "amiD"
source_database: "NCBI RefSeq"
source_id: "gene-b0867"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0867"
  - "amiD"
---

# amiD

`gene.b0867`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0867`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

amiD (gene.b0867) is a gene entity. It encodes amiD (protein.P75820). Encoded protein function: N-acetylmuramoyl-L-alanine amidase AmiD (EC 3.5.1.28) EcoCyc product frame: G6452-MONOMER. EcoCyc synonyms: ybjR. Genomic coordinates: 904913-905743. EcoCyc protein note: AmiD is an N-acetylmuramic acid-L-alanine amidase responsible for cleaving the bond between muramic acid and L-alanine within murein, muropeptides, and anhydro-muropeptides. AmiD is an outer membrane lipoprotein . nagB nagZ ampD amiD mutants are unable to release murein tripeptide from GlcNAc-anhMurNAc-tripeptide while the nagB nagZ ampD mutant is able to do so . Assays of purified AmiD show it prefers GlcNAc-anhMurNAc-peptides or GlcNAc-MurNAc-peptides as substrates over those lacking GlcNAc . Purified AmiD was shown to hydrolyse peptidoglycan fragments that have at least three amino acids in their peptide chains and the enzyme activity was inhibited by its substrate in vitro . Review:

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75820|protein.P75820]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002947,ECOCYC:G6452,GeneID:945494`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:904913-905743:+; feature_type=gene
