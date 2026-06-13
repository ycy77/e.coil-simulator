---
entity_id: "gene.b1089"
entity_type: "gene"
name: "rpmF"
source_database: "NCBI RefSeq"
source_id: "gene-b1089"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1089"
  - "rpmF"
---

# rpmF

`gene.b1089`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1089`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpmF (gene.b1089) is a gene entity. It encodes rpmF (protein.P0A7N4). Encoded protein function: Large ribosomal subunit protein bL32 (50S ribosomal protein L32) EcoCyc product frame: EG10890-MONOMER. Genomic coordinates: 1147367-1147540. EcoCyc protein note: The L32 protein is a non-essential component of the 50S subunit of the ribosome. L32 was found to crosslink to L17 and does not appear to be exposed on the ribosomal surface . L32 assembles late in the process and does not bind rRNA by itself , but can be crosslinked to nucleotides 2878-90 within 23S rRNA . L32 is located within 21 Å of nucleotide C2475 of 23S rRNA, near the peptidyltransferase center . In a ΔrpmF mutant, exposure to hydroxyurea leads to an increased membrane stress response and increased generation of reactive oxygen species . The Keio collection rpmF mutant is sensitive to lithium (<90% growth at 200mM Li) .

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7N4|protein.P0A7N4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003686,ECOCYC:EG10890,GeneID:945657`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1147367-1147540:+; feature_type=gene
