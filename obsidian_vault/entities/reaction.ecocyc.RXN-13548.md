---
entity_id: "reaction.ecocyc.RXN-13548"
entity_type: "reaction"
name: "RXN-13548"
source_database: "EcoCyc"
source_id: "RXN-13548"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-13548

`reaction.ecocyc.RXN-13548`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-13548`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-GALACTOSAMINE-6-PHOSPHATE + WATER -> TAGATOSE-6-PHOSPHATE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: D-GALACTOSAMINE-6-PHOSPHATE + WATER -> TAGATOSE-6-PHOSPHATE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by agaS (protein.P42907). Substrates: H2O (molecule.C00001), D-Galactosamine 6-phosphate (molecule.C06377). Products: D-Tagatose 6-phosphate (molecule.C01097), ammonium (molecule.ecocyc.AMMONIUM).

## Annotation

D-GALACTOSAMINE-6-PHOSPHATE + WATER -> TAGATOSE-6-PHOSPHATE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P42907|protein.P42907]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01097|molecule.C01097]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06377|molecule.C06377]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-13548`

## Notes

D-GALACTOSAMINE-6-PHOSPHATE + WATER -> TAGATOSE-6-PHOSPHATE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT
