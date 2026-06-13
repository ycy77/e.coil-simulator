---
entity_id: "reaction.ecocyc.TRANS-RXN-122"
entity_type: "reaction"
name: "glutamate:Na+ symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-122"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# glutamate:Na+ symport

`reaction.ecocyc.TRANS-RXN-122`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-122`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

NA+ + GLT -> NA+ + GLT; direction=REVERSIBLE EcoCyc reaction equation: NA+ + GLT -> NA+ + GLT; direction=REVERSIBLE.

## Biological Role

Catalyzed by gltS (protein.P0AER8). Substrates: L-Glutamate (molecule.C00025), Sodium cation (molecule.C01330). Products: L-Glutamate (molecule.C00025), Sodium cation (molecule.C01330).

## Annotation

NA+ + GLT -> NA+ + GLT; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AER8|protein.P0AER8]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-122`

## Notes

NA+ + GLT -> NA+ + GLT; direction=REVERSIBLE
