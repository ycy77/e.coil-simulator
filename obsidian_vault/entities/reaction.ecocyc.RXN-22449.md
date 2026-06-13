---
entity_id: "reaction.ecocyc.RXN-22449"
entity_type: "reaction"
name: "L-threonine:Na+ symport"
source_database: "EcoCyc"
source_id: "RXN-22449"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-threonine:Na+ symport

`reaction.ecocyc.RXN-22449`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22449`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

NA+ + THR -> NA+ + THR; direction=LEFT-TO-RIGHT EcoCyc reaction equation: NA+ + THR -> NA+ + THR; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by sstT (protein.P0AGE4). Substrates: L-Threonine (molecule.C00188), Sodium cation (molecule.C01330). Products: L-Threonine (molecule.C00188), Sodium cation (molecule.C01330).

## Annotation

NA+ + THR -> NA+ + THR; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AGE4|protein.P0AGE4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00188|molecule.C00188]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00188|molecule.C00188]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22449`

## Notes

NA+ + THR -> NA+ + THR; direction=LEFT-TO-RIGHT
