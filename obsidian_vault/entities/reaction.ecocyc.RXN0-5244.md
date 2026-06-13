---
entity_id: "reaction.ecocyc.RXN0-5244"
entity_type: "reaction"
name: "RXN0-5244"
source_database: "EcoCyc"
source_id: "RXN0-5244"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5244

`reaction.ecocyc.RXN0-5244`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5244`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Ubiquinones + PROTON + E- -> Ubiquinols; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Ubiquinones + PROTON + E- -> Ubiquinols; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), a ubiquinone (molecule.ecocyc.Ubiquinones). Products: Ubiquinol (molecule.C00390).

## Annotation

Ubiquinones + PROTON + E- -> Ubiquinols; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00390|molecule.C00390]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Ubiquinones|molecule.ecocyc.Ubiquinones]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5244`

## Notes

Ubiquinones + PROTON + E- -> Ubiquinols; direction=LEFT-TO-RIGHT
