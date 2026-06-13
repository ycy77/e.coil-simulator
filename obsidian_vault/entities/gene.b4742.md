---
entity_id: "gene.b4742"
entity_type: "gene"
name: "ymjE"
source_database: "NCBI RefSeq"
source_id: "gene-b4742"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4742"
  - "ymjE"
---

# ymjE

`gene.b4742`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4742`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ymjE (gene.b4742) is a gene entity. It encodes ymjE (protein.P0DPO2). Encoded protein function: Protein YmjE EcoCyc product frame: MONOMER0-4419. Genomic coordinates: 1359177-1359341. EcoCyc protein note: YmjE was identified as a previously unannotated small protein that is expressed at approximately equal levels during exponential growth and stationary phase in rich growth medium .

## Biological Role

Repressed by puuR (protein.P0A9U6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DPO2|protein.P0DPO2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9U6|protein.P0A9U6]] `RegulonDB` `S` - regulator=PuuR; target=ymjE; function=-

## External IDs

- `Dbxref:ECOCYC:G0-16737,GeneID:38094954`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1359177-1359341:-; feature_type=gene
