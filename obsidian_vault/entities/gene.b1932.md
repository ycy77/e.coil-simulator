---
entity_id: "gene.b1932"
entity_type: "gene"
name: "yedL"
source_database: "NCBI RefSeq"
source_id: "gene-b1932"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1932"
  - "yedL"
---

# yedL

`gene.b1932`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1932`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yedL (gene.b1932) is a gene entity. It encodes yedL (protein.P76319). Encoded protein function: Uncharacterized N-acetyltransferase YedL (EC 2.3.1.-) EcoCyc product frame: G7040-MONOMER. Genomic coordinates: 2010600-2011079. EcoCyc protein note: Expression of yedL appears to be activated by NtrC via the G7072-MONOMER .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76319|protein.P76319]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yedL; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006433,ECOCYC:G7040,GeneID:946437`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2010600-2011079:+; feature_type=gene
