---
entity_id: "gene.b1770"
entity_type: "gene"
name: "ydjF"
source_database: "NCBI RefSeq"
source_id: "gene-b1770"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1770"
  - "ydjF"
---

# ydjF

`gene.b1770`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1770`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydjF (gene.b1770) is a gene entity. It encodes ydjF (protein.P77721). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YdjF EcoCyc product frame: G6957-MONOMER. Genomic coordinates: 1854096-1854854. EcoCyc protein note: YdjF appears to belong to the DeoR family of transcription factors, and it was predicted to regulate genes related to metabolism . Upstream of the ydjF gene, a sequence was found that could work as a transcriptional promoter, and the transcription of the ydjF gene is affected by cadmium, stress, and glucose-lactose shift . The YdjF binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77721|protein.P77721]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005897,ECOCYC:G6957,GeneID:946272`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1854096-1854854:-; feature_type=gene
