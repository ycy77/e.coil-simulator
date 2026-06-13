---
entity_id: "reaction.ecocyc.RXN-22915"
entity_type: "reaction"
name: "RXN-22915"
source_database: "EcoCyc"
source_id: "RXN-22915"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22915

`reaction.ecocyc.RXN-22915`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22915`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-25382 + CYS -> R-4-PHOSPHOPANTOTHENOYL-L-CYSTEINE + CMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-25382 + CYS -> R-4-PHOSPHOPANTOTHENOYL-L-CYSTEINE + CMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: L-Cysteine (molecule.C00097), (R)-4'-phosphopantothenoyl-cytidylate (molecule.ecocyc.CPD-25382). Products: CMP (molecule.C00055), H+ (molecule.C00080), (R)-4'-Phosphopantothenoyl-L-cysteine (molecule.C04352).

## Annotation

CPD-25382 + CYS -> R-4-PHOSPHOPANTOTHENOYL-L-CYSTEINE + CMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00055|molecule.C00055]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04352|molecule.C04352]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-25382|molecule.ecocyc.CPD-25382]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22915`

## Notes

CPD-25382 + CYS -> R-4-PHOSPHOPANTOTHENOYL-L-CYSTEINE + CMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
