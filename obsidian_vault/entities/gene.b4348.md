---
entity_id: "gene.b4348"
entity_type: "gene"
name: "hsdS"
source_database: "NCBI RefSeq"
source_id: "gene-b4348"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4348"
  - "hsdS"
---

# hsdS

`gene.b4348`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4348`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hsdS (gene.b4348) is a gene entity. It encodes hsdS (protein.P05719). Encoded protein function: FUNCTION: The specificity (S) subunit of a type I restriction enzyme; this subunit dictates DNA sequence specificity. The M and S subunits together form a methyltransferase (MTase) that methylates A-2 on the top and A-3 on the bottom strand of the sequence 5'-AACN(6)GTGC-3'. In the presence of the R subunit the complex can also act as an endonuclease, binding to the same target sequence but cutting the DNA some distance from this site. Whether the DNA is cut or modified depends on the methylation state of the target sequence. When the target site is unmodified, the DNA is cut. When the target site is hemimethylated, the complex acts as a maintenance MTase modifying the DNA so that both strands become methylated. After locating a non-methylated recognition site, the enzyme complex serves as a molecular motor that translocates DNA in an ATP-dependent manner until a collision occurs that triggers cleavage. {ECO:0000269|PubMed:4868368, ECO:0000269|PubMed:6255295, ECO:0000269|PubMed:8514761, ECO:0000269|PubMed:9033396}. EcoCyc product frame: EG10460-MONOMER. EcoCyc synonyms: hsp, hss, rm. Genomic coordinates: 4580068-4581462. EcoCyc protein note: HsdS is the specificity-determining component of the EcoKI restriction-modification system .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P05719|protein.P05719]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0014258,ECOCYC:EG10460,GeneID:948867`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4580068-4581462:-; feature_type=gene
