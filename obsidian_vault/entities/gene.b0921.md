---
entity_id: "gene.b0921"
entity_type: "gene"
name: "cmoM"
source_database: "NCBI RefSeq"
source_id: "gene-b0921"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0921"
  - "cmoM"
---

# cmoM

`gene.b0921`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0921`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cmoM (gene.b0921) is a gene entity. It encodes cmoM (protein.P36566). Encoded protein function: FUNCTION: Catalyzes the methylation of 5-carboxymethoxyuridine (cmo5U) to form 5-methoxycarbonylmethoxyuridine (mcmo5U) at position 34 in tRNAs. Four tRNAs (tRNA(Ala1), tRNA(Ser1), tRNA(Pro3) and tRNA(Thr4)) are fully modified with mcmo5U in stationary-phase E.coli. Also present at low frequency in tRNA(Leu3) and tRNA(Val1). {ECO:0000269|PubMed:26681692}. EcoCyc product frame: EG12167-MONOMER. EcoCyc synonyms: ycbD, smtA. Genomic coordinates: 973537-974322.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36566|protein.P36566]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003131,ECOCYC:EG12167,GeneID:945547`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:973537-974322:+; feature_type=gene
