---
entity_id: "gene.b4685"
entity_type: "gene"
name: "yrbN"
source_database: "NCBI RefSeq"
source_id: "gene-b4685"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4685"
  - "yrbN"
---

# yrbN

`gene.b4685`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4685`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yrbN (gene.b4685) is a gene entity. It encodes yrbN (protein.C1P618). Encoded protein function: Uncharacterized protein YrbN EcoCyc product frame: MONOMER0-2878. Genomic coordinates: 3307853-3307933. EcoCyc protein note: The YrbN open reading frame was predicted based on sequence similarity to a number of other enteric bacteria. YrbN is expressed during exponential growth .

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.C1P618|protein.C1P618]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yrbN; function=+

## External IDs

- `Dbxref:ASAP:ABE-0285228,ECOCYC:G0-10651,GeneID:7751619`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3307853-3307933:-; feature_type=gene
