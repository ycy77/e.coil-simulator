---
entity_id: "reaction.ecocyc.RXN-15356"
entity_type: "reaction"
name: "RXN-15356"
source_database: "EcoCyc"
source_id: "RXN-15356"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15356

`reaction.ecocyc.RXN-15356`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15356`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-16566 -> CPD-16567; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-16566 -> CPD-16567; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: L-Rhamnulose (molecule.C00861). Products: L-rhamnulofuranose (molecule.ecocyc.CPD-16567).

## Enriched Pathways

- `ecocyc.RHAMCAT-PWY` L-rhamnose degradation I (EcoCyc)

## Annotation

CPD-16566 -> CPD-16567; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.RHAMCAT-PWY` L-rhamnose degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.CPD-16567|molecule.ecocyc.CPD-16567]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00861|molecule.C00861]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15356`

## Notes

CPD-16566 -> CPD-16567; direction=LEFT-TO-RIGHT
