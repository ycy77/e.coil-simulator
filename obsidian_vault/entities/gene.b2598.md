---
entity_id: "gene.b2598"
entity_type: "gene"
name: "pheL"
source_database: "NCBI RefSeq"
source_id: "gene-b2598"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2598"
  - "pheL"
---

# pheL

`gene.b2598`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2598`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pheL (gene.b2598) is a gene entity. It encodes pheL (protein.P0AD72). Encoded protein function: FUNCTION: This protein is involved in control of the biosynthesis of phenylalanine. EcoCyc product frame: EG11271-MONOMER. EcoCyc synonyms: pheAE. Genomic coordinates: 2737599-2737646. EcoCyc protein note: pheL includes a sequence that increases the frequency of ribosomal frameshifting. This frameshifting may in turn assist in the role of pheL as an attenuator for pheA .

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD72|protein.P0AD72]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pheL; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008543,ECOCYC:EG11271,GeneID:947080`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2737599-2737646:+; feature_type=gene
