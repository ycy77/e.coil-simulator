---
entity_id: "reaction.ecocyc.RXN-23920"
entity_type: "reaction"
name: "RXN-23920"
source_database: "EcoCyc"
source_id: "RXN-23920"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23920

`reaction.ecocyc.RXN-23920`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23920`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-ORNITHINE + ATP + PROTON -> CPD-26476 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-ORNITHINE + ATP + PROTON -> CPD-26476 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), L-Ornithine (molecule.C00077), H+ (molecule.C00080). Products: Diphosphate (molecule.C00013), (L-ornithyl)adenylate (molecule.ecocyc.CPD-26476).

## Annotation

L-ORNITHINE + ATP + PROTON -> CPD-26476 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-26476|molecule.ecocyc.CPD-26476]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00077|molecule.C00077]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23920`

## Notes

L-ORNITHINE + ATP + PROTON -> CPD-26476 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
