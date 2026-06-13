---
entity_id: "gene.b1671"
entity_type: "gene"
name: "ydhX"
source_database: "NCBI RefSeq"
source_id: "gene-b1671"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1671"
  - "ydhX"
---

# ydhX

`gene.b1671`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1671`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydhX (gene.b1671) is a gene entity. It encodes ydhX (protein.P77375). Encoded protein function: Uncharacterized ferredoxin-like protein YdhX EcoCyc product frame: G6899-MONOMER. Genomic coordinates: 1750345-1751013. EcoCyc protein note: YdhX is a predicted electron transfer protein . YdhX is located in the periplasm and can be transported by both the Tat and Sec pathways . Based on sequence similarity, the ydhYVWXUT operon may encode components of an oxidoreductase . A ydhY-T mutant does not show a growth defect under anaerobic conditions, although utilization of certain sources of sulfur is impaired .

## Biological Role

Repressed by narP (protein.P31802). Activated by fnr (protein.P0A9E5), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77375|protein.P77375]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=ydhX; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ydhX; function=+
- `represses` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `C` - regulator=NarP; target=ydhX; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005583,ECOCYC:G6899,GeneID:947308`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1750345-1751013:-; feature_type=gene
