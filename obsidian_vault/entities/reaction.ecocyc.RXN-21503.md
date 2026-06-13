---
entity_id: "reaction.ecocyc.RXN-21503"
entity_type: "reaction"
name: "RXN-21503"
source_database: "EcoCyc"
source_id: "RXN-21503"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21503

`reaction.ecocyc.RXN-21503`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21503`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-Xylopyranose + NADP -> D-XYLONO-14-LACTONE + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: D-Xylopyranose + NADP -> D-XYLONO-14-LACTONE + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: NADP+ (molecule.C00006), D-xylopyranose (molecule.ecocyc.D-Xylopyranose). Products: NADPH (molecule.C00005), H+ (molecule.C00080), D-Xylono-1,4-lactone (molecule.C02753).

## Enriched Pathways

- `ecocyc.PWY-6760` D-xylose degradation III (EcoCyc)

## Annotation

D-Xylopyranose + NADP -> D-XYLONO-14-LACTONE + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6760` D-xylose degradation III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02753|molecule.C02753]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.D-Xylopyranose|molecule.ecocyc.D-Xylopyranose]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21503`

## Notes

D-Xylopyranose + NADP -> D-XYLONO-14-LACTONE + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
