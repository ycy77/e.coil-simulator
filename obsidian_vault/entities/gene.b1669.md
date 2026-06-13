---
entity_id: "gene.b1669"
entity_type: "gene"
name: "ydhT"
source_database: "NCBI RefSeq"
source_id: "gene-b1669"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1669"
  - "ydhT"
---

# ydhT

`gene.b1669`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1669`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydhT (gene.b1669) is a gene entity. It encodes ydhT (protein.P77147). Encoded protein function: Uncharacterized protein YdhT EcoCyc product frame: G6897-MONOMER. Genomic coordinates: 1748747-1749559. EcoCyc protein note: YdhT was hypothesized to be a redox enzyme maturation protein. Based on sequence similarity, the ydhYVWXUT operon may encode components of an oxidoreductase . A ydhY-T mutant does not show a growth defect under anaerobic conditions, although utilization of certain sources of sulfur is impaired .

## Biological Role

Repressed by narP (protein.P31802). Activated by fnr (protein.P0A9E5), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77147|protein.P77147]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=ydhT; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ydhT; function=+
- `represses` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `C` - regulator=NarP; target=ydhT; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005577,ECOCYC:G6897,GeneID:945960`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1748747-1749559:-; feature_type=gene
