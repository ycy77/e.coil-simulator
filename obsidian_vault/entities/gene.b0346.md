---
entity_id: "gene.b0346"
entity_type: "gene"
name: "mhpR"
source_database: "NCBI RefSeq"
source_id: "gene-b0346"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0346"
  - "mhpR"
---

# mhpR

`gene.b0346`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0346`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mhpR (gene.b0346) is a gene entity. It encodes mhpR (protein.P77569). Encoded protein function: FUNCTION: Activator of the mhpABCDFE operon coding for components of the 3-hydroxyphenylpropionate degradation pathway. {ECO:0000269|PubMed:9098055}. EcoCyc product frame: G6201-MONOMER. Genomic coordinates: 367587-368420.

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77569|protein.P77569]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mhpR; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=mhpR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001191,ECOCYC:G6201,GeneID:945938`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:367587-368420:-; feature_type=gene
