---
entity_id: "reaction.ecocyc.TRANS-RXN-123"
entity_type: "reaction"
name: "D-galacturonate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-123"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# D-galacturonate:proton symport

`reaction.ecocyc.TRANS-RXN-123`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-123`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

D-GALACTURONATE + PROTON -> D-GALACTURONATE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: D-GALACTURONATE + PROTON -> D-GALACTURONATE + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by exuT (protein.P0AA78). Substrates: H+ (molecule.C00080), D-Galacturonate (molecule.C00333). Products: H+ (molecule.C00080), D-Galacturonate (molecule.C00333).

## Annotation

D-GALACTURONATE + PROTON -> D-GALACTURONATE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AA78|protein.P0AA78]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00333|molecule.C00333]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00333|molecule.C00333]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-123`

## Notes

D-GALACTURONATE + PROTON -> D-GALACTURONATE + PROTON; direction=REVERSIBLE
