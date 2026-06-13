---
entity_id: "reaction.ecocyc.TRANS-RXN-118"
entity_type: "reaction"
name: "L-proline:Na+ symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-118"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-proline:Na+ symport

`reaction.ecocyc.TRANS-RXN-118`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-118`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

NA+ + PRO -> NA+ + PRO; direction=REVERSIBLE EcoCyc reaction equation: NA+ + PRO -> NA+ + PRO; direction=REVERSIBLE.

## Biological Role

Catalyzed by putP (protein.P07117). Substrates: L-Proline (molecule.C00148), Sodium cation (molecule.C01330). Products: L-Proline (molecule.C00148), Sodium cation (molecule.C01330).

## Annotation

NA+ + PRO -> NA+ + PRO; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P07117|protein.P07117]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00148|molecule.C00148]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00148|molecule.C00148]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-118`

## Notes

NA+ + PRO -> NA+ + PRO; direction=REVERSIBLE
