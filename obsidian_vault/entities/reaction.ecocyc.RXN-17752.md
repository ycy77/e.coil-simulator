---
entity_id: "reaction.ecocyc.RXN-17752"
entity_type: "reaction"
name: "RXN-17752"
source_database: "EcoCyc"
source_id: "RXN-17752"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17752

`reaction.ecocyc.RXN-17752`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17752`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPDMETA-13650 -> CPD0-2558 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPDMETA-13650 -> CPD0-2558 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: 3-Oxo-5,6-dehydrosuberyl-CoA semialdehyde (molecule.C19946). Products: H2O (molecule.C00001), 2-hydroxycyclohepta-1,4,6-triene-1-carboxyl-CoA (molecule.ecocyc.CPD0-2558).

## Annotation

CPDMETA-13650 -> CPD0-2558 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2558|molecule.ecocyc.CPD0-2558]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C19946|molecule.C19946]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17752`

## Notes

CPDMETA-13650 -> CPD0-2558 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
