---
entity_id: "gene.b1930"
entity_type: "gene"
name: "yedF"
source_database: "NCBI RefSeq"
source_id: "gene-b1930"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1930"
  - "yedF"
---

# yedF

`gene.b1930`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1930`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yedF (gene.b1930) is a gene entity. It encodes yedF (protein.P0AA31). Encoded protein function: Putative sulfur carrier protein YedF EcoCyc product frame: EG11661-MONOMER. Genomic coordinates: 2009479-2009712. EcoCyc protein note: YedF shows sequence similarity to the sulfur transfer protein TusA; however, unlike TusA, YedF does not appear to function in molybdenum cofactor assembly . Structural characterization of YedF has been performed by NMR. The protein exhibits a two-layered α-β sandwich-type fold and shows structural similarity to translation initiation factor 3, indicating that the protein might bind RNA . YedF is soluble and has 31% identity to TusA .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA31|protein.P0AA31]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006425,ECOCYC:EG11661,GeneID:946909`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2009479-2009712:+; feature_type=gene
