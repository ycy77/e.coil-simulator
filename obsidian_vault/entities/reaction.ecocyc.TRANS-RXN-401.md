---
entity_id: "reaction.ecocyc.TRANS-RXN-401"
entity_type: "reaction"
name: "L-lysine:H+ antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-401"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-lysine:H+ antiport

`reaction.ecocyc.TRANS-RXN-401`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-401`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

LYS + PROTON -> LYS + PROTON; direction=REVERSIBLE EcoCyc reaction equation: LYS + PROTON -> LYS + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by lysO (protein.P75826). Substrates: L-Lysine (molecule.C00047), H+ (molecule.C00080). Products: L-Lysine (molecule.C00047), H+ (molecule.C00080).

## Annotation

LYS + PROTON -> LYS + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P75826|protein.P75826]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00047|molecule.C00047]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00047|molecule.C00047]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-401`

## Notes

LYS + PROTON -> LYS + PROTON; direction=REVERSIBLE
