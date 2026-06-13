---
entity_id: "reaction.ecocyc.RXN-17011"
entity_type: "reaction"
name: "RXN-17011"
source_database: "EcoCyc"
source_id: "RXN-17011"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17011

`reaction.ecocyc.RXN-17011`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17011`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-18346 + CPD-18348 -> CPD-18353 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-18346 + CPD-18348 -> CPD-18353 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: cis-Vaccenoyl-CoA (molecule.C21945), 1-cis-vaccenoyl-sn-glycerol-3-phosphate (molecule.ecocyc.CPD-18348). Products: CoA (molecule.C00010), 1,2-bis-cis-vaccenoyl-phosphatidate (molecule.ecocyc.CPD-18353).

## Annotation

CPD-18346 + CPD-18348 -> CPD-18353 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-18353|molecule.ecocyc.CPD-18353]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C21945|molecule.C21945]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-18348|molecule.ecocyc.CPD-18348]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17011`

## Notes

CPD-18346 + CPD-18348 -> CPD-18353 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
