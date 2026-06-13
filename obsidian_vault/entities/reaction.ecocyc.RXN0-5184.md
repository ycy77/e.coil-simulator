---
entity_id: "reaction.ecocyc.RXN0-5184"
entity_type: "reaction"
name: "RXN0-5184"
source_database: "EcoCyc"
source_id: "RXN0-5184"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5184

`reaction.ecocyc.RXN0-5184`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5184`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Part of the catabolic pathway for maltodextrins. EcoCyc reaction equation: 1-4-alpha-D-Glucan + Pi -> 1-4-alpha-D-Glucan + GLC-1-P; direction=PHYSIOL-LEFT-TO-RIGHT. Part of the catabolic pathway for maltodextrins.

## Biological Role

Substrates: Amylose (molecule.C00718), phosphate (molecule.ecocyc.Pi). Products: Amylose (molecule.C00718), α-D-glucopyranose 1-phosphate (molecule.ecocyc.GLC-1-P).

## Annotation

Part of the catabolic pathway for maltodextrins.

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00718|molecule.C00718]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.GLC-1-P|molecule.ecocyc.GLC-1-P]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00718|molecule.C00718]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5184`

## Notes

1-4-alpha-D-Glucan + Pi -> 1-4-alpha-D-Glucan + GLC-1-P; direction=PHYSIOL-LEFT-TO-RIGHT
