---
entity_id: "gene.b0513"
entity_type: "gene"
name: "ybbY"
source_database: "NCBI RefSeq"
source_id: "gene-b0513"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0513"
  - "ybbY"
---

# ybbY

`gene.b0513`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0513`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybbY (gene.b0513) is a gene entity. It encodes ybbY (protein.P77328). Encoded protein function: Putative purine permease YbbY EcoCyc product frame: G6282-MONOMER. EcoCyc synonyms: glxB4. Genomic coordinates: 540565-541866. EcoCyc protein note: YbbY is predicted to be an inner membrane protein with 11 transmembrane domains; topology analysis suggests the C-terminus is located in the cytoplasm . YbbY has sequence similarity to xanthine permease of Bacillus subtilis and to uracil permease of Bacillus caldolyticus . In the Transporter Classification Database, YbbY is a member of the nucleobase:cation symporter-2 (NCS2) family within the Amino Acid-Polyamine-Organocation (APC) superfamily .

## Biological Role

Repressed by allR (protein.P0ACN4).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77328|protein.P77328]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACN4|protein.P0ACN4]] `RegulonDB` `C` - regulator=AllR; target=ybbY; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001771,ECOCYC:G6282,GeneID:945131`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:540565-541866:+; feature_type=gene
