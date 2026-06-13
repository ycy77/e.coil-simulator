---
entity_id: "reaction.ecocyc.RXN-15761"
entity_type: "reaction"
name: "RXN-15761"
source_database: "EcoCyc"
source_id: "RXN-15761"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15761

`reaction.ecocyc.RXN-15761`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15761`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-8876 + WATER -> CPD-7867 + SULFATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-8876 + WATER -> CPD-7867 + SULFATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yjcS (protein.P32717). Substrates: H2O (molecule.C00001), dodecyl sulfate (molecule.ecocyc.CPD-8876). Products: Sulfate (molecule.C00059), H+ (molecule.C00080), dodecan-1-ol (molecule.ecocyc.CPD-7867).

## Annotation

CPD-8876 + WATER -> CPD-7867 + SULFATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P32717|protein.P32717]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00059|molecule.C00059]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-7867|molecule.ecocyc.CPD-7867]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-8876|molecule.ecocyc.CPD-8876]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15761`

## Notes

CPD-8876 + WATER -> CPD-7867 + SULFATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
