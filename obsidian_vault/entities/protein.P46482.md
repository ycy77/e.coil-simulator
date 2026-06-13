---
entity_id: "protein.P46482"
entity_type: "protein"
name: "aaeA"
source_database: "UniProt"
source_id: "P46482"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01544}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01544}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aaeA yhcQ b3241 JW3210"
---

# aaeA

`protein.P46482`

## Static

- Type: `protein`
- Source: `UniProt:P46482`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01544}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01544}.

## Enriched Summary

FUNCTION: Forms an efflux pump with AaeB. {ECO:0000255|HAMAP-Rule:MF_01544, ECO:0000269|PubMed:15489430}.

## Biological Role

Component of aromatic carboxylic acid efflux pump (complex.ecocyc.CPLX0-4).

## Annotation

FUNCTION: Forms an efflux pump with AaeB. {ECO:0000255|HAMAP-Rule:MF_01544, ECO:0000269|PubMed:15489430}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-4|complex.ecocyc.CPLX0-4]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3241|gene.b3241]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P46482`
- `KEGG:ecj:JW3210;eco:b3241;ecoc:C3026_17630;`
- `GeneID:75206091;947748;`
- `GO:GO:0005886; GO:0022857; GO:0046942; GO:0055085`

## Notes

p-hydroxybenzoic acid efflux pump subunit AaeA (pHBA efflux pump protein A)
