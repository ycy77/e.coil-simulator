---
entity_id: "reaction.ecocyc.RXN0-6368"
entity_type: "reaction"
name: "RXN0-6368"
source_database: "EcoCyc"
source_id: "RXN0-6368"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6368

`reaction.ecocyc.RXN0-6368`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6368`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DIHYDROMONAPTERIN-TRIPHOSPHATE + WATER -> PROTON + CPD-11770 + Pi; direction=LEFT-TO-RIGHT EcoCyc reaction equation: DIHYDROMONAPTERIN-TRIPHOSPHATE + WATER -> PROTON + CPD-11770 + Pi; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), 7,8-Dihydromonapterin 3'-triphosphate (molecule.C21094). Products: H+ (molecule.C00080), 7,8-Dihydromonapterin (molecule.C21008), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY0-1433` tetrahydromonapterin biosynthesis (EcoCyc)

## Annotation

DIHYDROMONAPTERIN-TRIPHOSPHATE + WATER -> PROTON + CPD-11770 + Pi; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1433` tetrahydromonapterin biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C21008|molecule.C21008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C21094|molecule.C21094]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6368`

## Notes

DIHYDROMONAPTERIN-TRIPHOSPHATE + WATER -> PROTON + CPD-11770 + Pi; direction=LEFT-TO-RIGHT
