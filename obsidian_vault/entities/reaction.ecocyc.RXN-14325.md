---
entity_id: "reaction.ecocyc.RXN-14325"
entity_type: "reaction"
name: "RXN-14325"
source_database: "EcoCyc"
source_id: "RXN-14325"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14325

`reaction.ecocyc.RXN-14325`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14325`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + UTP + AMMONIA -> ADP + Pi + CTP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + UTP + AMMONIA -> ADP + Pi + CTP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), Ammonia (molecule.C00014), UTP (molecule.C00075). Products: ADP (molecule.C00008), CTP (molecule.C00063), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

ATP + UTP + AMMONIA -> ADP + Pi + CTP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00063|molecule.C00063]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00014|molecule.C00014]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00075|molecule.C00075]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14325`

## Notes

ATP + UTP + AMMONIA -> ADP + Pi + CTP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
