---
entity_id: "gene.b3446"
entity_type: "gene"
name: "yrhB"
source_database: "NCBI RefSeq"
source_id: "gene-b3446"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3446"
  - "yrhB"
---

# yrhB

`gene.b3446`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3446`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yrhB (gene.b3446) is a gene entity. It encodes yrhB (protein.P46857). Encoded protein function: Uncharacterized protein YrhB EcoCyc product frame: G7763-MONOMER. Genomic coordinates: 3584759-3585043. EcoCyc protein note: YrhB from E. coli BL21 has been characterized: a yrhB-deficient mutant is more sensitive to heat shock (48°C) than wild type, and YrhB shows chaperone-like function in vitro .

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P46857|protein.P46857]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yrhB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011255,ECOCYC:G7763,GeneID:947948`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3584759-3585043:+; feature_type=gene
