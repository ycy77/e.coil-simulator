---
entity_id: "reaction.ecocyc.RXN-20897"
entity_type: "reaction"
name: "RXN-20897"
source_database: "EcoCyc"
source_id: "RXN-20897"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20897

`reaction.ecocyc.RXN-20897`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20897`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2673 + Light -> CPD-22519; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2673 + Light -> CPD-22519; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by phrB (protein.P00914). Substrates: hν (molecule.ecocyc.Light).

## Annotation

CPD0-2673 + Light -> CPD-22519; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P00914|protein.P00914]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20897`

## Notes

CPD0-2673 + Light -> CPD-22519; direction=PHYSIOL-LEFT-TO-RIGHT
