---
entity_id: "gene.b1044"
entity_type: "gene"
name: "ymdA"
source_database: "NCBI RefSeq"
source_id: "gene-b1044"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1044"
  - "ymdA"
---

# ymdA

`gene.b1044`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1044`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ymdA (gene.b1044) is a gene entity. It encodes ymdA (protein.P75917). Encoded protein function: Uncharacterized protein YmdA EcoCyc product frame: G6549-MONOMER. Genomic coordinates: 1105414-1105725. EcoCyc protein note: Expression of YmdA is posttranscriptionally activated by CsrA. CsrA binds to two sites in the 5' UTR of ymdA; both binding sites are required to destabilize a hairpin structure that sequesters the ribosome binding site . Overexpression of YmdA inhibits biofilm formation . A ΔymdA strain shows a modest decrease in biofilm formation .

## Biological Role

Activated by csrA (protein.P69913).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75917|protein.P75917]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P69913|protein.P69913]] `RegulonDB|EcoCyc` `S` - regulator=CsrA; target=ymdA; function=+ | EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation

## External IDs

- `Dbxref:ASAP:ABE-0003545,ECOCYC:G6549,GeneID:949012`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1105414-1105725:+; feature_type=gene
