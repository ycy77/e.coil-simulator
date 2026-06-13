---
entity_id: "gene.b4845"
entity_type: "gene"
name: "xtpA"
source_database: "NCBI RefSeq"
source_id: "gene-b4845"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4845"
  - "xtpA"
---

# xtpA

`gene.b4845`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4845`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

xtpA (gene.b4845) is a gene entity. It encodes xtpA (protein.P0DXX6). Encoded protein function: FUNCTION: Controls the expression of small non-coding RNA GcvB, which represses the expression of many amino acid transporter proteins and uptake of aminoglycoside antibiotics in cells (PubMed:35081614). Might be a transcriptional activator (Probable) (PubMed:35081614). An RNA (xtr) with a tRNA-like fold possibly derived from tRNA-Arg(UCG) is encoded entirely within the protein; xtr does not have the sequence corresponding to tRNA anticodon or variable arms (PubMed:35081614). 10 synonymous codon changes in the xtr region of xtpA have the same phenotype as a deletion mutation, suggesting the mRNA secondary structure is important for function (PubMed:35081614). {ECO:0000269|PubMed:35081614, ECO:0000305|PubMed:35081614}. EcoCyc product frame: MONOMER0-4561. Genomic coordinates: 345252-345434. EcoCyc protein note: XtpA is a small protein (60 amino acids) that appears to regulate genes involved in resistance to several aminoglycoside antibiotics through the positive regulation of the expression of the small RNA GcvB . The gene produces a leaderless mRNA that contains a sequence (xtr) that resembles the arginine-tRNA and encodes the peptide XtpA...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DXX6|protein.P0DXX6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ECOCYC:G0-17126,GeneID:302211664`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:345252-345434:+; feature_type=gene
