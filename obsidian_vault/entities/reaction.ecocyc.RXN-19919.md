---
entity_id: "reaction.ecocyc.RXN-19919"
entity_type: "reaction"
name: "RXN-19919"
source_database: "EcoCyc"
source_id: "RXN-19919"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19919

`reaction.ecocyc.RXN-19919`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19919`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD3O-0 + NAD -> CPD-21533 + NIACINAMIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD3O-0 + NAD -> CPD-21533 + NIACINAMIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: NAD+ (molecule.C00003), a [protein]-N6-acetyl-L-lysine (molecule.ecocyc.CPD3O-0). Products: Nicotinamide (molecule.C00153), a [protein]-N6-[1,1-(5-adenosylyl-α-D-ribose-1,2-di-O-yl)ethyl]-L-lysine (molecule.ecocyc.CPD-21533).

## Annotation

CPD3O-0 + NAD -> CPD-21533 + NIACINAMIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00153|molecule.C00153]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-21533|molecule.ecocyc.CPD-21533]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD3O-0|molecule.ecocyc.CPD3O-0]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19919`

## Notes

CPD3O-0 + NAD -> CPD-21533 + NIACINAMIDE; direction=PHYSIOL-LEFT-TO-RIGHT
