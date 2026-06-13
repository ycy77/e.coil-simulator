---
entity_id: "gene.b4199"
entity_type: "gene"
name: "yjfY"
source_database: "NCBI RefSeq"
source_id: "gene-b4199"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4199"
  - "yjfY"
---

# yjfY

`gene.b4199`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4199`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjfY (gene.b4199) is a gene entity. It encodes yjfY (protein.P0AF86). Encoded protein function: Uncharacterized protein YjfY EcoCyc product frame: G7861-MONOMER. Genomic coordinates: 4424516-4424791. EcoCyc protein note: No information about this protein was found by a literature search conducted on March 15, 2017.

## Biological Role

Repressed by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF86|protein.P0AF86]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=yjfY; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013736,ECOCYC:G7861,GeneID:948713`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4424516-4424791:-; feature_type=gene
