---
entity_id: "reaction.ecocyc.RXN-18804"
entity_type: "reaction"
name: "RXN-18804"
source_database: "EcoCyc"
source_id: "RXN-18804"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-18804

`reaction.ecocyc.RXN-18804`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-18804`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLT + ATP + PROTON -> CPD-20105 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GLT + ATP + PROTON -> CPD-20105 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), L-Glutamate (molecule.C00025), H+ (molecule.C00080). Products: Diphosphate (molecule.C00013), (L-glutamyl)adenylate (molecule.ecocyc.CPD-20105).

## Annotation

GLT + ATP + PROTON -> CPD-20105 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-20105|molecule.ecocyc.CPD-20105]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-18804`

## Notes

GLT + ATP + PROTON -> CPD-20105 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
