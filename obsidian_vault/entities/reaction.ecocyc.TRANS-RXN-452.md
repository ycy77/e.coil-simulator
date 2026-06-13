---
entity_id: "reaction.ecocyc.TRANS-RXN-452"
entity_type: "reaction"
name: "TRANS-RXN-452"
source_database: "EcoCyc"
source_id: "TRANS-RXN-452"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-452

`reaction.ecocyc.TRANS-RXN-452`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-452`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PB+2 + ATP + WATER -> PB+2 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PB+2 + ATP + WATER -> PB+2 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by zntA (protein.P37617). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), Lead (molecule.C06696). Products: ADP (molecule.C00008), H+ (molecule.C00080), Lead (molecule.C06696), phosphate (molecule.ecocyc.Pi).

## Annotation

PB+2 + ATP + WATER -> PB+2 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P37617|protein.P37617]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06696|molecule.C06696]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06696|molecule.C06696]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-452`

## Notes

PB+2 + ATP + WATER -> PB+2 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
