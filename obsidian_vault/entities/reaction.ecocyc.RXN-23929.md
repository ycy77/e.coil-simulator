---
entity_id: "reaction.ecocyc.RXN-23929"
entity_type: "reaction"
name: "RXN-23929"
source_database: "EcoCyc"
source_id: "RXN-23929"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23929

`reaction.ecocyc.RXN-23929`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23929`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-302 + ATP + PROTON -> CPD-26479 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-302 + ATP + PROTON -> CPD-26479 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), H+ (molecule.C00080), D-Aspartate (molecule.C00402). Products: Diphosphate (molecule.C00013), (D-aspartyl)adenylate (molecule.ecocyc.CPD-26479).

## Annotation

CPD-302 + ATP + PROTON -> CPD-26479 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-26479|molecule.ecocyc.CPD-26479]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00402|molecule.C00402]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23929`

## Notes

CPD-302 + ATP + PROTON -> CPD-26479 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
