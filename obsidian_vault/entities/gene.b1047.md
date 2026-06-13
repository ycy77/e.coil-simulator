---
entity_id: "gene.b1047"
entity_type: "gene"
name: "opgC"
source_database: "NCBI RefSeq"
source_id: "gene-b1047"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1047"
  - "opgC"
---

# opgC

`gene.b1047`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1047`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

opgC (gene.b1047) is a gene entity. It encodes mdoC (protein.P75920). Encoded protein function: FUNCTION: Necessary for the succinyl substitution of periplasmic glucans. Could catalyze the transfer of succinyl residues from the cytoplasmic side of the membrane to the nascent glucan backbones on the periplasmic side of the membrane. EcoCyc product frame: G6552-MONOMER. EcoCyc synonyms: ymdD, mdoC. Genomic coordinates: 1107784-1108941. EcoCyc protein note: OpgC is required for wild-type succinyl modification of the branched periplasmic oligosaccharides known as CPD-16398 osmoregulated periplasmic glucans (OPG), formerly called membrane-derived oligosaccharides (MDO). The origin of the succinyl group is not known but is suggested to be SUC-COA (see ). OPGs extracted from opgC- cells (strain NFB1864 mdoB214::Tn10 mdoC1::Tn5) are devoid of succinyl residues . Succinylation of OPGs is not osmodependent . OpgC is predicted to be an innner membrane protein with 10 transmembrane domains . In the Transporter Classification Database OpgC is a member of the Acyltransferase-3/Putative Acetyl-CoA Transporter (ATAT) family.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75920|protein.P75920]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003553,ECOCYC:G6552,GeneID:946944`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1107784-1108941:-; feature_type=gene
