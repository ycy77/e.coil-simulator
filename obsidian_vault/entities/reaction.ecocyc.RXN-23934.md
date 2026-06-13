---
entity_id: "reaction.ecocyc.RXN-23934"
entity_type: "reaction"
name: "RXN-23934"
source_database: "EcoCyc"
source_id: "RXN-23934"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23934

`reaction.ecocyc.RXN-23934`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23934`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-TYROSINE + ATP + PROTON -> CPD-26482 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: D-TYROSINE + ATP + PROTON -> CPD-26482 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), H+ (molecule.C00080), D-tyrosine (molecule.ecocyc.D-TYROSINE). Products: Diphosphate (molecule.C00013), (D-tyrosyl)adenylate (molecule.ecocyc.CPD-26482).

## Annotation

D-TYROSINE + ATP + PROTON -> CPD-26482 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-26482|molecule.ecocyc.CPD-26482]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.D-TYROSINE|molecule.ecocyc.D-TYROSINE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23934`

## Notes

D-TYROSINE + ATP + PROTON -> CPD-26482 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
