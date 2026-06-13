---
entity_id: "reaction.ecocyc.RXN-14814"
entity_type: "reaction"
name: "RXN-14814"
source_database: "EcoCyc"
source_id: "RXN-14814"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14814

`reaction.ecocyc.RXN-14814`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14814`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-ASPARTATE + ATP + PROTON -> CPD0-915 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-ASPARTATE + ATP + PROTON -> CPD0-915 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), L-Aspartate (molecule.C00049), H+ (molecule.C00080). Products: Diphosphate (molecule.C00013), (L-aspartyl)adenylate (molecule.ecocyc.CPD0-915).

## Annotation

L-ASPARTATE + ATP + PROTON -> CPD0-915 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-915|molecule.ecocyc.CPD0-915]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14814`

## Notes

L-ASPARTATE + ATP + PROTON -> CPD0-915 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
