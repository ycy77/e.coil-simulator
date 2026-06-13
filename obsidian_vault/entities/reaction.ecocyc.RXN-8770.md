---
entity_id: "reaction.ecocyc.RXN-8770"
entity_type: "reaction"
name: "RXN-8770"
source_database: "EcoCyc"
source_id: "RXN-8770"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-8770

`reaction.ecocyc.RXN-8770`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8770`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ADENOSYLCOBALAMIN-5-P + WATER -> ADENOSYLCOBALAMIN + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ADENOSYLCOBALAMIN-5-P + WATER -> ADENOSYLCOBALAMIN + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cobC (protein.P52086). Substrates: H2O (molecule.C00001), adenosylcobalamin 5'-phosphate (molecule.ecocyc.ADENOSYLCOBALAMIN-5-P). Products: Cobamide coenzyme (molecule.C00194), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.COBALSYN-PWY` superpathway of adenosylcobalamin salvage from cobinamide I (EcoCyc)
- `ecocyc.PWY-5509` adenosylcobalamin biosynthesis from adenosylcobinamide-GDP I (EcoCyc)

## Annotation

ADENOSYLCOBALAMIN-5-P + WATER -> ADENOSYLCOBALAMIN + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.COBALSYN-PWY` superpathway of adenosylcobalamin salvage from cobinamide I (EcoCyc)
- `ecocyc.PWY-5509` adenosylcobalamin biosynthesis from adenosylcobinamide-GDP I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P52086|protein.P52086]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00194|molecule.C00194]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.ADENOSYLCOBALAMIN-5-P|molecule.ecocyc.ADENOSYLCOBALAMIN-5-P]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8770`

## Notes

ADENOSYLCOBALAMIN-5-P + WATER -> ADENOSYLCOBALAMIN + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
