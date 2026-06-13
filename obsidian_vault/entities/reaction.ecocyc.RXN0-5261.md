---
entity_id: "reaction.ecocyc.RXN0-5261"
entity_type: "reaction"
name: "RXN0-5261"
source_database: "EcoCyc"
source_id: "RXN0-5261"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5261

`reaction.ecocyc.RXN0-5261`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5261`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PYRUVATE + PROTON + E- -> D-LACTATE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PYRUVATE + PROTON + E- -> D-LACTATE; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: Pyruvate (molecule.C00022), H+ (molecule.C00080). Products: (R)-Lactate (molecule.C00256).

## Annotation

PYRUVATE + PROTON + E- -> D-LACTATE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00256|molecule.C00256]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5261`

## Notes

PYRUVATE + PROTON + E- -> D-LACTATE; direction=LEFT-TO-RIGHT
