---
entity_id: "reaction.ecocyc.R170-RXN"
entity_type: "reaction"
name: "R170-RXN"
source_database: "EcoCyc"
source_id: "R170-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# R170-RXN

`reaction.ecocyc.R170-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:R170-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CU+2 + NADH -> CU+ + NAD + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CU+2 + NADH -> CU+ + NAD + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ndh (protein.P00393). Substrates: NADH (molecule.C00004), Cu2+ (molecule.ecocyc.CU_2). Products: NAD+ (molecule.C00003), H+ (molecule.C00080), Cu+ (molecule.ecocyc.CU_).

## Annotation

CU+2 + NADH -> CU+ + NAD + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P00393|protein.P00393]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CU|molecule.ecocyc.CU_]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:R170-RXN`

## Notes

CU+2 + NADH -> CU+ + NAD + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
