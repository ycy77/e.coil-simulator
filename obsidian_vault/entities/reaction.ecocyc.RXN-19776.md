---
entity_id: "reaction.ecocyc.RXN-19776"
entity_type: "reaction"
name: "RXN-19776"
source_database: "EcoCyc"
source_id: "RXN-19776"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19776

`reaction.ecocyc.RXN-19776`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19776`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

MENADIOL + HYDROGEN-PEROXIDE -> CPD-3766 + WATER; direction=REVERSIBLE EcoCyc reaction equation: MENADIOL + HYDROGEN-PEROXIDE -> CPD-3766 + WATER; direction=REVERSIBLE.

## Biological Role

Catalyzed by ccp (protein.P37197). Substrates: Hydrogen peroxide (molecule.C00027), menadiol (molecule.ecocyc.MENADIOL). Products: H2O (molecule.C00001), menadione (molecule.ecocyc.CPD-3766).

## Annotation

MENADIOL + HYDROGEN-PEROXIDE -> CPD-3766 + WATER; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P37197|protein.P37197]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-3766|molecule.ecocyc.CPD-3766]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.MENADIOL|molecule.ecocyc.MENADIOL]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19776`

## Notes

MENADIOL + HYDROGEN-PEROXIDE -> CPD-3766 + WATER; direction=REVERSIBLE
