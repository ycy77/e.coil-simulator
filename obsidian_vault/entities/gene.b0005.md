---
entity_id: "gene.b0005"
entity_type: "gene"
name: "yaaX"
source_database: "NCBI RefSeq"
source_id: "gene-b0005"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0005"
  - "yaaX"
---

# yaaX

`gene.b0005`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0005`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yaaX (gene.b0005) is a gene entity. It encodes yaaX (protein.P75616). Encoded protein function: Uncharacterized protein YaaX EcoCyc product frame: G6081-MONOMER. Genomic coordinates: 5234-5530. EcoCyc protein note: No information about this protein was found by a literature search conducted on March 21, 2017.

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75616|protein.P75616]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000015,ECOCYC:G6081,GeneID:944747`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:5234-5530:+; feature_type=gene
