---
entity_id: "gene.b1668"
entity_type: "gene"
name: "ydhS"
source_database: "NCBI RefSeq"
source_id: "gene-b1668"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1668"
  - "ydhS"
---

# ydhS

`gene.b1668`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1668`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydhS (gene.b1668) is a gene entity. It encodes ydhS (protein.P77148). Encoded protein function: Uncharacterized protein YdhS EcoCyc product frame: G6896-MONOMER. Genomic coordinates: 1747131-1748735. EcoCyc protein note: No information about this protein was found by a literature search conducted on February 9, 2017.

## Biological Role

Repressed by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77148|protein.P77148]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=ydhS; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005575,ECOCYC:G6896,GeneID:945786`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1747131-1748735:+; feature_type=gene
