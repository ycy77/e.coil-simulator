---
entity_id: "reaction.ecocyc.RXN-23340"
entity_type: "reaction"
name: "RXN-23340"
source_database: "EcoCyc"
source_id: "RXN-23340"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23340

`reaction.ecocyc.RXN-23340`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23340`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PRENOL + NADP -> PRENAL + NADPH + PROTON; direction=REVERSIBLE EcoCyc reaction equation: PRENOL + NADP -> PRENAL + NADPH + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by yahK (protein.P75691). Substrates: NADP+ (molecule.C00006), Prenol (molecule.C01390). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 3-methylbut-2-enal (molecule.ecocyc.PRENAL).

## Annotation

PRENOL + NADP -> PRENAL + NADPH + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P75691|protein.P75691]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.PRENAL|molecule.ecocyc.PRENAL]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01390|molecule.C01390]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23340`

## Notes

PRENOL + NADP -> PRENAL + NADPH + PROTON; direction=REVERSIBLE
