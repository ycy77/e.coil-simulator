---
entity_id: "gene.b1159"
entity_type: "gene"
name: "mcrA"
source_database: "NCBI RefSeq"
source_id: "gene-b1159"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1159"
  - "mcrA"
---

# mcrA

`gene.b1159`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1159`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mcrA (gene.b1159) is a gene entity. It encodes mcrA (protein.P24200). Encoded protein function: FUNCTION: Restriction of 5-methyl and 5-hydroxymethylcytosines at the specific DNA sequence 5'-C(me)CGG-3'. EcoCyc product frame: EG10573-MONOMER. EcoCyc synonyms: rglA. Genomic coordinates: 1210346-1211179. EcoCyc protein note: The McrA protein is a type IV site-specific deoxyribonuclease and is one of three restriction systems defending the cell against foreign DNA, such as bacteriophages. It specifically recognizes 5-methylcytosine residues in DNA , but the precise recognition sequence has not yet been identified. McrA was initially identified as a cellular activity that degraded T-even phage DNA containing nonglucosylated DNA . The rglA and mcrA phenotypes are separable; see the discussion in and references therein. Structural modelling of McrA has identified similarity to the ββαMe superfamily of endonucleases . Linker insertion scanning mutagenesis has been used to study the functional domain architecture . mcrA is part of the defective lambdoid prophage element e14 . After induction of the SOS response by UV irradiation, the prophage is abortively excised from the E. coli chromosome, leading to decreased levels of McrA restriction within a cell population...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24200|protein.P24200]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003891,ECOCYC:EG10573,GeneID:945727`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1210346-1211179:+; feature_type=gene
