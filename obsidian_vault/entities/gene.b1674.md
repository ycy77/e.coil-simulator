---
entity_id: "gene.b1674"
entity_type: "gene"
name: "ydhY"
source_database: "NCBI RefSeq"
source_id: "gene-b1674"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1674"
  - "ydhY"
---

# ydhY

`gene.b1674`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1674`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydhY (gene.b1674) is a gene entity. It encodes ydhY (protein.P0AAL6). Encoded protein function: Uncharacterized ferredoxin-like protein YdhY EcoCyc product frame: G6902-MONOMER. Genomic coordinates: 1753851-1754477. EcoCyc protein note: YdhY is a predicted ferredoxin-like protein. Based on sequence similarity, the ydhYVWXUT operon may encode components of an oxidoreductase . Expression of ydhY is increased under anaerobic growth conditions, dependent on FNR , and repressed by nitrate and nitrite . Expression of ydhY displayed significantly lower variability across populations adapted to different toxins . A ydhY-T mutant does not show a growth defect under anaerobic conditions, although utilization of certain sources of sulfur is impaired .

## Biological Role

Repressed by narP (protein.P31802). Activated by fnr (protein.P0A9E5), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAL6|protein.P0AAL6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=ydhY; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ydhY; function=+
- `represses` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `C` - regulator=NarP; target=ydhY; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005589,ECOCYC:G6902,GeneID:948749`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1753851-1754477:-; feature_type=gene
