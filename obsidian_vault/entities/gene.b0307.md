---
entity_id: "gene.b0307"
entity_type: "gene"
name: "ykgF"
source_database: "NCBI RefSeq"
source_id: "gene-b0307"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0307"
  - "ykgF"
---

# ykgF

`gene.b0307`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0307`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ykgF (gene.b0307) is a gene entity. It encodes ykgF (protein.P77536). Encoded protein function: Uncharacterized electron transport protein YkgF EcoCyc product frame: G6177-MONOMER. Genomic coordinates: 322338-323765. EcoCyc protein note: While their physiological role in E. coli remains unknown, the ykgEFG genes are homologous to newly identified lactate utilization genes in Shewanella oneidensis. Low-copy expression of E. coli ykgEFG in S. oneidensis complements the ability of the Δdld-II ΔlldF double mutant for growth on L-lactate, but not D-lactate . Overexpression of ykgEFG in E. coli restores the ability of a EG10231 dld mutant to grow on D-lactate; crude extracts of an overexpressing strain contain elevated levels of both L- and D-lactate dehydrogenase activity . A ykgF insertion mutant is still able to utilize L-lactate as the sole source of carbon . However, a quadruple null mutant strain (ΔlldD dld glcD ykgF) is unable to grow on L- or D-lactate .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77536|protein.P77536]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001060,ECOCYC:G6177,GeneID:944980`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:322338-323765:+; feature_type=gene
