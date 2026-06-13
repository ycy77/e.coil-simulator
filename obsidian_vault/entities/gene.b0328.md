---
entity_id: "gene.b0328"
entity_type: "gene"
name: "yahN"
source_database: "NCBI RefSeq"
source_id: "gene-b0328"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0328"
  - "yahN"
---

# yahN

`gene.b0328`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0328`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yahN (gene.b0328) is a gene entity. It encodes yahN (protein.P75693). Encoded protein function: Uncharacterized membrane protein YahN EcoCyc product frame: G6193-MONOMER. Genomic coordinates: 345666-346337. EcoCyc protein note: YahN is homologous to RhtB - a likely homoserine/homoserine lactone exporter in E. coli K-12 YahN is a member of the Resistance to Homoserine/Threonine (RhtB) family . The global regulator Lrp regulates yahN expression .

## Biological Role

Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75693|protein.P75693]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=yahN; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001122,ECOCYC:G6193,GeneID:944968`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:345666-346337:-; feature_type=gene
