---
entity_id: "reaction.ecocyc.RXN-17009"
entity_type: "reaction"
name: "RXN-17009"
source_database: "EcoCyc"
source_id: "RXN-17009"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17009

`reaction.ecocyc.RXN-17009`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17009`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-10269 + CPD-18348 -> CPD-18351 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-10269 + CPD-18348 -> CPD-18351 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Palmitoleoyl-CoA (molecule.C21072), 1-cis-vaccenoyl-sn-glycerol-3-phosphate (molecule.ecocyc.CPD-18348). Products: CoA (molecule.C00010), 1-cis-vaccenoyl-2-palmitoleoyl-sn-glycerol-3-phosphate (molecule.ecocyc.CPD-18351).

## Annotation

CPD-10269 + CPD-18348 -> CPD-18351 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-18351|molecule.ecocyc.CPD-18351]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C21072|molecule.C21072]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-18348|molecule.ecocyc.CPD-18348]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17009`

## Notes

CPD-10269 + CPD-18348 -> CPD-18351 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
