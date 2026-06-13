---
entity_id: "reaction.ecocyc.RXN-22679"
entity_type: "reaction"
name: "RXN-22679"
source_database: "EcoCyc"
source_id: "RXN-22679"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22679

`reaction.ecocyc.RXN-22679`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22679`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

LYS + ATP + PROTON -> CPD-24910 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: LYS + ATP + PROTON -> CPD-24910 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), L-Lysine (molecule.C00047), H+ (molecule.C00080). Products: Diphosphate (molecule.C00013), (L-lysyl)adenylate (molecule.ecocyc.CPD-24910).

## Annotation

LYS + ATP + PROTON -> CPD-24910 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-24910|molecule.ecocyc.CPD-24910]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00047|molecule.C00047]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22679`

## Notes

LYS + ATP + PROTON -> CPD-24910 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
