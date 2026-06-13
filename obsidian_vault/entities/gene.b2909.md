---
entity_id: "gene.b2909"
entity_type: "gene"
name: "ygfB"
source_database: "NCBI RefSeq"
source_id: "gene-b2909"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2909"
  - "ygfB"
---

# ygfB

`gene.b2909`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2909`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygfB (gene.b2909) is a gene entity. It encodes ygfB (protein.P0A8C4). Encoded protein function: UPF0149 protein YgfB EcoCyc product frame: EG11323-MONOMER. Genomic coordinates: 3054866-3055444. EcoCyc protein note: No information about this protein was found by a literature search conducted on November 16, 2020. Using a method that distinguishes N-phosphorylation from O-phosphorylation, N-phosphorylation was detected in vitro .

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8C4|protein.P0A8C4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ygfB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009551,ECOCYC:EG11323,GeneID:947400`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3054866-3055444:-; feature_type=gene
