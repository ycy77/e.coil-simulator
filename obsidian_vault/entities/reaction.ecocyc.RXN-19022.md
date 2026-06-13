---
entity_id: "reaction.ecocyc.RXN-19022"
entity_type: "reaction"
name: "RXN-19022"
source_database: "EcoCyc"
source_id: "RXN-19022"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19022

`reaction.ecocyc.RXN-19022`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19022`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-GLUTAMATE-5-P -> 5-OXOPROLINE + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-GLUTAMATE-5-P -> 5-OXOPROLINE + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: L-Glutamyl 5-phosphate (molecule.C03287). Products: H+ (molecule.C00080), 5-Oxoproline (molecule.C01879), phosphate (molecule.ecocyc.Pi).

## Annotation

L-GLUTAMATE-5-P -> 5-OXOPROLINE + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01879|molecule.C01879]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C03287|molecule.C03287]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19022`

## Notes

L-GLUTAMATE-5-P -> 5-OXOPROLINE + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
