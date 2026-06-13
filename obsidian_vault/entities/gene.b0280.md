---
entity_id: "gene.b0280"
entity_type: "gene"
name: "yagN"
source_database: "NCBI RefSeq"
source_id: "gene-b0280"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0280"
  - "yagN"
---

# yagN

`gene.b0280`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0280`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yagN (gene.b0280) is a gene entity. It encodes yagN (protein.P71297). Encoded protein function: Uncharacterized protein YagN EcoCyc product frame: G6151-MONOMER. Genomic coordinates: 295139-295579. EcoCyc protein note: YagN contains a stretch of alternating acidic and proline residues, a ribosome-destabilizing sequence. Translation of YagN, both in a cell-free system and in vivo, yields an incomplete polypeptidyl-tRNA species that is cleaved by Pth . Ribosome-profiling data show a drop in ribosome occupancy at the ribosome-destabilizing sequence .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P71297|protein.P71297]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000976,ECOCYC:G6151,GeneID:945349`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:295139-295579:-; feature_type=gene
