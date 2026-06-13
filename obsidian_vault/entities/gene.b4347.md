---
entity_id: "gene.b4347"
entity_type: "gene"
name: "symE"
source_database: "NCBI RefSeq"
source_id: "gene-b4347"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4347"
  - "symE"
---

# symE

`gene.b4347`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4347`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

symE (gene.b4347) is a gene entity. It encodes symE (protein.P39394). Encoded protein function: FUNCTION: Toxic component of a type I toxin-antitoxin (TA) system (PubMed:17462020). Involved in the degradation and recycling of damaged RNA (PubMed:17462020). It is itself a target for degradation by the ATP-dependent protease Lon (PubMed:17462020). {ECO:0000269|PubMed:17462020}. EcoCyc product frame: G7940-MONOMER. EcoCyc synonyms: yjiW, dinL, sosC. Genomic coordinates: 4579499-4579840.

## Biological Role

Repressed by lexA (protein.P0A7C2).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39394|protein.P39394]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A7C2|protein.P0A7C2]] `RegulonDB` `S` - regulator=LexA; target=symE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014253,ECOCYC:G7940,GeneID:949088`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4579499-4579840:-; feature_type=gene
