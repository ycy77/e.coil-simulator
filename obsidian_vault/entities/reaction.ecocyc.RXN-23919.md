---
entity_id: "reaction.ecocyc.RXN-23919"
entity_type: "reaction"
name: "RXN-23919"
source_database: "EcoCyc"
source_id: "RXN-23919"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23919

`reaction.ecocyc.RXN-23919`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23919`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-26476 -> CPD-26475 + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-26476 -> CPD-26475 + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: (L-ornithyl)adenylate (molecule.ecocyc.CPD-26476). Products: AMP (molecule.C00020), H+ (molecule.C00080), 3-aminopiperidine-2-one (molecule.ecocyc.CPD-26475).

## Annotation

CPD-26476 -> CPD-26475 + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-26475|molecule.ecocyc.CPD-26475]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-26476|molecule.ecocyc.CPD-26476]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23919`

## Notes

CPD-26476 -> CPD-26475 + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
