---
entity_id: "reaction.ecocyc.RXN-13605"
entity_type: "reaction"
name: "RXN-13605"
source_database: "EcoCyc"
source_id: "RXN-13605"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-13605

`reaction.ecocyc.RXN-13605`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-13605`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-14602 + WATER -> CPD-14601 + D-Glucopyranuronate + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-14602 + WATER -> CPD-14601 + D-Glucopyranuronate + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by β-D-glucuronidase (complex.ecocyc.CPLX0-7662). Substrates: H2O (molecule.C00001), mycophenolic acid O-acyl-glucuronide (molecule.ecocyc.CPD-14602). Products: H+ (molecule.C00080), mycophenolate (molecule.ecocyc.CPD-14601), D-glucopyranuronate (molecule.ecocyc.D-Glucopyranuronate).

## Annotation

CPD-14602 + WATER -> CPD-14601 + D-Glucopyranuronate + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7662|complex.ecocyc.CPLX0-7662]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-14601|molecule.ecocyc.CPD-14601]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.D-Glucopyranuronate|molecule.ecocyc.D-Glucopyranuronate]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-14602|molecule.ecocyc.CPD-14602]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-27850|molecule.ecocyc.CPD-27850]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-13605`

## Notes

CPD-14602 + WATER -> CPD-14601 + D-Glucopyranuronate + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
