---
entity_id: "reaction.ecocyc.RXN0-6369"
entity_type: "reaction"
name: "RXN0-6369"
source_database: "EcoCyc"
source_id: "RXN0-6369"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6369

`reaction.ecocyc.RXN0-6369`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6369`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Ubiquinols + NITRATE -> Ubiquinones + WATER + NITRITE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Ubiquinols + NITRATE -> Ubiquinones + WATER + NITRITE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Nitrate (molecule.C00244), Ubiquinol (molecule.C00390). Products: H2O (molecule.C00001), Nitrite (molecule.C00088), a ubiquinone (molecule.ecocyc.Ubiquinones).

## Annotation

Ubiquinols + NITRATE -> Ubiquinones + WATER + NITRITE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00088|molecule.C00088]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Ubiquinones|molecule.ecocyc.Ubiquinones]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00244|molecule.C00244]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00390|molecule.C00390]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6369`

## Notes

Ubiquinols + NITRATE -> Ubiquinones + WATER + NITRITE; direction=PHYSIOL-LEFT-TO-RIGHT
