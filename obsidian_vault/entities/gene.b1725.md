---
entity_id: "gene.b1725"
entity_type: "gene"
name: "yniA"
source_database: "NCBI RefSeq"
source_id: "gene-b1725"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1725"
  - "yniA"
---

# yniA

`gene.b1725`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1725`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yniA (gene.b1725) is a gene entity. It encodes yniA (protein.P77739). Encoded protein function: FUNCTION: Ketoamine kinase that phosphorylates ketoamines on the third carbon of the sugar moiety to generate ketoamine 3-phosphate (By similarity). Its precise substrate are unknown: does not have ribulosamine and/or erythrulosamine 3-kinase activity in vitro (PubMed:17681011). {ECO:0000250|UniProtKB:Q9H479, ECO:0000269|PubMed:17681011}. EcoCyc product frame: G6930-MONOMER. Genomic coordinates: 1807796-1808656. EcoCyc protein note: YniA is similar to a family of fructosamine 3-kinases, but is lacking some residues that are conserved within the family. Purified YniA was inactive with all tested substrates, including ribuloselysine, erythruloselysine, and a range of compounds such as D-ribulose, choline, L-serine, and thiamine .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77739|protein.P77739]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005755,ECOCYC:G6930,GeneID:946236`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1807796-1808656:+; feature_type=gene
