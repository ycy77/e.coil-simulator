---
entity_id: "reaction.ecocyc.RXN-16003"
entity_type: "reaction"
name: "RXN-16003"
source_database: "EcoCyc"
source_id: "RXN-16003"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16003

`reaction.ecocyc.RXN-16003`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16003`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

SER + NADP -> CPD-1772 + NADPH + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: SER + NADP -> CPD-1772 + NADPH + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: NADP+ (molecule.C00006), L-Serine (molecule.C00065). Products: NADPH (molecule.C00005), CO2 (molecule.C00011), Aminoacetaldehyde (molecule.C06735).

## Annotation

SER + NADP -> CPD-1772 + NADPH + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06735|molecule.C06735]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16003`

## Notes

SER + NADP -> CPD-1772 + NADPH + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
