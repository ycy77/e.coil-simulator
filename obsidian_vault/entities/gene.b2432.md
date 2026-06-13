---
entity_id: "gene.b2432"
entity_type: "gene"
name: "yfeY"
source_database: "NCBI RefSeq"
source_id: "gene-b2432"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2432"
  - "yfeY"
---

# yfeY

`gene.b2432`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2432`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfeY (gene.b2432) is a gene entity. It encodes yfeY (protein.P76537). Encoded protein function: Uncharacterized protein YfeY EcoCyc product frame: G7267-MONOMER. Genomic coordinates: 2550641-2551216. EcoCyc protein note: YfeY is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ). YfeY is a member of the σE regulon .

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76537|protein.P76537]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=yfeY; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008017,ECOCYC:G7267,GeneID:946919`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2550641-2551216:-; feature_type=gene
