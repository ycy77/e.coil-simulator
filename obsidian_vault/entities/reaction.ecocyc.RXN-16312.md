---
entity_id: "reaction.ecocyc.RXN-16312"
entity_type: "reaction"
name: "RXN-16312"
source_database: "EcoCyc"
source_id: "RXN-16312"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16312

`reaction.ecocyc.RXN-16312`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16312`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-17573 + OXYGEN-MOLECULE -> CPD-17574 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-17573 + OXYGEN-MOLECULE -> CPD-17574 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yfiH (protein.P33644). Substrates: Oxygen (molecule.C00007), syringaldazine (molecule.ecocyc.CPD-17573). Products: H2O (molecule.C00001), tetramethoxy azobismethylene quinine (molecule.ecocyc.CPD-17574).

## Annotation

CPD-17573 + OXYGEN-MOLECULE -> CPD-17574 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P33644|protein.P33644]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-17574|molecule.ecocyc.CPD-17574]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-17573|molecule.ecocyc.CPD-17573]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16312`

## Notes

CPD-17573 + OXYGEN-MOLECULE -> CPD-17574 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
