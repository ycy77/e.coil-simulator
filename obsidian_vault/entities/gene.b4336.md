---
entity_id: "gene.b4336"
entity_type: "gene"
name: "yjiN"
source_database: "NCBI RefSeq"
source_id: "gene-b4336"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4336"
  - "yjiN"
---

# yjiN

`gene.b4336`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4336`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjiN (gene.b4336) is a gene entity. It encodes yjiN (protein.P39385). Encoded protein function: Uncharacterized protein YjiN EcoCyc product frame: G7933-MONOMER. Genomic coordinates: 4565966-4567246. EcoCyc protein note: YjiN is implicated in the uptake of proline-rich antimicrobial peptides (PrAMPS) in cells lacking the peptide uptake permease, CPLX0-8097 "SbmA" .

## Biological Role

Activated by slyA (protein.P0A8W2).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39385|protein.P39385]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=yjiN; function=+

## External IDs

- `Dbxref:ASAP:ABE-0014219,ECOCYC:G7933,GeneID:948860`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4565966-4567246:-; feature_type=gene
