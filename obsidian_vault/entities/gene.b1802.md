---
entity_id: "gene.b1802"
entity_type: "gene"
name: "yeaW"
source_database: "NCBI RefSeq"
source_id: "gene-b1802"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1802"
  - "yeaW"
---

# yeaW

`gene.b1802`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1802`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yeaW (gene.b1802) is a gene entity. It encodes yeaW (protein.P0ABR7). Encoded protein function: FUNCTION: Converts carnitine to trimethylamine and malic semialdehyde. Can also use gamma-butyrobetaine, choline and betaine as substrates. {ECO:0000269|PubMed:25440057}. EcoCyc product frame: G6988-MONOMER. Genomic coordinates: 1884665-1885789. EcoCyc protein note: Partially purified YeaW protein was shown to contain a [2Fe-2S] iron-sulfur cluster that can be reduced by dithionite, but not ascorbate, identifying it as a low-potential Rieske iron-sulfur cluster protein . When incubated together in the presence of NADH, YeaWX liberated TRIMETHYLAMINE from several substrates, including CARNITINE, GAMMA-BUTYROBETAINE and CHOLINE . It has not yet been determined whether a physical YeaWX complex exists.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABR7|protein.P0ABR7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005997,ECOCYC:G6988,GeneID:946325`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1884665-1885789:+; feature_type=gene
