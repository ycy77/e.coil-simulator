---
entity_id: "gene.b1503"
entity_type: "gene"
name: "ydeR"
source_database: "NCBI RefSeq"
source_id: "gene-b1503"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1503"
  - "ydeR"
---

# ydeR

`gene.b1503`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1503`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydeR (gene.b1503) is a gene entity. It encodes ydeR (protein.P77294). Encoded protein function: Uncharacterized fimbrial-like protein YdeR EcoCyc product frame: G6793-MONOMER. Genomic coordinates: 1587793-1588296. EcoCyc protein note: E. coli K-12 contains 12 chaperone-usher fimbrial operons, including ydeQRST; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77294|protein.P77294]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005008,ECOCYC:G6793,GeneID:946049`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1587793-1588296:-; feature_type=gene
