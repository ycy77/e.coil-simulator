---
entity_id: "reaction.ecocyc.RXN0-6957"
entity_type: "reaction"
name: "RXN0-6957"
source_database: "EcoCyc"
source_id: "RXN0-6957"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6957

`reaction.ecocyc.RXN0-6957`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6957`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-13851 + WATER -> CPD-13852 + PPI + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-13851 + WATER -> CPD-13852 + PPI + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nudG (protein.P77788). Substrates: H2O (molecule.C00001), 2-hydroxy-dATP (molecule.ecocyc.CPD-13851). Products: Diphosphate (molecule.C00013), H+ (molecule.C00080), 2-hydroxy-dAMP (molecule.ecocyc.CPD-13852).

## Annotation

CPD-13851 + WATER -> CPD-13852 + PPI + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P77788|protein.P77788]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-13852|molecule.ecocyc.CPD-13852]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-13851|molecule.ecocyc.CPD-13851]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6957`

## Notes

CPD-13851 + WATER -> CPD-13852 + PPI + PROTON; direction=LEFT-TO-RIGHT
