---
entity_id: "reaction.ecocyc.TREHALOSEPHOSPHA-RXN"
entity_type: "reaction"
name: "TREHALOSEPHOSPHA-RXN"
source_database: "EcoCyc"
source_id: "TREHALOSEPHOSPHA-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TREHALOSEPHOSPHA-RXN

`reaction.ecocyc.TREHALOSEPHOSPHA-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TREHALOSEPHOSPHA-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

TREHALOSE-6P + WATER -> TREHALOSE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: TREHALOSE-6P + WATER -> TREHALOSE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by otsB (protein.P31678). Substrates: H2O (molecule.C00001), alpha,alpha'-Trehalose 6-phosphate (molecule.C00689). Products: alpha,alpha-Trehalose (molecule.C01083), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.TRESYN-PWY` trehalose biosynthesis I (EcoCyc)

## Annotation

TREHALOSE-6P + WATER -> TREHALOSE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.TRESYN-PWY` trehalose biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P31678|protein.P31678]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01083|molecule.C01083]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00689|molecule.C00689]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TREHALOSEPHOSPHA-RXN`

## Notes

TREHALOSE-6P + WATER -> TREHALOSE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
