---
entity_id: "reaction.ecocyc.RXN-20706"
entity_type: "reaction"
name: "RXN-20706"
source_database: "EcoCyc"
source_id: "RXN-20706"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20706

`reaction.ecocyc.RXN-20706`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20706`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FMN + NAD + WATER -> CPD-22329 + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: FMN + NAD + WATER -> CPD-22329 + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), FMN (molecule.C00061). Products: NADH (molecule.C00004), H+ (molecule.C00080), FMN-N5-oxide (molecule.ecocyc.CPD-22329).

## Annotation

FMN + NAD + WATER -> CPD-22329 + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-22329|molecule.ecocyc.CPD-22329]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20706`

## Notes

FMN + NAD + WATER -> CPD-22329 + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
