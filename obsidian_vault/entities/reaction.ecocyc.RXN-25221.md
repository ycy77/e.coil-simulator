---
entity_id: "reaction.ecocyc.RXN-25221"
entity_type: "reaction"
name: "RXN-25221"
source_database: "EcoCyc"
source_id: "RXN-25221"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-25221

`reaction.ecocyc.RXN-25221`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25221`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-27807 + WATER -> CPD-20606 + D-Glucopyranuronate + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-27807 + WATER -> CPD-20606 + D-Glucopyranuronate + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by β-D-glucuronidase (complex.ecocyc.CPLX0-7662). Substrates: H2O (molecule.C00001), diclofenac glucuronide (molecule.ecocyc.CPD-27807). Products: H+ (molecule.C00080), diclofenac (molecule.ecocyc.CPD-20606), D-glucopyranuronate (molecule.ecocyc.D-Glucopyranuronate).

## Annotation

CPD-27807 + WATER -> CPD-20606 + D-Glucopyranuronate + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7662|complex.ecocyc.CPLX0-7662]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-20606|molecule.ecocyc.CPD-20606]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.D-Glucopyranuronate|molecule.ecocyc.D-Glucopyranuronate]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-27807|molecule.ecocyc.CPD-27807]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-27851|molecule.ecocyc.CPD-27851]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-25221`

## Notes

CPD-27807 + WATER -> CPD-20606 + D-Glucopyranuronate + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
