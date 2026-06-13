---
entity_id: "protein.P46481"
entity_type: "protein"
name: "aaeB"
source_database: "UniProt"
source_id: "P46481"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aaeB yhcP b3240 JW3209"
---

# aaeB

`protein.P46481`

## Static

- Type: `protein`
- Source: `UniProt:P46481`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Forms an efflux pump with AaeA. Could function as a metabolic relief valve, allowing to eliminate certain compounds when they accumulate to high levels in the cell. Substrates are p-hydroxybenzoic acid (pHBA), 6-hydroxy-2-naphthoic and 2-hydroxycinnamate. {ECO:0000255|HAMAP-Rule:MF_01545, ECO:0000269|PubMed:15489430}.

## Biological Role

Component of aromatic carboxylic acid efflux pump (complex.ecocyc.CPLX0-4).

## Annotation

FUNCTION: Forms an efflux pump with AaeA. Could function as a metabolic relief valve, allowing to eliminate certain compounds when they accumulate to high levels in the cell. Substrates are p-hydroxybenzoic acid (pHBA), 6-hydroxy-2-naphthoic and 2-hydroxycinnamate. {ECO:0000255|HAMAP-Rule:MF_01545, ECO:0000269|PubMed:15489430}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-4|complex.ecocyc.CPLX0-4]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3240|gene.b3240]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P46481`
- `KEGG:ecj:JW3209;eco:b3240;`
- `GeneID:947747;`
- `GO:GO:0005886; GO:0022857; GO:0046942`

## Notes

p-hydroxybenzoic acid efflux pump subunit AaeB (pHBA efflux pump protein B)
