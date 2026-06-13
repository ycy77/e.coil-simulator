---
entity_id: "reaction.ecocyc.RXN-20707"
entity_type: "reaction"
name: "RXN-20707"
source_database: "EcoCyc"
source_id: "RXN-20707"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20707

`reaction.ecocyc.RXN-20707`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20707`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

URACIL + CPD-24463 -> CPD0-2331 + CPD-22329; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: URACIL + CPD-24463 -> CPD0-2331 + CPD-22329; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Uracil (molecule.C00106), FMN-N5-peroxide (molecule.ecocyc.CPD-24463). Products: Ureidoacrylate (molecule.C20254), FMN-N5-oxide (molecule.ecocyc.CPD-22329).

## Annotation

URACIL + CPD-24463 -> CPD0-2331 + CPD-22329; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C20254|molecule.C20254]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-22329|molecule.ecocyc.CPD-22329]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00106|molecule.C00106]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-24463|molecule.ecocyc.CPD-24463]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20707`

## Notes

URACIL + CPD-24463 -> CPD0-2331 + CPD-22329; direction=PHYSIOL-LEFT-TO-RIGHT
