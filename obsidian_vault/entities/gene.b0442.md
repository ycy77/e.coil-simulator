---
entity_id: "gene.b0442"
entity_type: "gene"
name: "ybaV"
source_database: "NCBI RefSeq"
source_id: "gene-b0442"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0442"
  - "ybaV"
---

# ybaV

`gene.b0442`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0442`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybaV (gene.b0442) is a gene entity. It encodes ybaV (protein.P0AAR8). Encoded protein function: Uncharacterized protein YbaV EcoCyc product frame: G6243-MONOMER. EcoCyc synonyms: comEA. Genomic coordinates: 463937-464308. EcoCyc protein note: ybaV was recognised in a screen designed to identify genes that are involved in repressing cell-to-cell plasmid transfer in E. coli K-12 . YbaV contains an N-terminal signal peptide and is predicted to be located in the periplasm. YbaV contains two helix-hairpin-helix motifs that are predicted to be involved in DNA binding . YbaV may sequster DNA in the periplasm and repress transformation . ybaV shows homology to comEA - an integral membrane protein required for transformation in Bacillus subtilis .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAR8|protein.P0AAR8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001534,ECOCYC:G6243,GeneID:945884`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:463937-464308:+; feature_type=gene
