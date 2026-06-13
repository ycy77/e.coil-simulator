---
entity_id: "gene.b0601"
entity_type: "gene"
name: "ybdM"
source_database: "NCBI RefSeq"
source_id: "gene-b0601"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0601"
  - "ybdM"
---

# ybdM

`gene.b0601`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0601`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybdM (gene.b0601) is a gene entity. It encodes ybdM (protein.P77174). Encoded protein function: Uncharacterized protein YbdM EcoCyc product frame: G6330-MONOMER. Genomic coordinates: 634747-635376. EcoCyc protein note: No information about this protein was found by a literature search conducted on March 21, 2017.

## Biological Role

Repressed by ybdO (protein.P77746).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77174|protein.P77174]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P77746|protein.P77746]] `RegulonDB` `S` - regulator=CitR; target=ybdM; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002071,ECOCYC:G6330,GeneID:945206`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:634747-635376:-; feature_type=gene
