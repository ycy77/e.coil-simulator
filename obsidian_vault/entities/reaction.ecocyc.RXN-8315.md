---
entity_id: "reaction.ecocyc.RXN-8315"
entity_type: "reaction"
name: "RXN-8315"
source_database: "EcoCyc"
source_id: "RXN-8315"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-8315

`reaction.ecocyc.RXN-8315`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8315`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + SO3 -> HSO3; direction=REVERSIBLE EcoCyc reaction equation: PROTON + SO3 -> HSO3; direction=REVERSIBLE.

## Biological Role

Substrates: H+ (molecule.C00080), Sulfite (molecule.C00094). Products: HSO3- (molecule.C11481).

## Annotation

PROTON + SO3 -> HSO3; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C11481|molecule.C11481]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00094|molecule.C00094]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8315`

## Notes

PROTON + SO3 -> HSO3; direction=REVERSIBLE
