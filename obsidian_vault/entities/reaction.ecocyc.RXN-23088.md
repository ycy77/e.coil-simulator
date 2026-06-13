---
entity_id: "reaction.ecocyc.RXN-23088"
entity_type: "reaction"
name: "RXN-23088"
source_database: "EcoCyc"
source_id: "RXN-23088"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23088

`reaction.ecocyc.RXN-23088`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23088`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

TYR + ATP + PROTON -> CPD-25513 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: TYR + ATP + PROTON -> CPD-25513 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), H+ (molecule.C00080), L-Tyrosine (molecule.C00082). Products: Diphosphate (molecule.C00013), (L-tryrosyl)adenylate (molecule.ecocyc.CPD-25513).

## Annotation

TYR + ATP + PROTON -> CPD-25513 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-25513|molecule.ecocyc.CPD-25513]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00082|molecule.C00082]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23088`

## Notes

TYR + ATP + PROTON -> CPD-25513 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
