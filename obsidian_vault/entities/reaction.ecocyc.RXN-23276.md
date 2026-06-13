---
entity_id: "reaction.ecocyc.RXN-23276"
entity_type: "reaction"
name: "RXN-23276"
source_database: "EcoCyc"
source_id: "RXN-23276"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23276

`reaction.ecocyc.RXN-23276`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23276`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NITRIC-OXIDE + SUPER-OXIDE -> CPD0-1395; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: NITRIC-OXIDE + SUPER-OXIDE -> CPD0-1395; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Nitric oxide (molecule.C00533), superoxide (molecule.ecocyc.SUPER-OXIDE). Products: peroxynitrite (molecule.ecocyc.CPD0-1395).

## Annotation

NITRIC-OXIDE + SUPER-OXIDE -> CPD0-1395; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.ecocyc.CPD0-1395|molecule.ecocyc.CPD0-1395]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00533|molecule.C00533]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.SUPER-OXIDE|molecule.ecocyc.SUPER-OXIDE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23276`

## Notes

NITRIC-OXIDE + SUPER-OXIDE -> CPD0-1395; direction=PHYSIOL-LEFT-TO-RIGHT
