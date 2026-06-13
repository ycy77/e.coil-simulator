---
entity_id: "gene.b1328"
entity_type: "gene"
name: "pgrR"
source_database: "NCBI RefSeq"
source_id: "gene-b1328"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1328"
  - "pgrR"
---

# pgrR

`gene.b1328`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1328`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pgrR (gene.b1328) is a gene entity. It encodes pgrR (protein.P77333). Encoded protein function: FUNCTION: Regulates the expression of genes involved in peptidoglycan (PG) degradation. Could play a role in switch control between recycling and degradation of PG peptides. Negatively regulates the expression of the ycjY-ymjD-ymjC-mpaA operon by binding to the PgrR-box. In addition, other genes are predicted to be under the control of PgrR, including genes related to membrane formation and function. {ECO:0000269|PubMed:23301696}. EcoCyc product frame: G6664-MONOMER. EcoCyc synonyms: ycjZ. Genomic coordinates: 1391991-1392890. EcoCyc protein note: Based on analysis with the Genomic SELEX screening system, PgrR was identified as a repressor of the expression of genes of the initial enzymes for peptidoglycan (PG) peptide degradation as well as genes of the switch control between recycling and degradation of PG peptides, which are induced upon exposure to heat shock or membrane distortion . PgrR negatively controls ycjY-ymjD-ymjC-mpaA operon expression and binds to the palindromic sequence ATCATTT-AAATGAT . Both the pgrR and ycjY promoters are recognized by RpoH (σ32) and RpoE (σ24), both of which are involved in the heat shock response, and by FecI (σ19), which is involved in the response to extracytoplasmic stimuli . Eleven possible targets were predicted to be under PgrR control...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77333|protein.P77333]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004457,ECOCYC:G6664,GeneID:945930`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1391991-1392890:+; feature_type=gene
