---
entity_id: "protein.P64550"
entity_type: "protein"
name: "alaE"
source_database: "UniProt"
source_id: "P64550"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00914, ECO:0000269|PubMed:21531828}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00914, ECO:0000269|PubMed:21531828}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "alaE ygaW b2670 JW2645"
---

# alaE

`protein.P64550`

## Static

- Type: `protein`
- Source: `UniProt:P64550`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00914, ECO:0000269|PubMed:21531828}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00914, ECO:0000269|PubMed:21531828}.

## Enriched Summary

FUNCTION: Exports L-alanine. {ECO:0000255|HAMAP-Rule:MF_00914, ECO:0000269|PubMed:21531828}.

## Biological Role

Component of L-alanine exporter (complex.ecocyc.CPLX0-8791).

## Annotation

FUNCTION: Exports L-alanine. {ECO:0000255|HAMAP-Rule:MF_00914, ECO:0000269|PubMed:21531828}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8791|complex.ecocyc.CPLX0-8791]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2670|gene.b2670]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P64550`
- `KEGG:ecj:JW2645;eco:b2670;ecoc:C3026_14715;`
- `GeneID:75172753;75205913;947147;`
- `GO:GO:0005886; GO:0015808; GO:0032973; GO:0033554; GO:0034639`

## Notes

L-alanine exporter AlaE
