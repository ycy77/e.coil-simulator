---
entity_id: "reaction.ecocyc.RXN-8487"
entity_type: "reaction"
name: "RXN-8487"
source_database: "EcoCyc"
source_id: "RXN-8487"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-8487

`reaction.ecocyc.RXN-8487`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8487`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

TYR + CPD-8651 -> PROTON + CPD-8670 + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: TYR + CPD-8651 -> PROTON + CPD-8670 + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: L-Tyrosine (molecule.C00082), betalamate (molecule.ecocyc.CPD-8651). Products: H2O (molecule.C00001), H+ (molecule.C00080), portulacaxanthin II (molecule.ecocyc.CPD-8670).

## Annotation

TYR + CPD-8651 -> PROTON + CPD-8670 + WATER; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-8670|molecule.ecocyc.CPD-8670]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00082|molecule.C00082]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-8651|molecule.ecocyc.CPD-8651]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8487`

## Notes

TYR + CPD-8651 -> PROTON + CPD-8670 + WATER; direction=LEFT-TO-RIGHT
