---
entity_id: "reaction.ecocyc.RXN0-7421"
entity_type: "reaction"
name: "RXN0-7421"
source_database: "EcoCyc"
source_id: "RXN0-7421"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7421

`reaction.ecocyc.RXN0-7421`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7421`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a test reaction created for use in the Q cycle catalysed by cytochrome bc1 (complex III). EcoCyc reaction equation: Ubiquinones + PROTON + E- -> Ubiquinols + PROTON; direction=LEFT-TO-RIGHT. This is a test reaction created for use in the Q cycle catalysed by cytochrome bc1 (complex III).

## Biological Role

Substrates: H+ (molecule.C00080), a ubiquinone (molecule.ecocyc.Ubiquinones). Products: H+ (molecule.C00080), Ubiquinol (molecule.C00390).

## Annotation

This is a test reaction created for use in the Q cycle catalysed by cytochrome bc1 (complex III).

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00390|molecule.C00390]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Ubiquinones|molecule.ecocyc.Ubiquinones]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7421`

## Notes

Ubiquinones + PROTON + E- -> Ubiquinols + PROTON; direction=LEFT-TO-RIGHT
