---
entity_id: "reaction.ecocyc.RXN-14124"
entity_type: "reaction"
name: "RXN-14124"
source_database: "EcoCyc"
source_id: "RXN-14124"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14124

`reaction.ecocyc.RXN-14124`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14124`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

CPD-3708 + WATER -> GUANOSINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-3708 + WATER -> GUANOSINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cpdB (protein.P08331). Substrates: H2O (molecule.C00001), Guanosine 3'-phosphate (molecule.C06193). Products: Guanosine (molecule.C00387), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD-3708 + WATER -> GUANOSINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P08331|protein.P08331]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00387|molecule.C00387]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06193|molecule.C06193]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14124`

## Notes

CPD-3708 + WATER -> GUANOSINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
