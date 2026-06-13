---
entity_id: "reaction.ecocyc.RXN-25603"
entity_type: "reaction"
name: "RXN-25603"
source_database: "EcoCyc"
source_id: "RXN-25603"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-25603

`reaction.ecocyc.RXN-25603`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25603`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-24961 -> D-XYLULOSE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-24961 -> D-XYLULOSE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: α-D-xylulofuranose (molecule.ecocyc.CPD-24961). Products: D-Xylulose (molecule.C00310).

## Enriched Pathways

- `ecocyc.XYLCAT-PWY` D-xylose degradation I (EcoCyc)

## Annotation

CPD-24961 -> D-XYLULOSE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.XYLCAT-PWY` D-xylose degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00310|molecule.C00310]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-24961|molecule.ecocyc.CPD-24961]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25603`

## Notes

CPD-24961 -> D-XYLULOSE; direction=PHYSIOL-LEFT-TO-RIGHT
