---
entity_id: "gene.b1974"
entity_type: "gene"
name: "yodB"
source_database: "NCBI RefSeq"
source_id: "gene-b1974"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1974"
  - "yodB"
---

# yodB

`gene.b1974`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1974`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yodB (gene.b1974) is a gene entity. It encodes yodB (protein.P76345). Encoded protein function: Cytochrome b561 homolog 1 EcoCyc product frame: G7062-MONOMER. Genomic coordinates: 2042368-2042898. EcoCyc protein note: YodB is a cytoplasmic membrane protein with four predicted transmembrane helices. The C terminus is cytoplasmic .

## Biological Role

Activated by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76345|protein.P76345]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=yodB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006552,ECOCYC:G7062,GeneID:946491`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2042368-2042898:+; feature_type=gene
