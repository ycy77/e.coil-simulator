---
entity_id: "gene.b3866"
entity_type: "gene"
name: "yihI"
source_database: "NCBI RefSeq"
source_id: "gene-b3866"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3866"
  - "yihI"
---

# yihI

`gene.b3866`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3866`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yihI (gene.b3866) is a gene entity. It encodes yihI (protein.P0A8H6). Encoded protein function: FUNCTION: A GTPase-activating protein (GAP) that modifies Der/EngA GTPase function, negatively regulating cell growth, probably via ribosome assembly. Stimulates the GTPase activity of Der; a construct missing the first 45 residues is even more stimulatory. Does not stimulate 2 other GTPases (ObgE and Era). Overexpression inhibits cell growth; precursor 16S rRNA accumulates, the 23S rRNA is 6-7 bases longer than usual, and 50S ribosomal subunits are improperly assembled, leading to 45S subunits lacking proteins L9, L18 and L25. Overexpression of Der in the same cells suppresses the 50S subunit assembly defect, corroborating that YihI and Der interact. {ECO:0000269|PubMed:20434458}. EcoCyc product frame: EG11835-MONOMER. Genomic coordinates: 4051347-4051856.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8H6|protein.P0A8H6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yihI; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012626,ECOCYC:EG11835,GeneID:948363`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4051347-4051856:+; feature_type=gene
