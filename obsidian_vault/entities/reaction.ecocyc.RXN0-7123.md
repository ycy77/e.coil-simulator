---
entity_id: "reaction.ecocyc.RXN0-7123"
entity_type: "reaction"
name: "RXN0-7123"
source_database: "EcoCyc"
source_id: "RXN0-7123"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7123

`reaction.ecocyc.RXN0-7123`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7123`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Menaquinones + PROTON + NADH -> Menaquinols + NAD; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Menaquinones + PROTON + NADH -> Menaquinols + NAD; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ndh (protein.P00393). Substrates: NADH (molecule.C00004), H+ (molecule.C00080), Menaquinone (molecule.C00828). Products: NAD+ (molecule.C00003), Menaquinol (molecule.C05819).

## Annotation

Menaquinones + PROTON + NADH -> Menaquinols + NAD; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P00393|protein.P00393]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05819|molecule.C05819]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00828|molecule.C00828]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7123`

## Notes

Menaquinones + PROTON + NADH -> Menaquinols + NAD; direction=LEFT-TO-RIGHT
