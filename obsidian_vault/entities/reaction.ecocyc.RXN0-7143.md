---
entity_id: "reaction.ecocyc.RXN0-7143"
entity_type: "reaction"
name: "RXN0-7143"
source_database: "EcoCyc"
source_id: "RXN0-7143"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7143

`reaction.ecocyc.RXN0-7143`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7143`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-17752 -> CPD-17753; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-17752 -> CPD-17753; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pdxI (protein.P25906). Substrates: 5-nitro benzisoxazole (molecule.ecocyc.CPD-17752). Products: 2-cyano-4-nitrophenol (molecule.ecocyc.CPD-17753).

## Annotation

CPD-17752 -> CPD-17753; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `activates` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P25906|protein.P25906]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-17753|molecule.ecocyc.CPD-17753]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-17752|molecule.ecocyc.CPD-17752]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7143`

## Notes

CPD-17752 -> CPD-17753; direction=PHYSIOL-LEFT-TO-RIGHT
