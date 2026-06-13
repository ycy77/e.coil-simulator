---
entity_id: "gene.b0610"
entity_type: "gene"
name: "rnk"
source_database: "NCBI RefSeq"
source_id: "gene-b0610"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0610"
  - "rnk"
---

# rnk

`gene.b0610`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0610`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rnk (gene.b0610) is a gene entity. It encodes rnk (protein.P0AFW4). Encoded protein function: FUNCTION: May act as an anti-Gre factor. Regulates the level of the nucleoside diphosphate kinase Ndk. {ECO:0000255|HAMAP-Rule:MF_00954, ECO:0000269|PubMed:18760284, ECO:0000269|PubMed:8596442}. EcoCyc product frame: G6337-MONOMER. Genomic coordinates: 643557-643967. EcoCyc protein note: The Rnk protein was first identified as a regulator of NUCLEOSIDE-DIP-KIN-CPLX (Ndk) protein levels . Rnk shows sequence and structural similarity to the C terminal domain of the Gre factors and competes with the Gre factors and DksA for binding to core RNA polymerase in vitro. It may thus function as an anti-Gre factor in vivo, although this has not yet been shown . A mutation in rnk leads to a significant reduction in the level of Ndk . Overexpression of rnk suppresses the oxidative stress sensitivity caused by a rifampicin-resistant rpoB mutation; UTP, CTP, GTP, and ATP concentrations are restored to normal levels in the suppressed strain . A crystal structure of Rnk has been solved at 1.91 Å resolution . Expression of rnk is catabolite repressed . Rnk: "regulator of nucleoside diphosphate kinase"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFW4|protein.P0AFW4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002104,ECOCYC:G6337,GeneID:947546`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:643557-643967:-; feature_type=gene
