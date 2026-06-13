---
entity_id: "reaction.ecocyc.RXN-19079"
entity_type: "reaction"
name: "RXN-19079"
source_database: "EcoCyc"
source_id: "RXN-19079"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19079

`reaction.ecocyc.RXN-19079`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19079`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PRO + ATP + PROTON -> CPD-20571 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PRO + ATP + PROTON -> CPD-20571 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), H+ (molecule.C00080), L-Proline (molecule.C00148). Products: Diphosphate (molecule.C00013), (L-prolyl)adenylate (molecule.ecocyc.CPD-20571).

## Annotation

PRO + ATP + PROTON -> CPD-20571 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-20571|molecule.ecocyc.CPD-20571]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00148|molecule.C00148]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19079`

## Notes

PRO + ATP + PROTON -> CPD-20571 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
