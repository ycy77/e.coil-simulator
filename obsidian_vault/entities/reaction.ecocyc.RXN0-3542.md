---
entity_id: "reaction.ecocyc.RXN0-3542"
entity_type: "reaction"
name: "RXN0-3542"
source_database: "EcoCyc"
source_id: "RXN0-3542"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-3542

`reaction.ecocyc.RXN0-3542`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-3542`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

THIAMINE-PYROPHOSPHATE + WATER -> PROTON + THIAMINE-P + Pi; direction=REVERSIBLE EcoCyc reaction equation: THIAMINE-PYROPHOSPHATE + WATER -> PROTON + THIAMINE-P + Pi; direction=REVERSIBLE.

## Biological Role

Catalyzed by nudJ (protein.P0AEI6). Substrates: H2O (molecule.C00001), Thiamin diphosphate (molecule.C00068). Products: H+ (molecule.C00080), Thiamin monophosphate (molecule.C01081), phosphate (molecule.ecocyc.Pi).

## Annotation

THIAMINE-PYROPHOSPHATE + WATER -> PROTON + THIAMINE-P + Pi; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AEI6|protein.P0AEI6]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01081|molecule.C01081]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00068|molecule.C00068]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-3542`

## Notes

THIAMINE-PYROPHOSPHATE + WATER -> PROTON + THIAMINE-P + Pi; direction=REVERSIBLE
