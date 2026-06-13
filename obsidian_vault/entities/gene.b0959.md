---
entity_id: "gene.b0959"
entity_type: "gene"
name: "sxy"
source_database: "NCBI RefSeq"
source_id: "gene-b0959"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0959"
  - "sxy"
---

# sxy

`gene.b0959`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0959`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sxy (gene.b0959) is a gene entity. It encodes sxy (protein.P75869). Encoded protein function: FUNCTION: Induces low levels of natural DNA uptake by inducing transcription of the competence genes (the CRP-S regulon) required for DNA transformation. Induction of the CRP-S regulon also requires Sxy-activated promoter (CRP-S), cAMP receptor protein (CRP) and cAMP (PubMed:17068078, PubMed:22532864). Induces CRP-S site-containing genes which are involved in genome maintenance and transcription or encoding transposases and toxin-antitoxin pairs (PubMed:19502395). {ECO:0000269|PubMed:17068078, ECO:0000269|PubMed:19502395, ECO:0000269|PubMed:22532864}. EcoCyc product frame: G6494-MONOMER. EcoCyc synonyms: yccR. Genomic coordinates: 1021138-1021767. EcoCyc protein note: Sxy is required for transcription from a subset of PD00257 CRP-activated promoters. Sxy is not thought to bind to DNA itself . Genes that are differentially expressed upon overexpression of Sxy were identified by microarray analysis . Although expression of Sxy induces the expression of competence gene homologs, natural transformation was not detected . However, transformation occurs when Sxy is expressed while recombination functions are provided by the λ Red recombinase . Expression of sxy is autoregulated . The Sxy protein is unstable and is rapidly degraded by the Lon protease...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75869|protein.P75869]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003249,ECOCYC:G6494,GeneID:946504`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1021138-1021767:+; feature_type=gene
