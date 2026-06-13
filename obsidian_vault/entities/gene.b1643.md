---
entity_id: "gene.b1643"
entity_type: "gene"
name: "ydhI"
source_database: "NCBI RefSeq"
source_id: "gene-b1643"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1643"
  - "ydhI"
---

# ydhI

`gene.b1643`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1643`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydhI (gene.b1643) is a gene entity. It encodes ydhI (protein.P64471). Encoded protein function: Uncharacterized protein YdhI EcoCyc product frame: G6883-MONOMER. Genomic coordinates: 1721025-1721261. EcoCyc protein note: In the Transporter Classification Database, YdhI (from E. coli O7:K1 str. CE10) is an uncharacterized member of the The Putative Auxiliary Aromatic Acid Exporter (AaeX) Family .The protein sequence is identical to that of YdhI from E. coli MG1655.

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64471|protein.P64471]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=ydhI; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005499,ECOCYC:G6883,GeneID:947559`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1721025-1721261:+; feature_type=gene
