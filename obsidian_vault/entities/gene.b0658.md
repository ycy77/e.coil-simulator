---
entity_id: "gene.b0658"
entity_type: "gene"
name: "ybeX"
source_database: "NCBI RefSeq"
source_id: "gene-b0658"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0658"
  - "ybeX"
---

# ybeX

`gene.b0658`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0658`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybeX (gene.b0658) is a gene entity. It encodes corC (protein.P0AE78). Encoded protein function: FUNCTION: Plays a role in the transport of magnesium and cobalt ions. {ECO:0000250}. EcoCyc product frame: G6361-MONOMER. Genomic coordinates: 690906-691784. EcoCyc protein note: No information about this protein was found in a literature search on 3/30/2017

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE78|protein.P0AE78]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=ybeX; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002252,ECOCYC:G6361,GeneID:946417`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:690906-691784:-; feature_type=gene
