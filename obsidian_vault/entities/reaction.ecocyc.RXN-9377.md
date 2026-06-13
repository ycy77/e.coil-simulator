---
entity_id: "reaction.ecocyc.RXN-9377"
entity_type: "reaction"
name: "RXN-9377"
source_database: "EcoCyc"
source_id: "RXN-9377"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-9377

`reaction.ecocyc.RXN-9377`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9377`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

THR + ATP + PROTON -> CPD-9994 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: THR + ATP + PROTON -> CPD-9994 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), H+ (molecule.C00080), L-Threonine (molecule.C00188). Products: Diphosphate (molecule.C00013), (L-threonyl)adenylate (molecule.ecocyc.CPD-9994).

## Annotation

THR + ATP + PROTON -> CPD-9994 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-9994|molecule.ecocyc.CPD-9994]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00188|molecule.C00188]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-9377`

## Notes

THR + ATP + PROTON -> CPD-9994 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
