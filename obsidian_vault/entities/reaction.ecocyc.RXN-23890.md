---
entity_id: "reaction.ecocyc.RXN-23890"
entity_type: "reaction"
name: "RXN-23890"
source_database: "EcoCyc"
source_id: "RXN-23890"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23890

`reaction.ecocyc.RXN-23890`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23890`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

LEU + ATP + PROTON -> CPD-26470 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: LEU + ATP + PROTON -> CPD-26470 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), H+ (molecule.C00080), L-Leucine (molecule.C00123). Products: Diphosphate (molecule.C00013), (L-leucyl)adenylate (molecule.ecocyc.CPD-26470).

## Annotation

LEU + ATP + PROTON -> CPD-26470 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-26470|molecule.ecocyc.CPD-26470]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00123|molecule.C00123]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23890`

## Notes

LEU + ATP + PROTON -> CPD-26470 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
