---
entity_id: "gene.b1139"
entity_type: "gene"
name: "lit"
source_database: "NCBI RefSeq"
source_id: "gene-b1139"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1139"
  - "lit"
---

# lit

`gene.b1139`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1139`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lit (gene.b1139) is a gene entity. It encodes lit (protein.P11072). Encoded protein function: FUNCTION: Interacts with a short DNA sequence about one-quarter of the way into the major capsid protein gene 23 of T4; general translation inhibition occurs when this late gene of the virus is expressed. {ECO:0000269|PubMed:2452152}. EcoCyc product frame: EG10535-MONOMER. Genomic coordinates: 1198695-1199588. EcoCyc protein note: The lit gene is part of the defective prophage element e14 . A mutation in the putative promoter region of the lit gene (termed litCon) causes constitutive expression of Lit and blocks late gene expression during T4 infection, and thus causes phage exclusion . The inhibitory effect of Lit on T4 replication is dependent on the gol site located within gene 23, which encodes the major capsid protein of T4 . Translation of the gol region in the presence of Lit protein causes global inhibition of translation . Both in vivo and in an in vitro system consisting of purified Lit protein, translation elongation factor TU (EF-Tu), and a short synthetic peptide derived from the gol region, interaction between the Lit protein and the gol product leads to the cleavage of EF-Tu . The substrate for Lit appears to be a specific complex between the Gol peptide and domains II and III of EF-Tu...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P11072|protein.P11072]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003834,ECOCYC:EG10535,GeneID:948421`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1198695-1199588:+; feature_type=gene
