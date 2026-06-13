---
entity_id: "gene.b0868"
entity_type: "gene"
name: "ybjS"
source_database: "NCBI RefSeq"
source_id: "gene-b0868"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0868"
  - "ybjS"
---

# ybjS

`gene.b0868`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0868`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybjS (gene.b0868) is a gene entity. It encodes ybjS (protein.P75821). Encoded protein function: Uncharacterized protein YbjS EcoCyc product frame: G6453-MONOMER. Genomic coordinates: 905740-906753. EcoCyc protein note: No information about this protein was found by a literature search conducted on July 6, 2020.

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75821|protein.P75821]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=ybjS; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002949,ECOCYC:G6453,GeneID:945495`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:905740-906753:-; feature_type=gene
