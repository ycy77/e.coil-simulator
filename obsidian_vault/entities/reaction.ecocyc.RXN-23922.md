---
entity_id: "reaction.ecocyc.RXN-23922"
entity_type: "reaction"
name: "RXN-23922"
source_database: "EcoCyc"
source_id: "RXN-23922"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23922

`reaction.ecocyc.RXN-23922`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23922`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

HOMO-CYS + ATP + PROTON -> CPD-26477 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: HOMO-CYS + ATP + PROTON -> CPD-26477 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), H+ (molecule.C00080), L-Homocysteine (molecule.C00155). Products: Diphosphate (molecule.C00013), (L-homocysteinyl)adenylate (molecule.ecocyc.CPD-26477).

## Annotation

HOMO-CYS + ATP + PROTON -> CPD-26477 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-26477|molecule.ecocyc.CPD-26477]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00155|molecule.C00155]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23922`

## Notes

HOMO-CYS + ATP + PROTON -> CPD-26477 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
