---
entity_id: "gene.b3427"
entity_type: "gene"
name: "yzgL"
source_database: "NCBI RefSeq"
source_id: "gene-b3427"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3427"
  - "yzgL"
---

# yzgL

`gene.b3427`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3427`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yzgL (gene.b3427) is a gene entity. It encodes yzgL (protein.P76692). Encoded protein function: Protein YzgL EcoCyc product frame: G7752-MONOMER. Genomic coordinates: 3563724-3564005. EcoCyc protein note: No information about this protein was found by a literature search conducted on July 9, 2018.

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76692|protein.P76692]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=yzgL; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011194,ECOCYC:G7752,GeneID:947933`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3563724-3564005:-; feature_type=gene
