---
entity_id: "gene.b1803"
entity_type: "gene"
name: "yeaX"
source_database: "NCBI RefSeq"
source_id: "gene-b1803"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1803"
  - "yeaX"
---

# yeaX

`gene.b1803`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1803`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yeaX (gene.b1803) is a gene entity. It encodes yeaX (protein.P76254). Encoded protein function: FUNCTION: Converts carnitine to trimethylamine and malic semialdehyde. Can also use gamma-butyrobetaine, choline and betaine as substrates. {ECO:0000269|PubMed:25440057}. EcoCyc product frame: G6989-MONOMER. Genomic coordinates: 1885845-1886810. EcoCyc protein note: When incubated together in the presence of NADH, YeaWX liberated TRIMETHYLAMINE from several substrates, including CARNITINE, GAMMA-BUTYROBETAINE and CHOLINE . It has not yet been determined whether a physical YeaWX complex exists.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76254|protein.P76254]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006000,ECOCYC:G6989,GeneID:946329`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1885845-1886810:+; feature_type=gene
