---
entity_id: "reaction.ecocyc.RXN-6161"
entity_type: "reaction"
name: "RXN-6161"
source_database: "EcoCyc"
source_id: "RXN-6161"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-6161

`reaction.ecocyc.RXN-6161`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-6161`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PYRUVATE + PROTON -> ACETALD + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PYRUVATE + PROTON -> ACETALD + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Pyruvate (molecule.C00022), H+ (molecule.C00080). Products: CO2 (molecule.C00011), Acetaldehyde (molecule.C00084).

## Annotation

PYRUVATE + PROTON -> ACETALD + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00084|molecule.C00084]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-6161`

## Notes

PYRUVATE + PROTON -> ACETALD + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
