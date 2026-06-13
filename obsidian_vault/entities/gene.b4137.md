---
entity_id: "gene.b4137"
entity_type: "gene"
name: "cutA"
source_database: "NCBI RefSeq"
source_id: "gene-b4137"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4137"
  - "cutA"
---

# cutA

`gene.b4137`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4137`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cutA (gene.b4137) is a gene entity. It encodes cutA (protein.P69488). Encoded protein function: FUNCTION: Involved in resistance toward heavy metals. {ECO:0000269|PubMed:7623666}. EcoCyc product frame: EG12177-MONOMER. EcoCyc synonyms: cutA1. Genomic coordinates: 4365018-4365356.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69488|protein.P69488]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cutA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013544,ECOCYC:EG12177,GeneID:948660`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4365018-4365356:-; feature_type=gene
