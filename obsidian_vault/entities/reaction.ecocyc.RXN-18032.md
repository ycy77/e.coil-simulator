---
entity_id: "reaction.ecocyc.RXN-18032"
entity_type: "reaction"
name: "RXN-18032"
source_database: "EcoCyc"
source_id: "RXN-18032"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-18032

`reaction.ecocyc.RXN-18032`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-18032`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

HCO3 -> CO3 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: HCO3 -> CO3 + PROTON; direction=REVERSIBLE.

## Biological Role

Substrates: HCO3- (molecule.C00288). Products: H+ (molecule.C00080), carbonate (molecule.ecocyc.CO3).

## Annotation

HCO3 -> CO3 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CO3|molecule.ecocyc.CO3]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00288|molecule.C00288]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-18032`

## Notes

HCO3 -> CO3 + PROTON; direction=REVERSIBLE
