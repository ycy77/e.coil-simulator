---
entity_id: "gene.b0651"
entity_type: "gene"
name: "rihA"
source_database: "NCBI RefSeq"
source_id: "gene-b0651"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0651"
  - "rihA"
---

# rihA

`gene.b0651`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0651`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rihA (gene.b0651) is a gene entity. It encodes rihA (protein.P41409). Encoded protein function: FUNCTION: Hydrolyzes with equal efficiency cytidine or uridine to ribose and cytosine or uracil, respectively. EcoCyc product frame: G6358-MONOMER. EcoCyc synonyms: ybeK. Genomic coordinates: 683477-684412.

## Biological Role

Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P41409|protein.P41409]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=rihA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002227,ECOCYC:G6358,GeneID:945503`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:683477-684412:-; feature_type=gene
