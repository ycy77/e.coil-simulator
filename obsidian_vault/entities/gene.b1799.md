---
entity_id: "gene.b1799"
entity_type: "gene"
name: "dmlR"
source_database: "NCBI RefSeq"
source_id: "gene-b1799"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1799"
  - "dmlR"
---

# dmlR

`gene.b1799`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1799`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dmlR (gene.b1799) is a gene entity. It encodes dmlR (protein.P76250). Encoded protein function: FUNCTION: Transcriptional regulator required for the aerobic growth on D-malate as the sole carbon source. Induces the expression of dmlA in response to D-malate or L- or meso-tartrate. Negatively regulates its own expression. {ECO:0000269|PubMed:17088549, ECO:0000269|PubMed:20233924}. EcoCyc product frame: G6985-MONOMER. EcoCyc synonyms: yeaT. Genomic coordinates: 1880886-1881809. EcoCyc protein note: DmlR (D-malate degradation regulator), formerly known as YeaT , is required for growth on D-malate as the sole carbon source under high-throughput growth conditions with limited aeration . DmlR is a LysR-type transcriptional regulator and has 49% sequence identity and 67% similarity with TtdR . Induction of dmlA by DmlR requires the presence of D-malate or L- or meso-tartate, but only D-malate supports aerobic growth . The expression of dmlR is subject to negative autoregulation independently of DcuS-DcuS and TtdR . DmlR was transcriptionally upregulated in iron excess over iron limitation at 63% dissolved oxygen as determined by RNA-seq . The DmlR binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76250|protein.P76250]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005987,ECOCYC:G6985,GeneID:946316`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1880886-1881809:-; feature_type=gene
