---
entity_id: "reaction.ecocyc.RXN0-4083"
entity_type: "reaction"
name: "L-serine:Na+ symport"
source_database: "EcoCyc"
source_id: "RXN0-4083"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-serine:Na+ symport

`reaction.ecocyc.RXN0-4083`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-4083`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

NA+ + SER -> NA+ + SER; direction=REVERSIBLE EcoCyc reaction equation: NA+ + SER -> NA+ + SER; direction=REVERSIBLE.

## Biological Role

Catalyzed by sstT (protein.P0AGE4). Substrates: L-Serine (molecule.C00065), Sodium cation (molecule.C01330). Products: L-Serine (molecule.C00065), Sodium cation (molecule.C01330).

## Annotation

NA+ + SER -> NA+ + SER; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AGE4|protein.P0AGE4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-4083`

## Notes

NA+ + SER -> NA+ + SER; direction=REVERSIBLE
