---
entity_id: "reaction.ecocyc.RXN-14641"
entity_type: "reaction"
name: "xylose dehydrogenase"
source_database: "EcoCyc"
source_id: "RXN-14641"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# xylose dehydrogenase

`reaction.ecocyc.RXN-14641`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14641`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-Xylopyranose + NAD-P-OR-NOP -> CPD-360 + NADH-P-OR-NOP + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: D-Xylopyranose + NAD-P-OR-NOP -> CPD-360 + NADH-P-OR-NOP + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: D-xylopyranose (molecule.ecocyc.D-Xylopyranose), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP). Products: H+ (molecule.C00080), D-Xylonolactone (molecule.C02266), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP).

## Enriched Pathways

- `ecocyc.PWY-7294` D-xylose degradation IV (EcoCyc)

## Annotation

D-Xylopyranose + NAD-P-OR-NOP -> CPD-360 + NADH-P-OR-NOP + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7294` D-xylose degradation IV (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02266|molecule.C02266]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.D-Xylopyranose|molecule.ecocyc.D-Xylopyranose]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14641`

## Notes

D-Xylopyranose + NAD-P-OR-NOP -> CPD-360 + NADH-P-OR-NOP + PROTON; direction=LEFT-TO-RIGHT
