---
entity_id: "reaction.ecocyc.RXN-17013"
entity_type: "reaction"
name: "RXN-17013"
source_database: "EcoCyc"
source_id: "RXN-17013"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17013

`reaction.ecocyc.RXN-17013`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17013`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Palmitoleoyl-ACPs + CPD-18348 -> CPD-18351 + ACP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Palmitoleoyl-ACPs + CPD-18348 -> CPD-18351 + ACP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by plsC (protein.P26647). Substrates: 1-cis-vaccenoyl-sn-glycerol-3-phosphate (molecule.ecocyc.CPD-18348). Products: 1-cis-vaccenoyl-2-palmitoleoyl-sn-glycerol-3-phosphate (molecule.ecocyc.CPD-18351).

## Annotation

Palmitoleoyl-ACPs + CPD-18348 -> CPD-18351 + ACP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P26647|protein.P26647]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-18351|molecule.ecocyc.CPD-18351]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-18348|molecule.ecocyc.CPD-18348]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17013`

## Notes

Palmitoleoyl-ACPs + CPD-18348 -> CPD-18351 + ACP; direction=PHYSIOL-LEFT-TO-RIGHT
