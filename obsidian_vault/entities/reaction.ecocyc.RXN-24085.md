---
entity_id: "reaction.ecocyc.RXN-24085"
entity_type: "reaction"
name: "RXN-24085"
source_database: "EcoCyc"
source_id: "RXN-24085"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24085

`reaction.ecocyc.RXN-24085`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24085`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Menaquinones + PROTON + E- -> Menaquinols + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Menaquinones + PROTON + E- -> Menaquinols + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), Menaquinone (molecule.C00828). Products: H+ (molecule.C00080), Menaquinol (molecule.C05819).

## Annotation

Menaquinones + PROTON + E- -> Menaquinols + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05819|molecule.C05819]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00828|molecule.C00828]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24085`

## Notes

Menaquinones + PROTON + E- -> Menaquinols + PROTON; direction=LEFT-TO-RIGHT
