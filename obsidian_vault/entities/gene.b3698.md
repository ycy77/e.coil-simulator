---
entity_id: "gene.b3698"
entity_type: "gene"
name: "yidB"
source_database: "NCBI RefSeq"
source_id: "gene-b3698"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3698"
  - "yidB"
---

# yidB

`gene.b3698`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3698`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yidB (gene.b3698) is a gene entity. It encodes yidB (protein.P09996). Encoded protein function: Uncharacterized protein YidB EcoCyc product frame: EG11196-MONOMER. Genomic coordinates: 3877067-3877465. EcoCyc protein note: No information about this protein was found by a literature search conducted on November 7, 2018.

## Biological Role

Activated by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09996|protein.P09996]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=yidB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012089,ECOCYC:EG11196,GeneID:948212`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3877067-3877465:-; feature_type=gene
