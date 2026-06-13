---
entity_id: "reaction.ecocyc.RXN-17104"
entity_type: "reaction"
name: "RXN-17104"
source_database: "EcoCyc"
source_id: "RXN-17104"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17104

`reaction.ecocyc.RXN-17104`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17104`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GERANYL-PP + WATER -> CPD-13243 + Pi + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: GERANYL-PP + WATER -> CPD-13243 + Pi + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nudI (protein.P52006). Substrates: H2O (molecule.C00001), Geranyl diphosphate (molecule.C00341). Products: H+ (molecule.C00080), geranyl monophosphate (molecule.ecocyc.CPD-13243), phosphate (molecule.ecocyc.Pi).

## Annotation

GERANYL-PP + WATER -> CPD-13243 + Pi + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P52006|protein.P52006]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-13243|molecule.ecocyc.CPD-13243]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00341|molecule.C00341]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17104`

## Notes

GERANYL-PP + WATER -> CPD-13243 + Pi + PROTON; direction=LEFT-TO-RIGHT
