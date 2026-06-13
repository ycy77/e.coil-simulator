---
entity_id: "reaction.ecocyc.THREOSPON-RXN"
entity_type: "reaction"
name: "THREOSPON-RXN"
source_database: "EcoCyc"
source_id: "THREOSPON-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# THREOSPON-RXN

`reaction.ecocyc.THREOSPON-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:THREOSPON-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

AMINO-OXOBUT + PROTON -> AMINO-ACETONE + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: AMINO-OXOBUT + PROTON -> AMINO-ACETONE + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), L-2-Amino-3-oxobutanoic acid (molecule.C03508). Products: CO2 (molecule.C00011), Aminoacetone (molecule.C01888).

## Enriched Pathways

- `ecocyc.THRDLCTCAT-PWY` L-threonine degradation III (to methylglyoxal) (EcoCyc)

## Annotation

AMINO-OXOBUT + PROTON -> AMINO-ACETONE + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.THRDLCTCAT-PWY` L-threonine degradation III (to methylglyoxal) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01888|molecule.C01888]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03508|molecule.C03508]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:THREOSPON-RXN`

## Notes

AMINO-OXOBUT + PROTON -> AMINO-ACETONE + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
