---
entity_id: "gene.b3188"
entity_type: "gene"
name: "sfsB"
source_database: "NCBI RefSeq"
source_id: "gene-b3188"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3188"
  - "sfsB"
---

# sfsB

`gene.b3188`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3188`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sfsB (gene.b3188) is a gene entity. It encodes sfsB (protein.P0ACH1). Encoded protein function: FUNCTION: This protein is involved in positive regulation of the metabolism of sugars. {ECO:0000250}. EcoCyc product frame: EG10656-MONOMER. EcoCyc synonyms: nlp, sfs7. Genomic coordinates: 3334909-3335187. EcoCyc protein note: This regulator participates in controlling several genes involved in maltose metabolism . It is similar to the Ner repressor protein of phage Mu. SfsB is not essential for viability . The SfsB binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu . SfsB: "sugar fermentation stimulation" Nlp: "Ner-like protein"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACH1|protein.P0ACH1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010477,ECOCYC:EG10656,GeneID:947960`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3334909-3335187:+; feature_type=gene
