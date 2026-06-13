---
entity_id: "reaction.ecocyc.RXN-11115"
entity_type: "reaction"
name: "RXN-11115"
source_database: "EcoCyc"
source_id: "RXN-11115"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11115

`reaction.ecocyc.RXN-11115`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11115`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CYS + ATP + PROTON -> CPD-12085 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CYS + ATP + PROTON -> CPD-12085 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), H+ (molecule.C00080), L-Cysteine (molecule.C00097). Products: Diphosphate (molecule.C00013), (L-cysteinyl)adenylate (molecule.ecocyc.CPD-12085).

## Annotation

CYS + ATP + PROTON -> CPD-12085 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-12085|molecule.ecocyc.CPD-12085]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11115`

## Notes

CYS + ATP + PROTON -> CPD-12085 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
