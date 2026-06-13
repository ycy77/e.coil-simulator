---
entity_id: "reaction.ecocyc.TRANS-RXN0-237"
entity_type: "reaction"
name: "TRANS-RXN0-237"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-237"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-237

`reaction.ecocyc.TRANS-RXN0-237`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-237`
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

- `EcoCyc:TRANS-RXN0-237`

## Notes

Ubiquinones + PROTON + E- -> Ubiquinols; direction=LEFT-TO-RIGHT
