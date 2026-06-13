---
entity_id: "gene.b3711"
entity_type: "gene"
name: "yidZ"
source_database: "NCBI RefSeq"
source_id: "gene-b3711"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3711"
  - "yidZ"
---

# yidZ

`gene.b3711`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3711`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yidZ (gene.b3711) is a gene entity. It encodes yidZ (protein.P31463). Encoded protein function: FUNCTION: Involved in anaerobic NO protection. EcoCyc product frame: EG11721-MONOMER. Genomic coordinates: 3892765-3893724. EcoCyc protein note: YidZ was predicted to be a LysR-type transcription factor using the Hidden Markov Model . DNA binding was found by chromatin immunoprecipitation assays (ChIP-exo) . Gene expression profile analysis of the wild-type strain and a yidZ knockout strain using RNA-seq showed differential expression of a set of genes also identified by ChIP-exo, indicating they are the direct regulatory targets . RNA-seq studies showed that in a yidZ knockout strain, genes associated with carbohydrate transport and metabolism were upregulated while genes involved in acid stress response and amino acid transport and metabolism were downregulated with respect to the wild-type strain . Based on SWISS-MODEL, YidZ could form dimers or tetramers . Levels of yidZ mRNA are increased in cells treated with NO under anaerobic growth conditions. An E. coli strain lacking a functional yidZ gene is more sensitive to NO than wild type . The YidZ binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31463|protein.P31463]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012141,ECOCYC:EG11721,GeneID:948227`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3892765-3893724:+; feature_type=gene
