---
entity_id: "gene.b2271"
entity_type: "gene"
name: "yfbL"
source_database: "NCBI RefSeq"
source_id: "gene-b2271"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2271"
  - "yfbL"
---

# yfbL

`gene.b2271`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2271`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfbL (gene.b2271) is a gene entity. It encodes yfbL (protein.P76482). Encoded protein function: Uncharacterized protein YfbL EcoCyc product frame: G7178-MONOMER. Genomic coordinates: 2385860-2386831. EcoCyc protein note: No information about this protein was found by a literature search conducted on August 16, 2018.

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76482|protein.P76482]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yfbL; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007506,ECOCYC:G7178,GeneID:945832`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2385860-2386831:+; feature_type=gene
