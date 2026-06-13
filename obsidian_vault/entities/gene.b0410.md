---
entity_id: "gene.b0410"
entity_type: "gene"
name: "yajD"
source_database: "NCBI RefSeq"
source_id: "gene-b0410"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0410"
  - "yajD"
---

# yajD

`gene.b0410`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0410`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yajD (gene.b0410) is a gene entity. It encodes yajD (protein.P0AAQ2). Encoded protein function: Putative HNH nuclease YajD (EC 3.1.-.-) EcoCyc product frame: EG11097-MONOMER. Genomic coordinates: 430605-430952. EcoCyc protein note: No information about this protein was found by a literature search conducted on November 16, 2018.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAQ2|protein.P0AAQ2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yajD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001422,ECOCYC:EG11097,GeneID:945051`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:430605-430952:+; feature_type=gene
