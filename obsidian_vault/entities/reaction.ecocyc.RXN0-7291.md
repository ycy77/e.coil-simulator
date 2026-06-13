---
entity_id: "reaction.ecocyc.RXN0-7291"
entity_type: "reaction"
name: "RXN0-7291"
source_database: "EcoCyc"
source_id: "RXN0-7291"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7291

`reaction.ecocyc.RXN0-7291`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7291`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GUANOSINE-5DP-3DP + WATER -> CPD0-2634 + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GUANOSINE-5DP-3DP + WATER -> CPD0-2634 + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nudG (protein.P77788). Substrates: H2O (molecule.C00001), Guanosine 3',5'-bis(diphosphate) (molecule.C01228). Products: H+ (molecule.C00080), pGp (molecule.ecocyc.CPD0-2634), phosphate (molecule.ecocyc.Pi).

## Annotation

GUANOSINE-5DP-3DP + WATER -> CPD0-2634 + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P77788|protein.P77788]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2634|molecule.ecocyc.CPD0-2634]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01228|molecule.C01228]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7291`

## Notes

GUANOSINE-5DP-3DP + WATER -> CPD0-2634 + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
