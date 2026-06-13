---
entity_id: "reaction.ecocyc.RXN-19753"
entity_type: "reaction"
name: "RXN-19753"
source_database: "EcoCyc"
source_id: "RXN-19753"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19753

`reaction.ecocyc.RXN-19753`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19753`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-XYLONO-14-LACTONE + WATER -> D-XYLONATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: D-XYLONO-14-LACTONE + WATER -> D-XYLONATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), D-Xylono-1,4-lactone (molecule.C02753). Products: H+ (molecule.C00080), D-Xylonate (molecule.C00502).

## Enriched Pathways

- `ecocyc.PWY-6760` D-xylose degradation III (EcoCyc)

## Annotation

D-XYLONO-14-LACTONE + WATER -> D-XYLONATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6760` D-xylose degradation III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00502|molecule.C00502]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02753|molecule.C02753]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19753`

## Notes

D-XYLONO-14-LACTONE + WATER -> D-XYLONATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
