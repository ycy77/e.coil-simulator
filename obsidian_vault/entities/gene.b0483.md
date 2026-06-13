---
entity_id: "gene.b0483"
entity_type: "gene"
name: "ybaQ"
source_database: "NCBI RefSeq"
source_id: "gene-b0483"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0483"
  - "ybaQ"
---

# ybaQ

`gene.b0483`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0483`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybaQ (gene.b0483) is a gene entity. It encodes ybaQ (protein.P0A9T6). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YbaQ EcoCyc product frame: G6259-MONOMER. Genomic coordinates: 508218-508559. EcoCyc protein note: YbaQ appears to belong to the Xre family of transcription factors (TFs), and it was predicted to regulate genes related to metabolism . YbaQ was confirmed as a TF through an integrated workflow comprised of computational prediction, knowledge-based classification, and experimental validation of candidate TFs at the genome scale . Compared to known global TFs, YbaQ exhibits some interesting regulatory features. First, it has more intragenic binding peaks and fewer peaks located within putative regulatory regions. Second, it has fewer binding peaks than global TFs, such as CRP, Lrp, Fnr, and ArcA. Third, it binds to more genes with putative functions. Finally, its expression level is lower relative to that of the majority of global TFs . The transcription of the ybaQ gene is affected by conditions that lead to biofilm formation, heat stress and glucose-lactose shift . The YbaQ binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9T6|protein.P0A9T6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001677,ECOCYC:G6259,GeneID:948800`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:508218-508559:+; feature_type=gene
