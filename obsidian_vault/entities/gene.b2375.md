---
entity_id: "gene.b2375"
entity_type: "gene"
name: "yfdX"
source_database: "NCBI RefSeq"
source_id: "gene-b2375"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2375"
  - "yfdX"
---

# yfdX

`gene.b2375`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2375`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfdX (gene.b2375) is a gene entity. It encodes yfdX (protein.P76520). Encoded protein function: Protein YfdX EcoCyc product frame: G7238-MONOMER. Genomic coordinates: 2493767-2494402. EcoCyc protein note: Expression of YfdX is induced by overexpression of the EvgA response regulator of the EvgAS two-component signal transduction system . Expression of yfdX increases at the onset of stationary phase . Deletion of yfdXWUVE slightly decreases acid resistance .

## Biological Role

Activated by evgA (protein.P0ACZ4).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76520|protein.P76520]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACZ4|protein.P0ACZ4]] `RegulonDB` `S` - regulator=EvgA; target=yfdX; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007835,ECOCYC:G7238,GeneID:949108`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2493767-2494402:-; feature_type=gene
