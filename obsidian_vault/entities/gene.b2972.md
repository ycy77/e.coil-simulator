---
entity_id: "gene.b2972"
entity_type: "gene"
name: "pppA"
source_database: "NCBI RefSeq"
source_id: "gene-b2972"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2972"
  - "pppA"
---

# pppA

`gene.b2972`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2972`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pppA (gene.b2972) is a gene entity. It encodes pppA (protein.Q46836). Encoded protein function: FUNCTION: A pre-pilin peptidase involved in a type II secretion system (T2SS, formerly general secretion pathway, GSP) for the export of folded proteins across the outer membrane. {ECO:0000305}. EcoCyc product frame: G7539-MONOMER. EcoCyc synonyms: yghH. Genomic coordinates: 3113543-3114352. EcoCyc protein note: In E. coli K-12, pppA encodes a functional prepilin peptidase; pppA appears to be poorly translated but the resulting peptidase activity is sufficient to allow temperature dependent partial processing of plasmid encoded pre-pilin substrates, Neisseria gonorrhoeae prePilE and Klebsiella pneumoniae prePulG . Heterologous over-expression of pppA is capable of restoring function to both secretion and piliation dedicated systems in a Pseudomonas aeruginosa strain lacking its endogenous prepilin peptidase, PilD . The cognate substrate of PppA is not clear - when expressed from a plasmid, it is capable of processing preG7702-MONOMER GspG (product of the normally cryptic pseudopilin gene) and preEG12107-MONOMER PpdD (a putative type IV prepilin-like protein) . yghJ-pppA-yghGFED are the vestigial genes of a type II secretion system (T2SSβ) present in pathogenic (and some commensal) E. coli strains...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46836|protein.Q46836]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009751,ECOCYC:G7539,GeneID:947467`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3113543-3114352:-; feature_type=gene
