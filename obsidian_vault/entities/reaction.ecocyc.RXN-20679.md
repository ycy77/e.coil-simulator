---
entity_id: "reaction.ecocyc.RXN-20679"
entity_type: "reaction"
name: "RXN-20679"
source_database: "EcoCyc"
source_id: "RXN-20679"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20679

`reaction.ecocyc.RXN-20679`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20679`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-22313 + NAD -> CPD0-2106 + NADH + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-22313 + NAD -> CPD0-2106 + NADH + PROTON; direction=REVERSIBLE.

## Biological Role

Substrates: NAD+ (molecule.C00003), (3S)-3-hydroxyoctanoyl-CoA (molecule.ecocyc.CPD-22313). Products: NADH (molecule.C00004), H+ (molecule.C00080), 3-Oxooctanoyl-CoA (molecule.C05267).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

CPD-22313 + NAD -> CPD0-2106 + NADH + PROTON; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05267|molecule.C05267]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-22313|molecule.ecocyc.CPD-22313]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20679`

## Notes

CPD-22313 + NAD -> CPD0-2106 + NADH + PROTON; direction=REVERSIBLE
