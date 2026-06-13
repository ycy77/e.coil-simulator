---
entity_id: "reaction.ecocyc.TRANS-RXN-68"
entity_type: "reaction"
name: "lysine:cadaverine antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-68"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# lysine:cadaverine antiport

`reaction.ecocyc.TRANS-RXN-68`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-68`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CADAVERINE + LYS -> CADAVERINE + LYS; direction=REVERSIBLE EcoCyc reaction equation: CADAVERINE + LYS -> CADAVERINE + LYS; direction=REVERSIBLE.

## Biological Role

Catalyzed by cadB (protein.P0AAE8). Substrates: L-Lysine (molecule.C00047), Cadaverine (molecule.C01672). Products: L-Lysine (molecule.C00047), Cadaverine (molecule.C01672).

## Annotation

CADAVERINE + LYS -> CADAVERINE + LYS; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AAE8|protein.P0AAE8]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00047|molecule.C00047]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01672|molecule.C01672]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00047|molecule.C00047]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01672|molecule.C01672]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-68`

## Notes

CADAVERINE + LYS -> CADAVERINE + LYS; direction=REVERSIBLE
