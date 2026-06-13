---
entity_id: "gene.b1672"
entity_type: "gene"
name: "ydhW"
source_database: "NCBI RefSeq"
source_id: "gene-b1672"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1672"
  - "ydhW"
---

# ydhW

`gene.b1672`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1672`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydhW (gene.b1672) is a gene entity. It encodes ydhW (protein.P77564). Encoded protein function: Uncharacterized protein YdhW EcoCyc product frame: G6900-MONOMER. Genomic coordinates: 1751077-1751724. EcoCyc protein note: YdhW was hypothesized to be a redox enzyme maturation protein. Based on sequence similarity, the ydhYVWXUT operon may encode components of an oxidoreductase . A ydhY-T mutant does not show a growth defect under anaerobic conditions, although utilization of certain sources of sulfur is impaired .

## Biological Role

Repressed by narP (protein.P31802). Activated by fnr (protein.P0A9E5), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77564|protein.P77564]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=ydhW; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ydhW; function=+
- `represses` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `C` - regulator=NarP; target=ydhW; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005585,ECOCYC:G6900,GeneID:947180`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1751077-1751724:-; feature_type=gene
