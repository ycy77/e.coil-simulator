---
entity_id: "reaction.ecocyc.RXN0-6450"
entity_type: "reaction"
name: "RXN0-6450"
source_database: "EcoCyc"
source_id: "RXN0-6450"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6450

`reaction.ecocyc.RXN0-6450`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6450`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2338 + NADH -> CPD0-2331 + NAD + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2338 + NADH -> CPD0-2331 + NAD + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: NADH (molecule.C00004), (Z)-3-Ureidoacrylate peracid (molecule.C20231). Products: H2O (molecule.C00001), NAD+ (molecule.C00003), Ureidoacrylate (molecule.C20254).

## Annotation

CPD0-2338 + NADH -> CPD0-2331 + NAD + WATER; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C20254|molecule.C20254]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C20231|molecule.C20231]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6450`

## Notes

CPD0-2338 + NADH -> CPD0-2331 + NAD + WATER; direction=LEFT-TO-RIGHT
