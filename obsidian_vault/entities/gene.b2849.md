---
entity_id: "gene.b2849"
entity_type: "gene"
name: "yqeK"
source_database: "NCBI RefSeq"
source_id: "gene-b2849"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2849"
  - "yqeK"
---

# yqeK

`gene.b2849`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2849`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yqeK (gene.b2849) is a gene entity. It encodes yqeK (protein.P77136). Encoded protein function: Uncharacterized protein YqeK EcoCyc product frame: G7469-MONOMER. Genomic coordinates: 2989935-2990360. EcoCyc protein note: yqeK is located within a remnant of an ETT2 (type III secretion system) pathogenicity island that is fully present in pathogenic strains such as E. coli O157:H7 and at least partially present in most sequenced E. coli and Shigella strains . ETT2 has been shown to contribute to pathogenesis .

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77136|protein.P77136]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yqeK; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009356,ECOCYC:G7469,GeneID:947329`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2989935-2990360:-; feature_type=gene
