---
entity_id: "reaction.ecocyc.RXN-18031"
entity_type: "reaction"
name: "RXN-18031"
source_database: "EcoCyc"
source_id: "RXN-18031"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-18031

`reaction.ecocyc.RXN-18031`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-18031`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

H2CO3 -> HCO3 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: H2CO3 -> HCO3 + PROTON; direction=REVERSIBLE.

## Biological Role

Substrates: carbonic acid (molecule.ecocyc.H2CO3). Products: H+ (molecule.C00080), HCO3- (molecule.C00288).

## Annotation

H2CO3 -> HCO3 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00288|molecule.C00288]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.H2CO3|molecule.ecocyc.H2CO3]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-18031`

## Notes

H2CO3 -> HCO3 + PROTON; direction=REVERSIBLE
