---
entity_id: "gene.b2152"
entity_type: "gene"
name: "yeiB"
source_database: "NCBI RefSeq"
source_id: "gene-b2152"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2152"
  - "yeiB"
---

# yeiB

`gene.b2152`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2152`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yeiB (gene.b2152) is a gene entity. It encodes yeiB (protein.P25747). Encoded protein function: FUNCTION: Involved in transport. {ECO:0000305}. EcoCyc product frame: EG11290-MONOMER. Genomic coordinates: 2241810-2242967. EcoCyc protein note: No information about this protein was found by a literature search conducted on August 2, 2006.

## Biological Role

Repressed by sgrS (gene.b4577), metJ (protein.P0A8U6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25747|protein.P25747]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[gene.b4577|gene.b4577]] `RegulonDB` `S` - regulator=SgrS; target=yeiB; function=-
- `represses` <-- [[protein.P0A8U6|protein.P0A8U6]] `RegulonDB` `S` - regulator=MetJ; target=yeiB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007115,ECOCYC:EG11290,GeneID:949044`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2241810-2242967:-; feature_type=gene
