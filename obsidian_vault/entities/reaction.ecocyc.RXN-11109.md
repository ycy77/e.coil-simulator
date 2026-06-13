---
entity_id: "reaction.ecocyc.RXN-11109"
entity_type: "reaction"
name: "RXN-11109"
source_database: "EcoCyc"
source_id: "RXN-11109"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Molecular chaperone Hsc70 ATPase"
  - "ATP phosphohydrolase (RNA helix unwinding)"
---

# RXN-11109

`reaction.ecocyc.RXN-11109`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11109`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Wound-RNA + ATP + WATER -> Unwound-RNA + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Wound-RNA + ATP + WATER -> Unwound-RNA + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), ATP (molecule.C00002). Products: ADP (molecule.C00008), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

Wound-RNA + ATP + WATER -> Unwound-RNA + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11109`

## Notes

Wound-RNA + ATP + WATER -> Unwound-RNA + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
