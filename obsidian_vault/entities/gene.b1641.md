---
entity_id: "gene.b1641"
entity_type: "gene"
name: "slyB"
source_database: "NCBI RefSeq"
source_id: "gene-b1641"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1641"
  - "slyB"
---

# slyB

`gene.b1641`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1641`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

slyB (gene.b1641) is a gene entity. It encodes slyB (protein.P0A905). Encoded protein function: Outer membrane lipoprotein SlyB EcoCyc product frame: G6881-MONOMER. Genomic coordinates: 1719876-1720343. EcoCyc protein note: Expression analysis shows slyB expression is repressed in the presence of high concentrations of extracellular Mg2+. This repression is dependent upon PhoP and PhoQ. DNase I footprinting assays show slyB is directly regulated by PhoP . A mutant constitutively expressing the EvgA/EvgS two-component system had increased expression of slyB through PhoPQ, though enhanced expression of phoP alone failed to increase expression of slyB . Proteomic analysis of membrane preparations suggests that SlyB forms a homo-oligomeric complex .

## Biological Role

Repressed by phoP (protein.P23836). Activated by phoP (protein.P23836).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A905|protein.P0A905]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P23836|protein.P23836]] `RegulonDB` `S` - regulator=PhoP; target=slyB; function=-+
- `represses` <-- [[protein.P23836|protein.P23836]] `RegulonDB` `S` - regulator=PhoP; target=slyB; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0005493,ECOCYC:G6881,GeneID:946801`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1719876-1720343:+; feature_type=gene
