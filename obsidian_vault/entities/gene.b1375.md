---
entity_id: "gene.b1375"
entity_type: "gene"
name: "ynaE"
source_database: "NCBI RefSeq"
source_id: "gene-b1375"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1375"
  - "ynaE"
---

# ynaE

`gene.b1375`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1375`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ynaE (gene.b1375) is a gene entity. It encodes ynaE (protein.P76073). Encoded protein function: Uncharacterized protein YnaE EcoCyc product frame: G6698-MONOMER. Genomic coordinates: 1433991-1434224. EcoCyc protein note: The 5' UTR of ynaE is similar to that of ydfK . Expression of both genes is upregulated by cold shock .

## Biological Role

Repressed by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76073|protein.P76073]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=ynaE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004602,ECOCYC:G6698,GeneID:946078`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1433991-1434224:-; feature_type=gene
