---
entity_id: "reaction.ecocyc.RXN0-7325"
entity_type: "reaction"
name: "RXN0-7325"
source_database: "EcoCyc"
source_id: "RXN0-7325"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7325

`reaction.ecocyc.RXN0-7325`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7325`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

COPROPORPHYRINOGEN_III + HYDROGEN-PEROXIDE -> COPROPORPHYRIN_III + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: COPROPORPHYRINOGEN_III + HYDROGEN-PEROXIDE -> COPROPORPHYRIN_III + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yfeX (protein.P76536). Substrates: Hydrogen peroxide (molecule.C00027), Coproporphyrinogen III (molecule.C03263). Products: H2O (molecule.C00001), Coproporphyrin III (molecule.C05770).

## Annotation

COPROPORPHYRINOGEN_III + HYDROGEN-PEROXIDE -> COPROPORPHYRIN_III + WATER; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P76536|protein.P76536]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05770|molecule.C05770]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03263|molecule.C03263]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7325`

## Notes

COPROPORPHYRINOGEN_III + HYDROGEN-PEROXIDE -> COPROPORPHYRIN_III + WATER; direction=LEFT-TO-RIGHT
