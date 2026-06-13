---
entity_id: "reaction.ecocyc.TRANS-RXN-320"
entity_type: "reaction"
name: "TRANS-RXN-320"
source_database: "EcoCyc"
source_id: "TRANS-RXN-320"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-320

`reaction.ecocyc.TRANS-RXN-320`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-320`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Glucopyranose + ATP + WATER -> Glucopyranose + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Glucopyranose + ATP + WATER -> Glucopyranose + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), ATP (molecule.C00002), D-Glucose (molecule.C00031). Products: ADP (molecule.C00008), D-Glucose (molecule.C00031), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

Glucopyranose + ATP + WATER -> Glucopyranose + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-320`

## Notes

Glucopyranose + ATP + WATER -> Glucopyranose + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
