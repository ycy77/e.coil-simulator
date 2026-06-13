---
entity_id: "reaction.ecocyc.RXN-22735"
entity_type: "reaction"
name: "RXN-22735"
source_database: "EcoCyc"
source_id: "RXN-22735"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22735

`reaction.ecocyc.RXN-22735`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22735`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + HCO3 + AMMONIA -> ADP + Pi + CARBAMOYL-P + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + HCO3 + AMMONIA -> ADP + Pi + CARBAMOYL-P + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), Ammonia (molecule.C00014), HCO3- (molecule.C00288). Products: ADP (molecule.C00008), H+ (molecule.C00080), Carbamoyl phosphate (molecule.C00169), phosphate (molecule.ecocyc.Pi).

## Annotation

ATP + HCO3 + AMMONIA -> ADP + Pi + CARBAMOYL-P + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00169|molecule.C00169]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00014|molecule.C00014]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00288|molecule.C00288]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22735`

## Notes

ATP + HCO3 + AMMONIA -> ADP + Pi + CARBAMOYL-P + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
