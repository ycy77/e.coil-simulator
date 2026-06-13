---
entity_id: "reaction.ecocyc.RXN-21383"
entity_type: "reaction"
name: "RXN-21383"
source_database: "EcoCyc"
source_id: "RXN-21383"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21383

`reaction.ecocyc.RXN-21383`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21383`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ENOL-OXALOACETATE + PROTON -> PYRUVATE + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ENOL-OXALOACETATE + PROTON -> PYRUVATE + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), 2-Hydroxyethylenedicarboxylate (molecule.C03981). Products: CO2 (molecule.C00011), Pyruvate (molecule.C00022).

## Annotation

ENOL-OXALOACETATE + PROTON -> PYRUVATE + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03981|molecule.C03981]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21383`

## Notes

ENOL-OXALOACETATE + PROTON -> PYRUVATE + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
