---
entity_id: "reaction.ecocyc.RXN-12246"
entity_type: "reaction"
name: "D-xylonolactonase"
source_database: "EcoCyc"
source_id: "RXN-12246"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# D-xylonolactonase

`reaction.ecocyc.RXN-12246`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12246`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-360 + WATER -> D-XYLONATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-360 + WATER -> D-XYLONATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), D-Xylonolactone (molecule.C02266). Products: H+ (molecule.C00080), D-Xylonate (molecule.C00502).

## Enriched Pathways

- `ecocyc.PWY-7294` D-xylose degradation IV (EcoCyc)

## Annotation

CPD-360 + WATER -> D-XYLONATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7294` D-xylose degradation IV (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00502|molecule.C00502]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02266|molecule.C02266]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12246`

## Notes

CPD-360 + WATER -> D-XYLONATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
