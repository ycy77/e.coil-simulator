---
entity_id: "reaction.ecocyc.TRANS-RXN-117"
entity_type: "reaction"
name: "pantothenate:Na+ symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-117"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# pantothenate:Na+ symport

`reaction.ecocyc.TRANS-RXN-117`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-117`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

NA+ + PANTOTHENATE -> NA+ + PANTOTHENATE; direction=REVERSIBLE EcoCyc reaction equation: NA+ + PANTOTHENATE -> NA+ + PANTOTHENATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by panF (protein.P16256). Substrates: Pantothenate (molecule.C00864), Sodium cation (molecule.C01330). Products: Pantothenate (molecule.C00864), Sodium cation (molecule.C01330).

## Annotation

NA+ + PANTOTHENATE -> NA+ + PANTOTHENATE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P16256|protein.P16256]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00864|molecule.C00864]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00864|molecule.C00864]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-117`

## Notes

NA+ + PANTOTHENATE -> NA+ + PANTOTHENATE; direction=REVERSIBLE
