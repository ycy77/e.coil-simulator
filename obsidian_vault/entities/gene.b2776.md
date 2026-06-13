---
entity_id: "gene.b2776"
entity_type: "gene"
name: "ygcE"
source_database: "NCBI RefSeq"
source_id: "gene-b2776"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2776"
  - "ygcE"
---

# ygcE

`gene.b2776`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2776`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygcE (gene.b2776) is a gene entity. It encodes ygcE (protein.P55138). Encoded protein function: Uncharacterized sugar kinase YgcE (EC 2.7.1.-) EcoCyc product frame: G7442-MONOMER. Genomic coordinates: 2901896-2903374. EcoCyc protein note: No information about this protein was found by a literature search conducted on February 24, 2017.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P55138|protein.P55138]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ygcE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009097,ECOCYC:G7442,GeneID:946193`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2901896-2903374:+; feature_type=gene
