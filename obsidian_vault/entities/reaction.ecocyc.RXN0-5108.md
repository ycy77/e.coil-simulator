---
entity_id: "reaction.ecocyc.RXN0-5108"
entity_type: "reaction"
name: "RXN0-5108"
source_database: "EcoCyc"
source_id: "RXN0-5108"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5108

`reaction.ecocyc.RXN0-5108`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5108`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GDP-MANNOSE + WATER -> PROTON + GMP + MANNOSE-1P; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GDP-MANNOSE + WATER -> PROTON + GMP + MANNOSE-1P; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by GDP-mannose hydrolase (complex.ecocyc.CPLX0-3971). Substrates: H2O (molecule.C00001), GDP-mannose (molecule.C00096). Products: H+ (molecule.C00080), GMP (molecule.C00144), D-Mannose 1-phosphate (molecule.C00636).

## Annotation

GDP-MANNOSE + WATER -> PROTON + GMP + MANNOSE-1P; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3971|complex.ecocyc.CPLX0-3971]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00144|molecule.C00144]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00636|molecule.C00636]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00096|molecule.C00096]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5108`

## Notes

GDP-MANNOSE + WATER -> PROTON + GMP + MANNOSE-1P; direction=PHYSIOL-LEFT-TO-RIGHT
