---
entity_id: "reaction.ecocyc.PROTOPORGENOXI-RXN"
entity_type: "reaction"
name: "PROTOPORGENOXI-RXN"
source_database: "EcoCyc"
source_id: "PROTOPORGENOXI-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PROTOPORGENOXI-RXN

`reaction.ecocyc.PROTOPORGENOXI-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PROTOPORGENOXI-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A reaction in porphyrin biosynthesis. EcoCyc reaction equation: PROTOPORPHYRINOGEN + OXYGEN-MOLECULE -> PROTOPORPHYRIN_IX + HYDROGEN-PEROXIDE; direction=PHYSIOL-LEFT-TO-RIGHT. A reaction in porphyrin biosynthesis.

## Biological Role

Substrates: Oxygen (molecule.C00007), Protoporphyrinogen IX (molecule.C01079). Products: Hydrogen peroxide (molecule.C00027), Protoporphyrin (molecule.C02191).

## Annotation

A reaction in porphyrin biosynthesis.

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02191|molecule.C02191]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01079|molecule.C01079]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PROTOPORGENOXI-RXN`

## Notes

PROTOPORPHYRINOGEN + OXYGEN-MOLECULE -> PROTOPORPHYRIN_IX + HYDROGEN-PEROXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
