---
entity_id: "reaction.ecocyc.RXN0-383"
entity_type: "reaction"
name: "RXN0-383"
source_database: "EcoCyc"
source_id: "RXN0-383"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-383

`reaction.ecocyc.RXN0-383`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-383`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CTP + WATER -> PROTON + CMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CTP + WATER -> PROTON + CMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), CTP (molecule.C00063). Products: Diphosphate (molecule.C00013), CMP (molecule.C00055), H+ (molecule.C00080).

## Annotation

CTP + WATER -> PROTON + CMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00055|molecule.C00055]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00063|molecule.C00063]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-383`

## Notes

CTP + WATER -> PROTON + CMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
